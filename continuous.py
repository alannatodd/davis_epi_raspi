from datetime import datetime
from libcamera import controls
from picamera2 import Picamera2, Preview, MappedArray
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import RPi.GPIO as GPIO
from threading import Thread

import cv2
import os
import sys
import shutil
import time

#### NOTE: This file should be placed in the /code directory ####

#### PI / FILE STRUCTURE SETUP ####
# Modify the following variables to match the individual pi's setup
pi_username = "davis_epi_raspi14"

# This subdirectory must exist under the /code directory
subdir = "goats"
# Verify the appearance of the drive's name when connected to the pi 
usb_name = "DUAL DRIVE"

#### FLASH DRIVE SETUP ####
flash_path = f"/media/{pi_username}/{usb_name}/"
to_copy = []

#### TIMESTAMP OVERLAY OPTIONS ####
color = (0, 255, 0)
origin = (0, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.75
thickness = 2

#### ERROR FILE OPTIONS ####
# Actual file name will be set below
error_file = ""

#### LED SETUP OPTIONS ####
sensor_pin = 23
use_led = True

#### LED ERROR CODES ####
led_error_codes = {
    "datetime": 1,
    "file_setup": 2,
    "camera_setup": 3,
    "recording": 4,
    "thread": 5,
    "copy_files": 6,
    "log_file": 7
}

# A function to set up the LED Light
def setup_led():
    if not use_led:
        return
    
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor_pin, GPIO.OUT)
    except Exception as e:
        print(f"Error setting up LED {e}")
        
def cleanup_led():
    if not use_led:
        return

    GPIO.cleanup()
        
def led_print(duration_seconds, times=1, pause_seconds=0, pause_between=0.5):
    if not use_led:
        return

    if times == 0:
        # Print a "zero"
        for i in range(0, 3):
            GPIO.output(sensor_pin, GPIO.HIGH)
            time.sleep(duration_seconds/3)
            GPIO.output(sensor_pin, GPIO.LOW)
            time.sleep(duration_seconds/3)
    
    else:
        for i in range(0, times):
            GPIO.output(sensor_pin, GPIO.HIGH)
            time.sleep(duration_seconds)
            GPIO.output(sensor_pin, GPIO.LOW)
            time.sleep(pause_between)
    
    time.sleep(pause_seconds)
    
def led_print_error_indicator(long=False):
    if not use_led:
        return
    
    if long:
        led_print(10, 1, 2, 1)
    else:
        led_print(0.1, 20, 2, 0.1)
        
def led_print_error_code(name, repeat=True):
    if not use_led:
        True
    
    code = led_error_codes.get(name, None)
    if code is not None:
        times = 3 if repeat else 1
        for i in range(0, times):
            led_print(1, code, 4)
        
def led_print_datetime():
    if not use_led:
        return
    
    time.sleep(3)
    
    current = datetime.now()

    led_print(1, current.month, 2)
    
    time.sleep(3)
    
    tens = current.day // 10
    ones = current.day % 10
    led_print(1, tens, 2)
    led_print(1, ones, 2)
    
    time.sleep(3)
    
    past_2000 = current.year % 2000
    year_tens = past_2000 // 10
    year_ones = past_2000 % 10

    led_print(1, year_tens, 2)
    led_print(1, year_ones, 2)
        
    time.sleep(3)
    
    hour_tens = current.hour // 10
    hour_ones = current.hour % 10
        
    led_print(1, hour_tens, 2)
    led_print(1, hour_ones, 2)
    
    time.sleep(3)
    
    minute_tens = current.minute // 10
    minute_ones = current.minute % 10
    
    led_print(1, minute_tens, 2)
    led_print(1, minute_ones, 2)



# A function to app a timestamp overlay on the video using the settings set in TIMESTAMP OVERLAY OPTIONS section
def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, color, thickness)

# Function to copy files to the flash drive
def copy_files():
    global to_copy
    
    # Copy files from the SD card to the flash drive if it is connected
    if not os.path.exists(flash_path):
        return
    
    for i in range(len(to_copy)):
        try:
            flash_file_path = f"{flash_path}{to_copy[i]}"
            shutil.copyfile(to_copy[i], flash_file_path)
        except Exception as e:
            print(f"exc {e}")
            # write error to error logs
            # The video file will not be removed from the pi if it was not successfully copied,
            # but the program will not try to copy it to the flash drive again
            global error_file
            led_print_error_indicator(True)
            led_print_error_code("copy_files")

            to_copy = to_copy[i:]
            return
        
        # If successfully copied to flash drive, remove the video file from the pi
        os.remove(to_copy[i])
        
    # Remove file names from to_copy
    to_copy = []
    
def write_error(exc):
    try:
        # Write any errors to the error log file
        with open(error_file, 'a') as f:
            f.write(f'{datetime.now()} {exc}')
    
    except Exception as e:
        print(f"Exception writing error to log file {e}")
        led_print_error_indicator()
        led_print_error_code("log_file")
    
try:
    setup_led()
except Exception as e:
    print(f"Error setting up LED {e}")
    exit()
    
try:
    # Turnon LED for 5 seconds to indicate program has started successfully
    led_print(5, 1, 2)
    led_print_datetime()
except Exception as e:
    print(f"Error w printing datetime: {e}")
    led_print_error_indicator()
    led_print_error_code("datetime")
    cleanup_led()
    exit()
    
try:
    # Create a file to store any logged errors
    if not os.path.exists(subdir):
        os.makedirs(subdir)
        
    error_file = f"{subdir}/errors_{datetime.now().strftime('%Y-%m-%d_%H.%M')}.txt"
    
    if not os.path.exists(error_file):
        with open(error_file, 'x') as f:
            f.write("Error log:\n")

except Exception as e:
    print(f"File setup exception {e}")
    
    # Show error via light
    led_print_error_indicator()
    led_print_error_code("file_setup")
    cleanup_led()
    exit()
    
try:
     #### CAMERA SETUP ####
    camera = Picamera2()

    # Set the video size and display type
    video_config = camera.create_video_configuration(main={"size":(480,480)}, lores={"size":(360,360)}, display="lores")
    camera.configure(video_config)
    encoder = H264Encoder(10000000)
    keep_running = True

    # The length of each video in seconds (60 seconds * 20 minutes = 1200)
    minutes = 20
    seconds = minutes * 60

    ## Uncomment/comment lines below to turn on/off continuous autofocus and set lens position
    # camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
    camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5})
    
    camera.pre_callback = apply_timestamp
    
except Exception as e:
    print(f"Camera setup exception {e}")
    
    # Show error via light
    led_print_error_indicator()
    led_print_error_code("camera_setup")
    cleanup_led()
    exit()
    
counter = 1
cam_error_counter = 0
thread_error_counter = 0
while keep_running:
    try:
        # Start video recording
        sd_file_path = f"{subdir}/{pi_username}_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}_{minutes}min.mp4"
        camera.start_and_record_video(sd_file_path, duration=seconds)
        to_copy.append(sd_file_path)
        
    except Exception as e:
        cam_error_counter += 1
        write_error(e)
        led_print_error_indicator(True)
        led_print_error_code("recording")
        
        if cam_error_counter > 10:
            keep_running = False
            continue
        
        time.sleep(65)
        
    try:
        # Use a thread to copy video file to flash drive (if drive connected) so next file recording is not blocked
        t = Thread(target=copy_files)
        t.start()

    except Exception as e:
        thread_error_counter += 1
        write_error(e)
        led_print_error_indicator(True)
        led_print_error_code("thread")
        
        if thread_error_counter > 10:
            keep_running = False
            continue
        
        time.sleep(65)


display_error_led = True
while display_error_led:
    cur = datetime.now()
    # Only turn on light during daylght hours
    if cur.hour < 18 and cur.hour > 7:
        for i in range(0, 10):
            led_print(60, 1, 2)
            led_print_error_code("recording", False) if cam_error_counter > 0 else None
            led_print_error_code("thread", False) if thread_error_counter > 0 else None
            
    else:
        time.sleep(600)
    
time.sleep(60)

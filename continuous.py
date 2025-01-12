from picamera2 import Picamera2, Preview, MappedArray
from libcamera import controls
import time
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import os
from datetime import datetime
import sys
import shutil
from threading import Thread
import cv2

#### NOTE: This file should be placed in the /code directory ####

#### PI / FILE STRUCTURE SETUP ####
pi_username = os.getlogin() # ie, davis_epi_raspi1

# Modify the following variables to match the individual pi's setup
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
scale = 1
thickness = 2

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

## Uncomment to turn on continuous autofocus; Keep commented out to turn off autofocus
#camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

# Create a file to store any logged errors
error_file = f"{subdir}/errors_{datetime.now().strftime('%Y-%m-%d_%H.%M')}.txt"
with open(error_file, 'x') as f:
    f.write("Error log:\n")

# A function to app a timestamp overlay on the video using the settings set in TIMESTAMP OVERLAY OPTIONS section
def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, color, thickness)

# Function to copy files to the flash drive
def copy_files():
    global to_copy
    
    # Copy files from the SD card to the flash drive if it is connected
    for i in range(len(to_copy)):
        try:
            flash_file_path = f"{flash_path}{to_copy[i]}"
            shutil.copyfile(to_copy[i], flash_file_path)
        except Exception as e:
            # write error to error logs
            # The video file will not be removed from the pi if it was not successfully copied,
            # but the program will not try to copy it to the flash drive again
            global error_file
            with open(error_file, 'a') as f:
                f.write(f'{datetime.now()} {e}')

            to_copy = to_copy[i:]
            return
        
        # If successfully copied to flash drive, remove the video file from the pi
        os.remove(to_copy[i])
        
    # Remove file names from to_copy
    to_copy = []
        
counter = 1
camera.pre_callback = apply_timestamp
while keep_running:
    try:
        # Start video recording
        sd_file_path = f"{subdir}/{username}_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}_{minutes}min.mp4"
        camera.start_and_record_video(sd_file_path, duration=seconds)
        to_copy.append(sd_file_path)
        
        # Use a thread to copy video file to flash drive (if drive connected) so next file recording is not blocked
        t = Thread(target=copy_files)
        t.start()

    except Exception as e:
        # Write any errors to the error log file
        with open(error_file, 'a') as f:
                f.write(f'{datetime.now()} {e}')

time.sleep(60)


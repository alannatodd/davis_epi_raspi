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

# 20 minutes
seconds = 1200

# Flash drive setup
flash_path = '/media/fishpi10/DUAL DRIVE/'
to_copy = []
username = os.getlogin()

# Timestamp overlay options
color = (0, 255, 0)
origin = (0, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

# camera setup
camera = Picamera2()
#video_config = camera.create_video_configuration()
video_config = camera.create_video_configuration(main={"size":(480,480)}, lores={"size":(360,360)}, display="lores")
camera.configure(video_config)
encoder = H264Encoder(10000000)
#camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

keep_running = True

error_file = f"fish/errors_{datetime.now().strftime('%Y-%m-%d_%H.%M')}.txt"
with open(error_file, 'x') as f:
    f.write("Error log:\n")

def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, color, thickness)

def copy_files():
    global to_copy
    
    # Copy files from the SD card to the flash drive if it is connected
    for i in range(len(to_copy)):
        try:
            flash_file_path = f"{flash_path}{to_copy[i]}"
            shutil.copyfile(to_copy[i], flash_file_path)
        except Exception as e:
            # write error to error logs
            global error_file
            with open(error_file, 'a') as f:
                f.write(f'{datetime.now()} {e}')

            to_copy = to_copy[i:]
            return
        
        # If successfully copied to flash drive, remove from SD card
        os.remove(to_copy[i])
        
    # Remove file names from to_copy
    to_copy = []
        
counter = 1
camera.pre_callback = apply_timestamp
while keep_running:
    try:
        # Start video recording
        sd_file_path = f"fish/fishpi10_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}_20min.mp4"
        camera.start_and_record_video(sd_file_path, duration=seconds)
        to_copy.append(sd_file_path)
        
        # Copy file to flash drive if connected as a thread so next file recording is not blocked
        t = Thread(target=copy_files)
        t.start()

    except Exception as e:
        with open(error_file, 'a') as f:
                f.write(f'{datetime.now()} {e}')

time.sleep(60)


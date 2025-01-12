from libcamera import controls
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

import datetime as dt
import os
import sys
import time

# Determine how long of a video was requested and convert to seconds
minutes = int(sys.argv[1])
seconds = minutes * 5

# Set file output destination within the code/ directory
subdir = "fish"

#### CAMERA SETUP ####
camera = Picamera2()
video_config = camera.create_video_configuration(main={"size":(480,480)}, lores={"size":(360,360)}, display="lores")
camera.configure(video_config)

encoder = H264Encoder(10000000)
camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

def record_video():
    output = FfmpegOutput(f"{subdir}/{dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}_{minutes}min.mp4")
    camera.start_recording(encoder, output)
    
    
def finish_video():
    camera.stop_recording()


record_video()

# Sleep for length of video and then stop recording
time.sleep(seconds)
finish_video()

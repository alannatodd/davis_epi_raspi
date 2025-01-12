from picamera2 import Picamera2, Preview
from libcamera import controls
import time
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import os
import datetime as dt
import sys

minutes = int(sys.argv[1])
seconds = minutes * 5

destination = '/code/fish/video'

camera = Picamera2()
#video_config = camera.create_video_configuration()
video_config = camera.create_video_configuration(main={"size":(480,480)}, lores={"size":(360,360)}, display="lores")
camera.configure(video_config)

encoder = H264Encoder(10000000)
camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

def record_video():
    output = FfmpegOutput(f"fish/{dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}_{minutes}min.mp4")
    #output = FfmpegOutput(f"fish/{dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.mp4')}")
    camera.start_recording(encoder,output)
    
    
def finish_video():
    camera.stop_recording()
    
record_video()

time.sleep(seconds)
finish_video()
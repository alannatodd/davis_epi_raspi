# In-Field Setup
## Setup (Per Pi)
1.	Connect pi to monitor, keyboard, mouse, power. Connect monitor to power. [(guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/6)
2.	Power on the Pi 
3.	Open terminal and find running `continuous.py` python process and kill it [Guide](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/find_and_kill_process.md)
4.	Use `variable.py`, `libcamera-vid`, or `libcv` to test and adjust video settings - height, autofocus, infrared etc [Guide](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/adjust_focus.md)
5.	Connect to hotspot or WiFi to update date + time so timestamps will be accurate [Guide](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/syncing_time.md)
6.	Disconnect from hotspot/WiFi if prohibited during experiment
7.	Update `continuous.py` with preferred settings
8.	Run `reboot` in terminal and disconnect mouse + monitor
9.	After 20+ minutes, you can remove usb to check that videos are recording properly

Unless changed, the Pi will record 20 minute long videos. Every time a recording is finished, the python process will check if there a USB connected to the Pi in the expected location with the expected name. If so, it will copy the video (and any other videos that have yet to be copied) to the USB drive and then delete it from the pi. If there is no USB connected to the Pi when the recording ends, the video file will be added to a list of files to be copied once a USB is connected. 

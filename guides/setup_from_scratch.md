# Davis Epi Lab Raspberry Pi Setup 

## Supplies
### Supplies needed per Pi (From scratch)
-	[Raspberry Pi 4 Model B + power cable](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
-	[Raspberry Pi case with fan + connection accessories](https://vilros.com/products/vilros-accessories-starter-pack-for-raspberry-pi-4-includes-fan-cooled-case-power-supply-heatsink-set-of-4-micro-hdmi-usb-c-adapters)
-	Wide angle camera in [regular](https://vilros.com/products/raspberry-pi-camera-3?variant=39984853155934) or [noir (infrared for night video)](https://vilros.com/products/raspberry-pi-camera-3?variant=39984853221470)
-	microSD card (large storage size: 256 GB - 1 TB+)
-	USB drive (large storage size: 256 GB - 1 TB+)
-	Carabiner (depending on setup)
-	Lanyard
-	Tape (painters & electrical)

### Supplies needed per pi (Pre-existing setup)
-	Raspberry Pi (in case) + power cable
-	Laptop
-	Laptop / Tablet to offload videos

### Supplies needed (General) 
-	Portable monitor + power cable
    * HDMI to miniHDMI cable (depending on portable monitor)
    * microHDMI to HDMI adapter
-	Computer mouse (with USB cable or USB Bluetooth adapter)
-	Computer Keyboard (with USB cable or USB Bluetooth adapter)
-	Power strip(s) 
-	Extension cord(s)
-	Hotspot-enabled smartphone
-	Small folding table or tv-dinner stand to put the monitor + keyboard + mouse on in the field

## Setup
### From Scratch 
1.	Download Raspberry Pi image from website (which image?); link [(guide for 1-4)](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)
2.	Download Raspberry Pi Imager on laptop
3.	Insert unformatted SD card into laptop either directly or via SD card reader adapter 
4.	Run through Raspberry Pi formatting [(alt guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/4)
5.	Insert SD card into Raspberry Pi (see end of guide above or [here](https://www.raspberrypi.com/documentation/computers/getting-started.html#set-up-your-raspberry-pi)]
6.	Connect camera to Raspberry Pi [(guide pt 1)](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1) [(guide pt2)](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
7.	Insert raspberry pi into case, connecting fan wires to correct pins on pi (show diagram). Carefully fold camera band (try not to crease) to fit inside the case. Using electrical tape, tape camera to front or side of the case depending on desired setup.
8.	Optional: If going to be used in an environment that may be wet, tape the back of the Pi with painters or electrical tape to prevent water from dripping into the back of the case.
9.	Connect Raspberry Pi to external monitor, mouse, keyboard, power. Insert USB drive. Make sure to connect to monitor before powering on. Use the first microHDMI port next to the usb-c power port on the Pi. [(guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/6)
10. Power on the Raspberry Pi 
11. Set keyboard to US
12. Login – username and password: 
13. Connect Pi to wifi network
14. Open terminal

    <img src=screenshots/terminal.png>
15. Run updates and installs – tbd 
16. In terminal, make directory called 'code': type `sudo mkdir code` in terminal and press enter - you may be prompted to enter password
    - [more info on sudo if interested](https://en.wikipedia.org/wiki/Sudo)
17. Make desired directory under `/code` – ie 'fish' or 'goats' – type `mkdir /code/goats` and press enter
18. Open Chromium browser and navigate to this davis_epi_raspi GitHub repo
19. Download needed files and move into /code directory
    - `launcher.sh`
    - `continuous.py`
    - `variable.py`
21. Determine name of USB drive – check in `/media/<username>/`
22. Edit vars in .env.raspi? 
23. Make sure raspberry pi config is correct. 
24. Check rc.local for correct settings 
25. Check config for correct settings
26. Add `launcher.sh` to crontab 
27. Proceed to in the field setup 

### In the field setup – per Pi 
1.	Connect pi to monitor, keyboard, mouse, power. Connect monitor to power. [(guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/6)
2.	Power on the Pi 
3.	Open terminal and find running python process - kill
4.	Use `variable.py`, `libcamera-vid`, or `libcv` to test and adjust video settings - height, autofocus, infrared etc (see `adjust_focus.md`)
5.	Connect to hotspot or WiFi to update date + time so timestamps will be accurate (see `syncing_time.md`)
6.	Disconnect from hotspot/WiFi if prohibited during experiment
7.	Update `continuous.py` with preferred settings
8.	Run `reboot` in terminal and disconnect mouse + monitor
9.	After 20+ minutes, you can remove usb to check that videos are recording properly

Unless changed, the Pi will record 20 minute long videos. Every time a recording is finished, the python process will check if there a USB connected to the Pi in the expected location with the expected name. If so, it will copy the video (and any other videos that have yet to be copied) to the USB drive and then delete it from the pi. If there is no USB connected to the Pi when the recording ends, the video file will be added to a list of files to be copied once a USB is connected. 

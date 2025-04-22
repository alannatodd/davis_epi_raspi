# Davis Epi Lab Raspberry Pi Setup 

## Supplies
### Supplies needed per Pi (From scratch)
-	[Raspberry Pi 4 Model B + power cable](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
-	[Raspberry Pi case with fan + connection accessories](https://vilros.com/products/vilros-accessories-starter-pack-for-raspberry-pi-4-includes-fan-cooled-case-power-supply-heatsink-set-of-4-micro-hdmi-usb-c-adapters)
-	Wide angle camera in [regular]([https://vilros.com/products/raspberry-pi-camera-3](https://vilros.com/products/raspberry-pi-camera-3?variant=39984853155934)) or [noir (infrared for night video)]([https://vilros.com/products/raspberry-pi-camera-3](https://vilros.com/products/raspberry-pi-camera-3?variant=39984853221470))
-	microSD card (large storage size: 256 GB - 1 TB+)
-	USB drive (large storage size: 256 GB - 1 TB+)
-	Carabiner
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
## From Scratch 
1.	Download raspberry pi image from website (which image?); link
2.	Download raspberry pi formatter? 
3.	Insert unformatted SD card into laptop either directly or via SD card reader adapter 
4.	Run through raspberry pi formatting 
5.	Insert SD card into raspberry pi 
6.	Connect camera to raspberry pi 
7.	Insert raspberry pi into case, connecting fan wires to correct pins on pi (show diagram). Carefully fold camera band (try not to crease) to fit inside the case 
8.	Tape the back of the pi to prevent leaks? 
9.	Connect raspberry pi to external monitor, mouse, keyboard, power. Insert USB drive. Make sure to connect to monitor before powering on. Use the first microHDMI port next to the usb-c power port on the pi. 
10.	Power on raspberry pi 
11.	Set keyboard to usq	
12.	Login – username and password: 
13.	Connect pi to wifi network
14.	Open terminal (diagram) 
15.	Run updates and installs – tbd 
16.	Make directory /code `sudo mkdir code`
17.	Make desired directory under /code – ie ‘fish’ or ‘goats’ – mkdir /code/goats
18.	Open chromium browser and navigate to github repo – davis_epi_raspi - https://github.com/alannatodd/davis_epi_raspi/tree/main 
19.	Download files into /code directory – which files? 
20.	Determine name of USB drive – check in /media/<username>/
21.	Edit vars in .env.raspi? 
22.	Make sure raspberry pi config is correct. 
23.	Check rc.local for correct settings 
24.	Check config for correct settings
25.	Add launcher.sh to crontab 
26.	Proceed to in the field setup 

## In the field setup – per pi 
1.	Connect pi to monitor, keyboard, mouse, power. Connect monitor to power. 
2.	Power on the pi 
3.	Open terminal and find running python process - kill
4.	Use variable and libcv or whatever to test and adjust video – height, autofocus, infrared etc. 
5.	Connect to hotspot, update date/time so timestamps will be accurate
6.	Update continuous.py with preferred settings.
7.	Run reboot in terminal and disconnect mouse + monitor
8.	After 20+ minutes, can remove usb to check that videos are recording properly

Unless changed, the pi will record 20 minute long videos. Every time a recording is finished, the python process will check if there a USB connected to the Pi in the expected location with the expected name. If so, it will copy the video (and any other videos that have yet to be copied) to the USB drive and then delete it from the pi. If there is no USB connected to the Pi when the recording ends, the video file will be added to a list of files to be copied once a USB is connected. 

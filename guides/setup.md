# Raspberry Pi Setup 

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
-	Recommended: Small folding table or tv-dinner stand to put the monitor + keyboard + mouse on in the field

## Setup
### From Scratch 
1.	Install a Rasberry Pi Operating System (OS) onto the SD Card [(comprehensive guide)](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)
   - Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on laptop
   - Insert unformatted SD card into laptop either directly or via SD card reader adapter
   - Load an OS onto the SD card using the Raspberry Pi Imager [(alt guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/4)
      - Note: The current Pis are running a 64-bit port of Debian Bullseye. To find this option in the Imager, after clicking OS you must click Raspberry Pi OS (other). It appears as "Raspberry Pi OS (Legacy, 64-bit)". Either the full or regular should be fine, just don't use the lite version since you will need a Desktop. You can also try using the Bookworm port, but I cannot guarantee everything will look or work the same as in this guide.
      
        <img src=screenshots/raspi_os_other.png>
        <img src=screenshots/raspi_os_options.png>
      
2.	Insert SD card into Raspberry Pi (see end of guide above or [here](https://www.raspberrypi.com/documentation/computers/getting-started.html#set-up-your-raspberry-pi))
3.	Connect camera to Raspberry Pi [(guide pt 1)](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1) [(guide pt2)](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
4.	Insert Raspberry Pi into case, connecting fan wires to correct pins on Pi (red to 4 "5V", black to 6 "Ground", blue to 8 "GPIO 14")

  	   <img src=screenshots/raspi_4_pinout.png>
   
6.	Carefully fold camera band (try not to crease) to fit inside the case and put top on. Using electrical tape, tape camera to front or side of the case depending on desired setup.
7.	Optional: If going to be used in an environment that may be wet, tape the back of the Pi with painters or electrical tape to prevent water from dripping into the back of the case.
8. Connect Raspberry Pi to external monitor, mouse, keyboard, power. Insert USB drive. Make sure to connect to monitor before powering on. Use the first microHDMI port next to the usb-c power port on the Pi. [(guide)](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/6)
9. Power on the Raspberry Pi 
10. Set keyboard to US
11. Login
12. Connect Pi to WiFi network
13. Open terminal

    <img src=screenshots/terminal.png>
    
14. In terminal, make a directory called 'code': type `sudo mkdir code` in terminal and press enter - you may be prompted to enter password
    - [more info on sudo if interested](https://en.wikipedia.org/wiki/Sudo)
15. Make desired directory under `/code` – ie 'fish' or 'goats' – ex type `mkdir code/goats` and press enter
16. Open Chromium browser and navigate to this `davis_epi_raspi` GitHub repo
17. Download needed files and move into `/code` directory
   - Files:
      - `launcher.sh`
      - `continuous.py`
      - `variable.py`
   - Steps:
      - Download zip file of code repo
        
        <img src=screenshots/download_zip.png>
        
      - Move the zip file from Downloads to the `/code` directory. In the terminal type: `mv Downloads/davis_epi_raspi-main.zip code/`,
      - Move to code directory: `cd code` 
      - Unzip the repo file into the code directory: `unzip davis_epi_raspi-main.zip`
      - Then move the files from the repo folder up a level to the code directory: `mv -v davis_epi_raspi-main/* .`
        
        <img src=screenshots/move_unzip_repo.png>
        
      - Remove the zip file and davis_epi_raspi-main folder: `rm -rf davis_epi_raspi-main` and `rm davis_epi_raspi-main.zip`
        
        <img src=screenshots/rm_davis_folders.png>
        
18. Determine name of USB drive – check by typing `ls /media/<username>/` in terminal (ie `ls /media/davis_epi_raspi14`) It should be 'DUAL DRIVE' if using USBs from previous projects - if not see `rename_usb.md`

    <img src=screenshots/ls_usb.png>

19. Make sure Raspberry Pi config is correct
    - Select raspberry icon in menu bar -> Preferences -> Raspberry Pi Configuration
    
      <img src=screenshots/raspi_config_toggles.png>

      You can also change keyboard settings, password, and auto-login from here

      <img src=screenshots/raspi_config_keyboard.png>
      <img src=screenshots/raspi_config_settings.png>
    
20. Add `launcher.sh` to crontab
    - Type `sudo crontab -e` in terminal and press enter (you may need to enter password)

      <img src=screenshots/crontab_term.png>

    - Add this line to the bottom of the file: `@reboot sh /home/davis_epi_raspi14/code/launcher.sh` (Note the # needed after `davis_epi_raspi` will vary depending on the username of the Pi)

      <img src=screenshots/crontab_edited.png>

21. Check that video works using `variable.py`
21. Reboot the Pi: type `reboot` in terminal and press enter
22. Make sure the video process is running
23. If it's working, you can proceed to 'in the field setup' instructions below

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

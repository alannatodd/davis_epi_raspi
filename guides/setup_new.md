# Raspberry Pi Setup (New Pi)
## Setup
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
        
      - Optional: Remove the zip file and davis_epi_raspi-main folder: `rm -rf davis_epi_raspi-main` and `rm davis_epi_raspi-main.zip`
        
        <img src=screenshots/rm_davis_folders.png>
        
18. Update variables `launcher.sh`, `continuous.py`, and `variable.py` to work with this specific Pi + username [Guide](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/code_customization.md)
19. Determine name of USB drive – check by typing `ls /media/<username>/` in terminal (ie `ls /media/davis_epi_raspi14`) It should be 'DUAL DRIVE' if using USBs from previous projects - if not see `rename_usb.md`

    <img src=screenshots/ls_usb.png>

20. Make sure Raspberry Pi config is correct
    - Select raspberry icon in menu bar -> Preferences -> Raspberry Pi Configuration
    
      <img src=screenshots/raspi_config_toggles.png>

      You can also change keyboard settings, password, and auto-login from here

      <img src=screenshots/raspi_config_keyboard.png>
      <img src=screenshots/raspi_config_settings.png>
    
21. Add `launcher.sh` to crontab
    - Type `sudo crontab -e` in terminal and press enter (you may need to enter password)

      <img src=screenshots/crontab_term.png>

    - Add this line to the bottom of the file: `@reboot sh /home/davis_epi_raspi14/code/launcher.sh` (Note the # needed after `davis_epi_raspi` will vary depending on the username of the Pi)

      <img src=screenshots/crontab_edited.png>

22. Check that video works using `variable.py`
21. Reboot the Pi: type `reboot` in terminal and press enter

    <img src="screenshots/reboot.png">

22. Make sure the video process is running. Reference steps 1-2 [here](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/find_and_kill_process.md)
24. If it's working, your Pi is ready - you can shut it off and proceed to 'In-Field Setup' instructions

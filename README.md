# Davis EPI Lab Raspberry Pi 
## Summary 
This repository contains the code and guidance to use Raspberry Pis for recording video. Using this setup, the Pis will continuously record videos of a given duration (default: 20 minutes) when turned on. When a USB is inserted into the Pi, the Pi will offload the videos that have been recorded since the Pi was started onto the USB. The USB can be removed, and the Pi will continue to record and store videos until the USB is reinserted and the new videos can be offloaded. 

## Details
1. The Pis are loaded with two important files that work together to run the video program: `launcher.sh` and `continuous.py`
2. The `crontab` file on the Pi is edited to run the `launcher.sh` script on reboot of the Pi. From the [Linux man page](https://man7.org/linux/man-pages/man5/crontab.5.html):
   > A crontab file contains instructions for the cron(8) daemon in the following simplified manner: "run this command at this time on this date".
   
   In addition to running at set times, there is also an option to run on reboot, which is what is used in this setup
   
4. The `launcher.sh` script launches the python process defined by `continuous.py`. This process records video and transfers it to the USB
5. If no USB is plugged in, `continuous.py` keeps a running list of the videos it has recorded during this run of the process that have not been transferred yet. Each time a video finishes, the program launches a thread to A) Check is a USB is plugged in and B) If so, transfer any videos to the USB that are in the not-yet-transferred list
6. The `continuous.py` process can be terminated in 2 ways: Turning off the Pi, or manually killing the process when connected to the Pi with a monitor/mouse/keyboard as defined in some of the Guides.

**Notes**
- When the Pi is turned off, the program running that records video will be un-gracefully shut down. This means that whatever video was in progress will not be properly saved or moved to the USB. It is recommended to only shut down the Pi at least 20 minutes past the required end of recording to ensure everything needed has been captured and transferred to the USB. You should also make sure that a USB has been plugged into the Pi for awhile before shutdown, so that all videos from that session had a chance to be transferred.
- If a USB is not plugged in before and up to when the Pi is shut down, the videos recorded during that time will not be automatically transferred to a USB during any following sessions. However, the videos can be moved manually by connecting a monitor/keyboard/mouse to the Pi.

## Guides
### Setup
### Syncing Time
### Adjusting Camera Focus + Video Size
### Changing Name of Pi User
### [Using LEDs for Time Information](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/setup_led.md)
### [Renaming USB](https://github.com/alannatodd/davis_epi_raspi/blob/main/guides/rename_usb.md)

## Expansion/Improvement Opportunities
### Hardware Clock 
Raspberry Pis do not have a hardware clock, and instead use a software clock. They rely on syncing to an internet time server to maintain accurate date + time. However, if a Pi cannot remain connected to the internet, it relies on its software clock to keep time. Software clocks experience more significant time drift than hardware clocks, so depending on length of time without internet connection and other factors like temperature, the Pi may become out of sync by second, minutes, or even hours. An improvement for situations where the Pi cannot remain connected to the internet would be purchasing, attaching, and configuring a Real Time Clock or RTC. 

**Further Reading**

Time Drift
- [Clock drift](https://en.wikipedia.org/wiki/Clock_drift)
- [Computer time drift](https://www.twingate.com/blog/glossary/ntp%20drift)

RTCs
- [Raspberry Pi Forum thread](https://forums.raspberrypi.com/viewtopic.php?t=255108)
- [Guide for setting up an RTC with a Pi](https://pimylifeup.com/raspberry-pi-rtc/)

### Buttons
Currently, shutting off the Raspberry Pis will not gracefully terminate the running program, cutting off the currently recording video somewhere in the middle and not saving them properly. A possible improvement would be to add a button that would send an interrupt to the program, triggering a gracefully termination where the in-progress video could be properly saved and transferred to the USB. This would be best used in conjunction with an LED which could indicate that the graceful termination was complete before the user manually shuts down the Pi. 

### Transferring Any Previously Recorded Videos 
It might be possible to make code changes that would cause the program to automatically transfer _any_ previously recorded videos onto the Pi when a USB is plugged in, instead of just ones from that session. Another consideration would be running a separate process at the same time as `continuous.py` that is responsible for transferring videos.

### Supporting Multiple USB Names 
Making code updates to `continuous.py` to search for multiple names of USBs. This would prevent needing to rename USBs to a single name, but would require user to update the `continuous.py` file to add new USBs to the list of possible names. 

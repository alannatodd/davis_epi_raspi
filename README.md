# Davis EPI Lab Raspberry Pi 
## Guides
### Setup
### Syncing Time
### Adjusting Camera Focus + Video Size
### Changing Name of Pi User
### Using LEDs for Time Information

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

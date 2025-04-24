# Syncing Time 
To get near-accurate timestamps on the videos while keeping the Pi disconnected from WiFi during the experiment, the time on the Pi **must** be synced to an internet time server before turning of the WiFi or Hotspot connection. 

Note: Turning the Pi off for more than a few seconds will cause it to fall deeply out of sync with the time it pulled from the internet. If you turn the Pi off for a period of time, you must re-sync it with the internet after turning it back on. 

See more discussion on time shift and potential hardware clock addition [here](https://github.com/alannatodd/davis_epi_raspi/blob/main/README.md#hardware-clock)

## Prereqs
- Pi setup, plugged in, and running in its final location for the experiment
- Proximity to a Wifi network, or a Hotspot-enabled smartphone

## Process
1. Connect Pi to monitor, keyboard, mouse and make sure its powered on.
2. For phone method, turn on your hotspot.
3. Click on the WiFi icon in the top corner of the Pi's desktop menu.
4. Select either the hotspot or the WiFi you wish to use. Enter password and connect.
5. For some types of WiFi (like eduroam guest), you will need to enter more information. Open a chromium browser and you should get redirected to the connection page where you will need to enter info or sign in.
6. Wait for the time on the Pi to sync up to the current time. The date and time are displayed in the top right corner in the menu bar. You may need to wait a few minutes for this to happen.
7. Once the date + time update, you can turn on the WiFi from the icon in the menu bar.

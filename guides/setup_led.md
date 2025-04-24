# Setup LED 
The `continuous.py` code includes support for connecting an LED that can provide information about the state of the process, so that errors can be detected while no monitor is connected. 

## Prereqs
General: 
- Electrical tape
  
For each Pi, you will need:
- An LED with a built in resistor. I used Octopus 5MM LED Brick OBLEDs, which can be found on DigiKey [here](https://www.digikey.com/en/products/detail/pi-supply/PIS-1280/10315756?s=N4IgTCBcDaIPIGEAqcAKBVAygAgKwFl9sAZAUQBFsAhAJQEkEBpbOKsygWmuJAF0BfIA)
- Extra M/F Breadboard Jumper wires - the connectors do not split on the wires that come with the above LED, so cannot be plugged into the right locations on the Pi alongside the fan (see photo below). [Here](https://www.digikey.com/en/products/detail/busboard-prototype-systems/KIT-ZW-20X3/19200354?s=N4IgTCBcDaIEYCcCmBDAJnA9ihaAEAVgK4C2ADkgngO4CWyAzniQPQBmIAugL5A) is a pack available on DigiKey that contains all 3 connection types (M/M, M/F, F/F), although you only need M/F. Packs can also be purchased on Amazon, etc.
  
  <img src=photos/led_no_split.png>

## Setup 
1. Remove the led + accompanying wires from packaging and insert wire group into connection point on LED.

   <img src=photos/led_insert.png>

2. For each wire, connect it to an extra jumper wire (recommend using matching color). Using electrical tape, tape the connection point to prevent it from separating.

   <img src=photos/led_wires_cxn.png>

3. Recommended: Put a couple layers of electrical tape on the bottom of the LED to cover the solder points

   <img src=photos/led_tape.png>

4. Connect the wires to the Pi. Red should go to pin 2 (5V), Black should go to pin 14 (Ground), and Yellow should go to pin 16 (GPIO 23). You will note in the `continuous.py` code that the `sensor_pin` variable is set to `23` - this refers to pin 16 which is `GPIO 23`

   <img src=screenshots/pinout_led.png>

   Here is a photo of the wires connected to the Pi alongside the fan connections:

   <img src=photos/led_pi_cxn.png>

## Use
You will need to make sure that `use_led` is set to `True` in `continuous.py` (See [Code Customization]() for more details). 
When the Pi is turned on and `continuous.py` starts, the LED will tell us that the process has started and print the current date and time, so we can make sure without connecting to a monitor that the time is correct. Note: You can turn off the date + time printing and just leave the "program started" indication (see code customization).
1. First the LED will turn on for 5 seconds. This indicates the program is starting.
2. The LED will then indicate the date + time as follows:
   - Blink the number of times to indicate the month: ie, blink 3 times for March, or 12 times for December. Then it will not blink for 3-4 seconds
   - Blink the tens place of the date. If its a zero, this will be indicated by 3 rapid blinks. ex: 3rd of May - 3 quick blinks. 11th - 1 longer blink. 21 - 2 longer blinks. Then pause for a few seconds.
   - Blink the ones place of the date. Again, if its a zero it will be indicated by 3 rapid blinks (ex: May 10th). Pause for 5 seconds.
   - Blink the current year (years past 2000) in the same way that date was printed (2 preceding items). (ex: 25). Then pause for 5 seconds.
   - Blink the current hour - this works the same way as the date and year. Note it will be in military time (24 hour clock). Pause for 5 seconds.
   - Blink the current minute - this works the same as date, year, and hour.
   - If an error occurs anywhere here, the LED will blink rapidly 20 times, then repeat the following 3 times to indicate an error printing the date + time: Blink once, then turn off for 4 seconds
3. After datetime is printed, video recording will commence.
4. If any error happens during video recording, the LED will indicate the error (see Guide below)

## Error Guide 
If an error occurs while the program is running, the following will happen: 
1. LED turns on for 10 seconds to indicate an error, then turns off.
2. LED will print the error code for the specific _type_ of error (see table below). The LED will blink the # of times indicating the type, then turn off for 4 seconds. This will repeat 2 more times.
3. For some types of errors that can only occur in the beginning of the process (1-4), this will only happen once and then the process will be killed. These need to be fixed before the Pi can be used.
4. Some errors do not indicate a catastrophic failure - Copying Files and Loggin Errors to Files. The error will be indicated by the LED turning on for 10 seconds, then blinking the error code followed by a pause 3 times. The process will then continue to record video and attempt to move it to the USB.
5. For errors with recording or with the python thread itself, the process will continue trying to run until the error is hit more than 10 times. At that point, no more recording will take place, and the LED will indicate an error by doing the following repeatedly: Turn on LED for 1 minute, then print error code indicating recording error, thread error, or both.
   
Note that to avoid disruption during nighttime hours to any animals being observed, the LED will not turn on to display recording or thread errors between 6 PM and 7 AM. This can be adjusted in `continuous.py` if desired. 

### Error Codes 
| Error Type | # Blinks |
| --- | --- |
| Date + Time | 1 |
| File Setup | 2 |
| Camera Setup | 3 |
| Recording | 4 |
| Python Thread | 5 | 
| Copying Files | 6 |
| Logging Errors to File | 7 |

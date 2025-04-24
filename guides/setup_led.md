# Setup LED 
The `continuous.py` code includes support for connecting an LED that can provide information about the state of the process, so that errors can be detected while no monitor is connected. 

## Prereqs
For each Pi, you will need:
- An LED with a built in resistor. I used Octopus 5MM LED Brick OBLEDs, which can be found on DigiKey [here](https://www.digikey.com/en/products/detail/pi-supply/PIS-1280/10315756?s=N4IgTCBcDaIPIGEAqcAKBVAygAgKwFl9sAZAUQBFsAhAJQEkEBpbOKsygWmuJAF0BfIA)
- Extra M/F Breadboard Jumper wires - the connectors do not split on the wires that come with the above LED, so cannot be plugged into the right locations on the Pi alongside the fan (see photo below). [Here](https://www.digikey.com/en/products/detail/busboard-prototype-systems/KIT-ZW-20X3/19200354?s=N4IgTCBcDaIEYCcCmBDAJnA9ihaAEAVgK4C2ADkgngO4CWyAzniQPQBmIAugL5A) is a pack available on DigiKey that contains all 3 connection types (M/M, M/F, F/F), although you only need M/F. Packs can also be purchased on Amazon, etc.
  
  <img src=photos/led_no_split>
  
- Electrical tape

## Setup 
1. Remove the led + accompanying wires from packaging and insert wire group into connection point on LED.

   <img src=photos/led_insert.png>

2. For each wire, connect it to an extra jumper wire (recommend using matching color). Using electrical tape, tape the connection point to prevent it from separating.

   <img src=photos/led_wire_cxn.png>

3. Recommended: Put a couple layers of electrical tape on the bottom of the LED to cover the solder points

   <img src=photos/led_tape.png>

4. Connect the wires to the Pi. Red should go to pin 2 (5V), Black should go to pin 14 (Ground), and Yellow should go to pin 16 (GPIO 23). You will note in the code that the `sensor_pin` variable is set to `23` - this refers to pin 16 which is `GPIO 23`

   <img src=screenshots/pinout_led.png>
   <img src=photos/led_pi_cxn.png>

## Error Guide 

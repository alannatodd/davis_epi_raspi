# Renaming a USB 
The code is configured to use a USB called `DUAL DRIVE`. If you wish to use a different type of USB, you have two options: 
1. Adjust the code on the Pi to use the name of the new type of USB
2. Rename the USB to be `DUAL DRIVE`, which will be covered in this guide

## Rename Process using mlabel
**Note**: This may not work on its own for all USBs - in which case, you will need to do the **Rename process using gparted** below this
Using a Raspberry Pi:
1. Plug in the USB you want to rename
2. Open terminal

   <img src=screenshots/terminal.png>

3. Download a package
   - Connect the Pi to the internet to download the package
   - In terminal, type `sudo apt-get install mtools`, press enter
   - You will be prompted to enter the password for `sudo`. Type password and hit enter (note: it will not look like you have typed anything for the password, but it's there)
   - Optional: can disconnect Pi from WiFi at this point
4. Figure out where the USB is mounted to the Pi. In the terminal, type `mount | grep media`. This should return the USB location and some info, something like:
   ```
   /dev/sda1 on /media/davis_epi_raspi14/A4DS-GB34 type vfat (rw,nosuid,nodev,relatime,uid=1000,gid=1000,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,showexec,utf8,flush,errors=remount-ro,uhelper=udisks2)
   ```

   You want this first thing - in this case it was `/dev/sda1` - which it probably will be in most cases

5. In terminal, type `sudo mlabel -i /dev/sda1 ::DUAL\ DRIVE`
6. Eject the USB - click the folders icon in the menu bar and scroll to the top - on the left hand side you should either see DUAL DRIVE or the original name of the USB - click the eject ⏏️ icon next to it
7. Physically remove the USB from the Pi, then plug it back in
8. Make sure the rename worked. In terminal, type `cd /media` and press enter
9. Then type `cd /da` (then press tab to autocomplete the name of the Pi - something like `davis_epi_raspi12`)
10. Then type `ls` (note this is a lowercase L, not an I)
11. If the rename worked, it should say 'DUAL DRIVE'
12. Again eject and remove USB 

## Rename Process Using gparted
If using a new pi, will need to install gparted, otherwise if using same Pi as before can skip step 1
1. Open terminal and type `sudo apt install gparted` and press enter.

2. You may be prompted to enter the password for `sudo`. Type password and hit enter (note: it will not look like you have typed anything for the password, but it's there)
3. Plug in the USB you want to rename to the Pi
4. Open gparted - from top menu click raspberry icon, then system tools, then gparted. Enter same password you use elsewhere (sudo, login)
5. In gparted, there should be a drop down towards the top right- select `/dev/sda` from the drop down and you should see the USB listed 
6. Go back to terminal and unmount USB. Type `sudo umount /media/` (then press tab to autocomplete - should be usb path). You might also be able to unmount the USB in gparted if you right click on the listed USB - might be an unmount option 
7. In gparted, right click on USB and select format -> fat32
8. Select accept / apply on any warnings. It should now say 1 pending operation at the bottom. 
9. In gparted go to edit in top menu -> apply operations
10. Accept any warnings and let it reformat the USB
11. When done reformatting, unplug the USB from the Pi and close gparted, then plug back in 
12. Follow steps 5-12 from the `mlabel` instructions above

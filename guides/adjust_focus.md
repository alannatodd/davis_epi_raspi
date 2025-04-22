1. Open the terminal
   <img src="screenshots/terminal.png">
2. If there is a `continuous.py` process running, we need to stop it. Find the process ID (PID) by typing:
   ```
   ps aux | grep continuous.py
   ```
   and then hitting enter.
   
   If it is running, you will see it listed like so:
   ```
   root   485 0.0  0.1  12168 ?    S   17:53  0:00 sudo python3 continuous.py 
   ```
   Note how it says "sudo python3 continuous.py" and there is a process ID, or "pid" listed - 485 in this case
4. If there is a running continuous.py process, kill it. We can only have one process running at a time that uses the camera. Use the PID from step 2. 
   ```
   sudo kill <pid>
   ```
   ex:
   ```
   sudo kill 485
   ```
   You may then be prompted to enter the sudo password, which you must do to kill the process.

   After, you can run the same command from 2 to make sure the process is no longer listed.

   Real Example:
   <img src="screenshots/stop_process.png">
   
5. From the terminal run `libcamera` to see a preview window to determine what lens position to use. This will likely be in a range between 0.1 and 10. You can also determine what image dimensions to use, such as 360 x 360 or 360 x 480.
   - For a high mounted camera, try:
   ```
   libcamera-vid --height 360 --width 360 --timeout 100000 --lens-position 0.5
   ```
   
   - For a lower, wide angle setup try:
   ```
   libcamera-vid --height 360 --width 480 --timeout 100000 --lens-position 0.5
   ```

   Real Example (0.5 lens position)
   <img src="screenshots/libcamera_05.png">

   Real Example (0.1 lens position)
   <img src="screenshots/libcamera_01.png">

   Running libcamera-vid will open a window with the video output resulting from running the camera with the inputted settings. The video will close itself after an amount of time determined by the `timeout` value set, or you can close the window manually with the x or stop the process from the terminal using ctrl-c.
   Example window:
   <img src="screenshots/libcamera_05_window.png">
   
7. After you select a lens position, you can additionally test it out using `variable.py` if desired
   - Go to Folders -> `code` -> Right click on `variable.py` and select Geany or Thonny (you can also use text editor but Thonny & Geany have line numbers + python color hints)
   - Around line 25 there should be setup for the focus. This might be set to Autofocus or already changed to Manual. It might look like:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
     ```
     Update it to look like this with your desired lens position:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5})
     ```
8. Click save at the top of the editor
   <img src="screenshots/geany_save.png">
9. In the terminal, move to the code directory by running
   ```
   cd code
   ```
10. Run the `variable.py` program to make a quick video, type
   ```
   python3 variable.py 1
   ```
11. After around 5 seconds, the video will be complete and be saved in the code/goats folder. It will be prefixed with the date like `2025_etc_etc..`
12. Update continuous.py to user your selected lens position
    - Go to Folders -> `code` -> Right click on `continuous.py` and select Geany or Thonny (you can also use text editor but Thonny & Geany have line numbers + python color hints)
    - Around line 258 there should be setup for the focus. This might be set to Autofocus or already changed to Manual. It might look like:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
     ```
     Update it to look like this with your desired lens position:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5})
     ```
13. Click save at the top of the editor
    <img src="screenshots/geany_save.png">
14. Restart the pi so that continuous.py will start running again with the new focus and lens position settings. In the terminal, type `reboot` and press enter
    <img src="screenshots/reboot.png">

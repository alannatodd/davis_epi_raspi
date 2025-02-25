1. Open the terminal
2. If there is a continuous.py process running, we need to stop it. Find the process ID (PID) by typing:
   ```
   ps aux | grep continuous.py
   ```
   If it is running, you will see it listed like so:
   ```
   ```
3. If there is a running continuous.py process, kill it. We can only have one process running at a time that uses the camera. Use the PID from step 2. 
   ```
   sudo kill <pid>
   ```
   ex:
   ```
   sudo kill 460
   ```
   You may then be prompted for a password 
4. From the terminal run `libcamera` to see a preview window to determine what lens position to use. This will likely be in a range between 0.1 and 10.
   - For a high mounted camera, run:
   ```
   libcamera-vid --height 360 --width 360 --timeout 100000 --lens-position 0.5
   ```
   - For a lower, wide angle setup run:
   ```
   libcamera-vid --height 360 --width 480 --timeout 100000 --lens-position 0.5
   ```
5. After you select a lens position, you can additionally test it out using `variable.py` if desired
   - Go to Folders -> `code` -> Right click on `variable.py` and select Geany or Thonny (you can also use text editor but Thonny & Geany have line numbers + python color hints)
   - Around line 25 there should be setup for the focus. This might be set to Autofocus or already changed to Manual. It might look like:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
     ```
     Update it to look like this with your desired lens position:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5})
     ```
6. Click save at the top of the editor
7. In the terminal, move to the code directory by running
   ```
   cd code
   ```
8. Run the `variable.py` program to make a quick video, type
   ```
   python3 variable.py 1
   ```
9. After around 5 seconds, the cideo will be complete and be saved in the code/goats folder. It will be prefixed with the date like `2025_etc_etc..`
10. Update continuous.py to user your selected lens position
    - Go to Folders -> `code` -> Right click on `continuous.py` and select Geany or Thonny (you can also use text editor but Thonny & Geany have line numbers + python color hints)
    - Around line 258 there should be setup for the focus. This might be set to Autofocus or already changed to Manual. It might look like:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
     ```
     Update it to look like this with your desired lens position:
     ```
     camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5})
     ```
12. Click save at the top of the editor
13. Restart the pi so that continuous.py will start running again with the new focus and lens position settings. In the terminal, type `reboot` and press enter

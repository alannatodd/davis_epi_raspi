If you want to rename the existing main user. In this example we are changing the name of the user from `fishpi13` to `davis_epi_raspi13`

1. Open terminal
2. Create a temporary user
   ```
   $ sudo adduser temppi
   ```
   Note: You may be prompted to put in your password here
   Note: You can put 'temppi' for the name and press enter to leave everything else blank
   Note: You will not be able to see the password that you type (it will seem like you haven't typed anything)
4. Assign the user to the `sudo` group so it has permission to manipulate other users
   ```
   $ sudo usermod -aG sudo temppi
   ```
5. Make sure auto-login is disabled in the raspi config
   - This is also a good opportunity to change the password of the main user if desired
6. Reboot the pi. This can either be done from the menu or by typing `reboot` in the terminal and hitting enter
7. When the pi reboots, log in to the temporary user 
8. Open the terminal
9. Rename the main user
   ```
   $ sudo usermod -l new_username -m -d /home/new_username old_username
   ```
   ex:
   ```
   $ sudo usermod -l davis_epi_raspi13 -m -d /home/davis_epi_raspi13 fishpi13
   ```
10. Update references to the old username
   ```
   sudo grep -rl 'fishpi13' /etc /home/davis_epi_raspi13
   ```
11. Reboot
12. Log in to new user (in example davis_epi_raspi13)
13. Open terminal
14. Delete temporary user
    ```
    sudo deluser --remove-home temppi
    ```
15. IN raspi config, re-enable auto-login
16. Update the cron file to point to the new user
    ```
    sudo crontab -e
    ```
    Edit the line at the bottom that mentions `launcher.sh` to use the new username instead of the old one
17. Save crontab `esc` , `:wq`, `Enter`
    

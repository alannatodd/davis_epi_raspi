# Customizing the Code on the Pi
All files can be edited in a number of ways on the Pi: 
- Opening the file from the folder GUI in a code editor like `Thonny` or `Geany`
- From the terminal using a text editor like [`vim`](https://www.vim.org/) or [`emacs`](https://www.gnu.org/software/emacs/) (Not recommended for those who have not used them before)

In these guides I will focus on editing using a code editor based on the intended audience and the helpful features of code editors such as line numbers and type hints.

## Required Per Pi 
Prereqs: 
1. Determine the username of the Pi + main user you are working in. It should be something like `davis_epi_raspi14` (number will vary).
2. Determine the name of the USB. You may wish to change the name(s) of the USB(s) to 'DUAL DRIVE' instead of changing the code.

### How to open a file in Geany/Thony
1. Open the documents GUI from the Desktop (if present) or menu bar

   <img src=screenshots/docs_folder.png>

2. Navigate to the `code` folder

   <img src=screenshots/code_folder.png>

3. Right click on the file you want to edit and select `Geany` or `Thonny`
4. The code editor will open with the selected file

### Update `continuous.py` 
Open the file in a code editor. You will need to update a few variables in the copy of the `continuous.py` _on the Pi_: 
- `pi_username`: must be set to the username on the Pi you are currently working on. If you open a terminal window this username will be shown in the line prefix.
- `subdir`: only if using different directory under `/code` than what is set
- `usb_name`: only if USB is not named this
  
You can look at these variables in this repo [here](https://github.com/alannatodd/davis_epi_raspi/blob/02ea7123ba0473a3676f347ce3bb9aa87a5150d7/continuous_led.py#L17) but they need to be edited in the file on the Pi itself.

Example of how this will look in Geany: 

<img src=screenshots/geany_vars.png>

Make any needed edits and then save the file.

### Update `launcher.sh` 
Open the file in a code editor. Here you only need to change a single item - the path after `cd` - it should (like in `continuous.py`) be updated with the username for the Pi you are currently working on. Update it, then save the file.

<img src=screenshots/geany_launcher.png>

## Optional 

### Turning off the LED integration
If you don't have an LED connected to the Pi, or do not wish to enable the LED functions, you can disable it here by setting the value to `False`:

<img src=screenshots/geany_led.png>

### Adjusting Camera Settings
The video duration, video dimensions, and focus settings can be adjusted here: 

<img src=screenshots/geany_video_settings.png>

See [Adjusting Focus Guide]() for more information 

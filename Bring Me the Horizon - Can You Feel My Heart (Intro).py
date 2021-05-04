##This python script repeatedly plays the intro of Bring Me the Horizon - Can 
##You Feel My Heart using the Windsong Lyre in Genshin Impact. Note the use of a 
##"while True:" loop; you'll need to terminate the script manually and a bit 
##harshly. Before running this script, make sure that you're Running as 
##Administrator, whether you're using the Command Prompt, Windows Powershell, 
##IDLE, or whatever you may be using.

import time
from pynput.keyboard import Controller

time.sleep(5) # Allow the user 5 seconds to switch to Genshin Impact and take out the Windsong Lyre

# Create a Controller object
keyboard = Controller()

# Press keys
while True:
    for measure in range(3):
        keyboard.type('j')
        time.sleep(60/128/4*4)
        keyboard.type('j')
        time.sleep(60/128/4*4)
        keyboard.type('j')
        time.sleep(60/128/4*3)
        keyboard.type('w')
        time.sleep(60/128/4*3)
        keyboard.type('q')
        time.sleep(60/128/4*2)
    keyboard.type('j')
    time.sleep(60/128/4*2)
    keyboard.type('j')
    time.sleep(60/128/4*2)
    keyboard.type('d')
    time.sleep(60/128/4*2)
    keyboard.type('j')
    time.sleep(60/128/4*2)
    keyboard.type('j')
    time.sleep(60/128/4*1)
    keyboard.type('d')
    time.sleep(60/128/4*1)
    keyboard.type('d')
    time.sleep(60/128/4*1)
    keyboard.type('d')
    time.sleep(60/128/4*1)
    keyboard.type('j')
    time.sleep(60/128/4*4)

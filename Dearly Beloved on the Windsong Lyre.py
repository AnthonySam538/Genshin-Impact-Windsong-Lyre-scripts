##This python script plays Dearly Beloved using the Windsong Lyre in Genshin 
##Impact. Note the use of a "while True:" loop; you'll need to terminate the 
##script manually and a bit harshly. Before running this script, make sure that 
##you're Running as Administrator, whether you're using the Command Prompt, 
##Windows Powershell, IDLE, or whatever you may be using.

import time
from pynput.keyboard import Controller

time.sleep(5) # Allow the user 5 seconds to switch to Genshin Impact and take out the Windsong Lyre

# Create a Controller object
keyboard = Controller()

# Press keys
while True:
    keyboard.type('w')
    time.sleep(1)
    keyboard.type('h')
    time.sleep(1)
    keyboard.type('g')
    time.sleep(1)
    keyboard.type('e')
    time.sleep(1)
    keyboard.type('w')
    time.sleep(1)
    keyboard.type('h')
    time.sleep(1)
    keyboard.type('g')
    time.sleep(1)
    keyboard.type('e')
    time.sleep(1)
    keyboard.type('r')
    time.sleep(1)
    keyboard.type('e')
    time.sleep(1)
    keyboard.type('y')
    time.sleep(1)
    keyboard.type('t')
    time.sleep(1)
    keyboard.type('r')
    time.sleep(1)
    keyboard.type('e')
    time.sleep(1)
    keyboard.type('w')
    time.sleep(1)
    keyboard.type('q')
    time.sleep(1)

import pyautogui as pag
from time import sleep

# Forza 5 XP Bot
# (C) 2022 William Starrs. Licensed under GPLv3.

# Variables you can change if you want: _______________________________________________________________________________________
# Make sure to change the numbers, not the names.
restart_delay = 10      # Adjust this based on how long your game takes to load after hitting restart
race_start_delay = 10   # Delay after hitting "Start Race Event"
anti_skrrrt = 20        # Times to pump acceleration to make sure you drive sober (set this to zero and you'll see what I mean)
full_throttle = 35      # Amount of time to full throttle
# _____________________________________________________________________________________________________________________________

print("Welcome to the land of infinite experience in Forza 5.")
sleep(0.5)
print("(C) 2022 William Starrs. Licensed under GPLv3 so anyone can make this better and be forced to share it.")
sleep(0.5)
print("First, you need to go to the difficulty settings and make sure you have assisted braking, steering, traction, stability, and shifting enabled.")
sleep(0.5)
print("Next, enter Creative Hub > Eventlab > Event Blueprints and search with share code 743 324 179. Choose solo and then your fastest car.")
sleep(0.5)
input("Finally, make sure you're on the start race event screen. Once you're there, press enter in this terminal.")
print(f"You have {restart_delay} seconds to open your Forza window. Make sure START RACE EVENT is highlighted. Have fun! :-D")

# You can ignore all the def stuff, it just makes the while True part easier to read.
def hold(key, time): # Holds key for certain amount of time
    pag.keyDown(key)
    print(key + " down")
    sleep(time)
    pag.keyUp(key)
    print(f"{key} up after {time} secs")

def tap(key): # Presses a key once
    pag.press(key)
    print(key + " pressed")

# This is the fun part.
while True:
    sleep(restart_delay)
    tap('enter')
    sleep(race_start_delay)
    for i in range(anti_skrrrt):
        hold('w', 0.1)
    hold('w', full_throttle)
    sleep(5)
    tap('x')
    sleep(0.5)
    tap('enter')
    sleep(0.5)
    tap('enter') # Just in case it asks you to like the course.

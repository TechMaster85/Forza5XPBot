# Forza XP Bot
## How this works:
- In Forza 5 (PC only, sorry Xbox players), open a specific custom map that will give you experience.
- Change your settings so that your car will steer automatically.
- Once you're on the start screen, run this bot.
- It will repeatedly drive for you and repeatedly play the map again.
- Feel free to adjust the script to your needs.

## How to run
- Run the included .exe file (output\main.exe) for default settings. To customize your settings, here's how to edit the script:

## How to edit the script:
- Install Python 3.10 via the [Microsoft Store](https://www.microsoft.com/store/productId/9PJPW5LDXLZ5). This is the most convenient way to install Python.
- It's easiest to change the variables at the top depending on how fast your computer is and your car is.
- Open a command prompt, go to this directory, and run `venv\Scripts\activate.bat`.
- If you did it correctly, you should see a (venv) at the start of the prompt.
- Run `python main.py`.
- To create an exe file for convenience (so your or someone else won't have to install Python), here's how:

## How to create a custom exe file:
- Make sure you're in a (venv) by following the first three instructions under "How to edit the script".
- Run `pyinstaller --noconfirm --onefile --console main.py`.

## What about Smartscreen?
- Hit More Info > Run Anyway.
- If you really don't trust me, run the script directly (after entering a venv) or build an exe yourself.

## How you can help:
- Find another xp grinding custom map and program for that. Make a pull request, I'll try it out, and if it's good, I'll use your modified script.
- Aim for the greatest efficiency. That's xp gained divided by amount of time. It would be nice if you can include this number in your pull request.

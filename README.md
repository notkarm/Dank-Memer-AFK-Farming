# Dank-Memer-AFK-Farming
A simple script to AFK Farm Dank Memer coins (Discord)


███████████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀██▀▄─██▄─▀█▄─▄█▄─█─▄███▄─▀█▀─▄█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀████▀▄─██▄─▄▄─█▄─█─▄█
██─██─██─▀─███─█▄▀─███─▄▀█████─█▄█─███─▄█▀██─█▄█─███─▄█▀██─▄─▄████─▀─███─▄████─▄▀██
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀
███████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄▄▀█▄─▄█▄─▄▄─█─▄─▄─█
█▄▄▄▄─█─███▀██─▄─▄██─███─▄▄▄███─███
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀

-----------------------------------------------------------------------------------------------------------

This readme file is for the dank memer script that I created using the pynput keyboard API. (Keep in mind you have to keep your discord in focus when you are running the script since it works by registering keystrokes)

Please follow the instructions for making sure this script works for you:
1) Make sure python is installed on your computer (Follow this site for doing so: https://www.python.org/downloads/)
2) Open command prompt and type "pip install pynput"
3) Type "pip install key" followed by that
4) Download the dankmemerscript.py and simply double click on it. If it does not work, open cmd, and go to the directory where the file is saved, and type "python3 dankmemerscript.py"
5) Congratulations! Your script should be running and now all you have to do is open discord and join a channel that does not ban you for spamming, and let the script do it's thing!
6) To stop the script, alt tab to the command promt and press ctrl+c or just stop the execution in whatever IDE you use for python.

Advanced commands for earning more through it:

In order to use these commands, you must install the mouse API using "pip install mouse" and also understand how position coordinates work. Since the commands, pls search, pls postmeme, and pls search require the user to 
use a mouse click, you must get the coordinates of the rightmost or leftmost option in these commands and then enter those coordinates in the 'x' and 'y' spaces in the commands provided below so that it can pick one of the 
three options given by the dankmemer bot.

    keyboard.type("pls search")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    mouse.move('x', 'y', absolute=True, duration = 0)
    mouse.click('left')

    time.sleep(5)

    keyboard.type('pls postmeme')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    mouse.move('x', 'y', absolute=True, duration = 0)
    mouse.click('left')

    time.sleep(5)

    keyboard.type('pls sell')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    mouse.move('x', 'y', absolute=True, duration = 0)
    mouse.click('left')

    time.sleep(5)

-----------------------------------------------------------------------------------------------------

█████████████████████████████████████████████████████
█─▄─▄─█─█─██▀▄─██▄─▀█▄─▄█▄─█─▄███▄─█─▄█─▄▄─█▄─██─▄█░█
███─███─▄─██─▀─███─█▄▀─███─▄▀█████▄─▄██─██─██─██─██▄█
▀▀▄▄▄▀▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▀

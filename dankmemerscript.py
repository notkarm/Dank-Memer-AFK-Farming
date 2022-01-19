from pynput.keyboard import Key, Controller
import time
import mouse

# Cooldown times:
# pls hunt 40s
# pls fish 40s
# pls dig 40s
# pls beg 45s

keyboard = Controller()
i = 0

time.sleep(2)
while i<1:
    keyboard.type("pls beg")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.type("pls dig")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.type("pls hunt")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.type("pls fish")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.type("pls dep all")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

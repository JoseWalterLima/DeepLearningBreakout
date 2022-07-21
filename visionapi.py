from PIL import ImageGrab
import pyautogui
import time

x, y = pyautogui.size()
left = x/2 - 470
top = y/2 - 370
right = x/2 + 470
bottom = y/2 + 370
ss_region = (left, top, right, bottom)
time.sleep(5)
ss_img = ImageGrab.grab(ss_region).convert("L").resize((200,200))
ss_img.save(str(time.time()) + '.png')
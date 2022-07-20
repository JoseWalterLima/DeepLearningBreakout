from PIL import ImageGrab
import pyautogui
import time

x, y = pyautogui.size()
left = x/2 - 470
top = y/2 - 370
right = x/2 + 470
bottom = y/2 + 370
ss_region = (left, top, right, bottom)
ss_img = ImageGrab.grab(ss_region).convert("L")
ss_img.save(str(time.time()) + '.png')
time.sleep(4)

# def get_images(screen):
#     time.sleep(0.5)
#     pygame.image.save(screen, str(time.time()) + '.jpeg')
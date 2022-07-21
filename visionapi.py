from PIL import ImageGrab
import pyautogui
import time
import torch
import torchvision.transforms as transforms

x, y = pyautogui.size()
left = x/2 - 500
top = y/2 - 370
right = x/2 + 470
bottom = y/2 + 370
ss_region = (left, top, right, bottom)
t1 = time.time()
ss_img = ImageGrab.grab(ss_region).convert("L").resize((200,200))

# Transform image to pytorch tensor
transform = transforms.Compose([transforms.PILToTensor()])
ss_img = transform(ss_img)
t2 = time.time()
print(type(ss_img))
print('Total Time: {}'.format((t2 - t1)))
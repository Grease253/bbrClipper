import pydirectinput
import cv2 as cv
import time

while True:  
  if pydirectinput.locateOnScreen('C:/Users/Testbench/Documents/newbbrPoints.png', confidence=0.01):
    print('Training image found on screen!')
  time.sleep(5)  
  pydirectinput.hotkey('`')
  print('Hotkey triggered!')
  if input() == '.': 
    break
  continue
# enjoy BBR fans !
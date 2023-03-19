import pyautogui
import cv2 as cv
import time

while True:  
  if pyautogui.locateOnScreen('C:/Users/Testbench/Documents/newbbrPoints.png', confidence=0.01):
    print('Training image found on screen!')
  time.sleep(5)  
  pyautogui.hotkey('`')
  print('Hotkey triggered!')
  if input() == '.': 
    break
  continue
# enjoy BBR fans !
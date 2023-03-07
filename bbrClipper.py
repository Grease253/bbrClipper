import pyautogui
import cv2 as cv
import time

while True:  
  pyautogui.locateOnScreen('C:\Users\Testbench\Documents\bbrPoints.png', confidence=0.5)
  time.sleep(15)  
  pyautogui.hotkey('`')
  if input() == '.': 
    break
  continue
# enjoy BBR fans ! 
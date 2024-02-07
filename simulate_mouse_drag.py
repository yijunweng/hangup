import pyautogui
import time
from get_absolute_position import get_absolute_position

# 模拟上拉动作

def simulate_mouse_drag(start, end): 
    pyautogui.moveTo(get_absolute_position(start[0], start[1]))
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.moveTo(get_absolute_position(end[0], end[1]))
    pyautogui.mouseUp()
    time.sleep(1) # sleep 1秒等待回弹归位
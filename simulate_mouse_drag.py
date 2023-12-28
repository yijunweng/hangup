import pyautogui
import time
from get_absolute_position import get_absolute_position

# 模拟上拉动作

def simulate_mouse_drag(): 
    pyautogui.moveTo(get_absolute_position(46, 65))
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.moveTo(get_absolute_position(46, 30))
    pyautogui.mouseUp()
    time.sleep(1) # sleep 1秒等待回弹归位

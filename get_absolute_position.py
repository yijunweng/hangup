import pyautogui
import pygetwindow as gw

# 计算并返回鼠标相对窗口位置百分比
def get_absolute_position(percentage_x, percentage_y):
    window = gw.getWindowsWithTitle('wow')[0]
    window_x, window_y = window.left, window.top
    window_width, window_height = window.width, window.height
    absolute_x = window_x + (percentage_x / 100) * window_width
    absolute_y = window_y + (percentage_y / 100) * window_height
    return absolute_x, absolute_y
import pyautogui
import pygetwindow as gw

# 实时计算鼠标相对于窗口的百分比位置
def get_relative_window_position():
    window = gw.getWindowsWithTitle('wow')[0]
    window_x, window_y = window.left, window.top
    window_width, window_height = window.width, window.height

    mouse_x, mouse_y = pyautogui.position()
    relative_x = mouse_x - window_x
    relative_y = mouse_y - window_y
    percentage_x = (relative_x / window_width) * 100
    percentage_y = (relative_y / window_height) * 100
    return percentage_x,percentage_y

while True:
    print(get_relative_window_position())
    
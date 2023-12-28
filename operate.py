import pyautogui
import time
from simulate_mouse_drag import simulate_mouse_drag
from get_absolute_position import get_absolute_position
from dxc import dbdl, xkly

# 界面操作类

# 重置界面
def reset():
    # 触发多次click确保没有浮层
    pyautogui.moveTo(get_absolute_position(2.5, 4), duration = 0.1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

# 模拟点击
def imitate_click(p_x, p_y):
    pyautogui.moveTo(get_absolute_position(p_x, p_y), duration = 0.1)
    pyautogui.click()
    # 暂停0.5秒防误触
    time.sleep(0.5)

# 打开地下城列表
def openList():
    imitate_click(10.5, 18)
    imitate_click(23.5, 28)

# 进入地下城
def enter():
    imitate_click(46, 82.5)

# 清空背包
def clearBag():
    imitate_click(31, 95)
    imitate_click(55.5, 87)
    imitate_click(66, 80)
    imitate_click(46, 80)
    imitate_click(66, 80)
    print('背包已清空')
    reset()

# 开启脚本
def start(targets, seconds):
    time.sleep(2) # sleep 2秒等待控制权释放

    for index, item in enumerate(targets):
        reset()
        openList()
        print(f'当前大陆：{ item["region_name"] }, 当前地下城：{ item["dxc_name"] }, 进度{ index }/{ len(targets) }')
        # 选择大陆
        imitate_click(item["regionPosition"][0], item["regionPosition"][1])
        if item["index"] > 10: simulate_mouse_drag()  # 10以后的副本要执行拖动事件
        # 选择副本
        imitate_click(item["dxcPosition"][0], item["dxcPosition"][1])
        enter()
        time.sleep(seconds)
        print(f'当前大陆：{ item["region_name"] }, 地下城{ item["dxc_name"] }已完成, 进度{ index + 1 }/{len(targets)}')
        clearBag()

    

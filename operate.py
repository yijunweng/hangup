import pyautogui
import time
from simulate_mouse_drag import simulate_mouse_drag
from get_absolute_position import get_absolute_position
from constant import ad_posistions

# 界面操作类

# 重置界面
def reset():
    # 触发多次click确保没有浮层
    pyautogui.moveTo(get_absolute_position(2, 4), duration = 0.1)
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
    imitate_click(7.5, 18)
    imitate_click(22, 28)

# 进入地下城
def enter_dxc():
    imitate_click(47, 82)

# 清空背包
def clearBag():
    imitate_click(30, 95)
    imitate_click(58, 87)
    imitate_click(71, 80)
    imitate_click(47, 80)
    imitate_click(70, 80)
    print('背包已清空')
    reset()

# 进入商店(广告)
def enter_store():
    imitate_click(85, 95)
    imitate_click(16, 60)
    imitate_click(33, 76)

# 播放广告
def play_ad():
    imitate_click(47, 63)

# 切换角色
def changeRole(roleTarget):
    imitate_click(87, 10)   #设置
    imitate_click(46, 77)   #切换角色
    imitate_click(roleTarget[0], roleTarget[1])
    imitate_click(47, 53)   #进入游戏

# 重启游戏
def reLuanch():
    imitate_click(30, 2) #退出
    time.sleep(2)
    imitate_click(35.5, 2) #打开进程
    time.sleep(2)
    imitate_click(83, 8) #清除
    time.sleep(2)
    imitate_click(75, 23) #打开游戏
    time.sleep(10)
    imitate_click(75, 23) #点击进入游戏，坐标随机
    time.sleep(5)
    imitate_click(48, 53) #进入游戏
    time.sleep(5)

# 自动地下城
def start(targets, seconds, roles):
    time.sleep(2) # sleep 2秒等待控制权释放
    imitate_click(50, 95)

    for role in roles:
       print(role["target"])
       changeRole(role["target"])
       time.sleep(10)
       for index, item in enumerate(targets):
           reset()
           openList()
           print(f'当前大陆：{ item["region_name"] }, 当前地下城：{ item["dxc_name"] }, 进度{ index }/{ len(targets) }')
           # 选择大陆
           imitate_click(item["regionPosition"][0], item["regionPosition"][1])
           if item["index"] > 10: simulate_mouse_drag([47, 65], [47, 35])  # 10以后的副本要执行拖动事件
           # 选择副本
           imitate_click(item["dxcPosition"][0], item["dxcPosition"][1])
           enter_dxc()
           time.sleep(seconds)
           print(f'当前大陆：{ item["region_name"] }, 地下城{ item["dxc_name"] }已完成, 进度{ index + 1 }/{len(targets)}')
           clearBag()
    


# 自动广告
def start_ad(arr): 
    time.sleep(2) # sleep 2秒等待控制权释放
    imitate_click(85, 95)

    for index, item in enumerate(arr):
        for _ in range(item): 
            reset()
            enter_store()
            imitate_click(ad_posistions[index][0], ad_posistions[index][1]) # 点击对应位置的道具
            play_ad() # 开始播放广告
            # for i in range(1, 20):
            #     simulate_mouse_drag([92.5, 85], [92.5, 20])
            #     time.sleep(2)
            time.sleep(90) # 广告兼容时长为90秒
            reLuanch()
            time.sleep(180) # 广告cd三分钟
    print("广告自动播放已完成！")
 


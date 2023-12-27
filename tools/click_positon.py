import pyautogui

def click_positon():
    while True:
        click_x, click_y = pyautogui.position()
        color = pyautogui.pixel(click_x, click_y)
        if pyautogui.mouseInfo().get('leftButton'):
            print(f"x: {click_x}")
            print(f"y: {click_y}")
            print(f"color: {color}")

click_positon()
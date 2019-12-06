import pyautogui as pag
import time

if __name__ == '__main__':
    data = pag.locateOnScreen("크롬.png")
    print(data)
    center = pag.center(data)
    print(center)
    pag.moveTo(center, duration=2)
    pag.doubleClick()
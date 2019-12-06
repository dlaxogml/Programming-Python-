import pyautogui as pag
import time

if __name__ == '__main__':
    # while True:
    #     x, y = pag.position()
    #     print("x : {}   y : {}".format(x, y), end = "\r")

    # pag.moveTo(725, 57)
    # pag.move(100, 200, duration=2)
    # pag.click()
    # pag.click()
    # pag.doubleClick()

    # pag.drag(0, 200, duration=1)
    # pag.rightClick()

    # pag.click(518, 183, duration=2)
    # pag.scroll(0, 100)

    # pag.moveTo(725, 57, duration=2)
    # pag.click()
    # time.sleep(1)
    # pag.typewrite("http://ticket.interpark.com/")
    # pag.press("enter")

    #TODO: scroll
    time.sleep(2)
    pag.hotkey("alt", "tab")
    pag.scroll(clicks=-2000, x=798, y=185)

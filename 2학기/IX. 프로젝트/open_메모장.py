import pyautogui as pag
import time

if __name__ == '__main__':
    # 메모장 프로그램 실행하자
    pag.press("winleft")
    pag.press("hangul")
    pag.typewrite("apahwkd")
    pag.press("enter")

    # Hello world 치자
    time.sleep(2)
    pag.typewrite("hello world")

    # 두 줄 내리자
    pag.press("enter", presses=2)

    # 반갑구나 세상아 하자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")

    # hello world 저장하자
    pag.press("hangul")
    pag.hotkey("ctrl", "s")
    time.sleep(1)
    pag.typewrite("C:\전공\PYTHON\helloworld")
    pag.press("hangul")
    pag.typewrite("vkdlfwjwkd")
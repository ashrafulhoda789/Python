import pyautogui
import time

def pyramid(n, char = '#'):
    time.sleep(3)

    for i in range(1, n + 1):
        row = char * i
        pyautogui.write(row, interval=0.252)
        pyautogui.press('enter')


num = int(input())
pyramid(num)


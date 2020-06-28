import pyautogui
import time

time.sleep(5)

# while True:
#     pyautogui.click()
#     time.sleep(.2)

for i in range(900):
    pyautogui.click()
    time.sleep(.5)
    print(i)

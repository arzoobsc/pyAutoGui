import pyautogui
import time

# time.sleep(5)

width, height = pyautogui.size()
iimi = 630, 750
pass_field = 700, 370
ok_button = 760, 408
entry = 65, 35
entry_statistics_report = 150, 210

print(f"Screen size is {width} x {height}")
im = pyautogui.locateAllOnScreen('stop.png')
print(list(im))
# stop = pyautogui.center(im)
# print(stop)

# pyautogui.click(iimi)
# time.sleep(1)
# pyautogui.typewrite('1795343', 0.05)
# pyautogui.click(pass_field)
# pyautogui.typewrite('A12345', 0.05)
# pyautogui.typewrite(['enter'])
# # pyautogui.click(ok_button)
#
# time.sleep(8)
# pyautogui.typewrite('Reg0038', 0.05)
# pyautogui.typewrite(['enter'])
#
# time.sleep(5)
#
# pyautogui.click(entry)
# pyautogui.click(entry_statistics_report)

#
# while True:
#     time.sleep(2)
#     print(pyautogui.position())
#     for i in (0, 5):
#         print(i)
#
#     pyautogui.click(stop)




























































































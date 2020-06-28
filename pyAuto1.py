import pyautogui, time

time.sleep(5)
pyautogui.click()  # click to put drawing program in focus
distance = 500
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.0001)  # move right
    distance = distance - 10
    pyautogui.dragRel(0, distance, duration=0.0001)  # move down
    pyautogui.dragRel(-distance, 0, duration=0.0001)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.0001)  # move up

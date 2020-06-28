import pyautogui, time

time.sleep(5)
pyautogui.click()  # click to put drawing program in focus


def draw_square_with_cross(length, duration):
    # go straight to right
    pyautogui.dragRel(length, 0, duration)
    # go straight to down 100px
    pyautogui.dragRel(0, length, duration)
    # go straight to left 100px
    pyautogui.dragRel(-length, 0, duration)
    # go straight to up 100px
    pyautogui.dragRel(0, -length, duration)

    pyautogui.dragRel(length, length, duration)

    pyautogui.moveRel(-length, 0, duration)
    pyautogui.dragRel(length, -length, duration)


draw_square_with_cross(200, 0.2)

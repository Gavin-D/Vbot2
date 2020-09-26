import pyautogui as pt
import time

buttons = ["W", "A", "S", "D"]

midnightMode = input("Midnight mode? (Y/N)\n")

def queueGame():
    print("queueing")
    time.sleep(2)
    pt.moveTo(939, 978)
    time.sleep(.5)
    pt.click()
    if midnightMode.upper() == "Y":
        for i in range(20):
            time.sleep(15)
            pt.keyDown("W")
            time.sleep(1)
            pt.keyUp("W")
            if i >= 19:
                afkAvoid(0, 0)
    else:
        for i in range(7):
            time.sleep(15)
            pt.keyDown("W")
            time.sleep(1)
            pt.keyUp("W")
            if i >= 8:
                afkAvoid(0, 0)


def afkAvoid(e, count):
    pt.keyDown(buttons[e])
    time.sleep(3)
    pt.keyUp(buttons[e])
    print("{}, {} for {}.".format(e, count, buttons[e]))
    if e >= 3:
        if count >= 120:
            print("requeue setup")
            time.sleep(30)
            pt.moveTo(930, 27)
            time.sleep(.5)
            pt.click()
            time.sleep(1)
            queueGame()
        else:
            print("button reloop")
            afkAvoid(0, count + 1)
    else:
        print("button loop++")
        afkAvoid(e + 1, count + 1)


queueGame()

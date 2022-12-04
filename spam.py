import pyautogui as pt
import random
import time





limit = int(input("Enter limit :"))
i = 0
time.sleep(5)

while i < int(limit):
    message = "Jai Shree Ram"
    pt.typewrite(message)
    pt.press("enter")
    i+=1

import pyautogui, time
from time import sleep
message = input("F, or Bee: ")
file = open("epic.txt", "r", encoding='utf-8')
bee_file = open("bee.txt", "r")
time.sleep(5)

if message == "f":
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press('enter', interval=5)
if message == "Bee":
    for word in bee_file:
        pyautogui.typewrite(word)
        pyautogui.press('enter',interval=0.75)
else:
    for word in range(0, 100):
        pyautogui.typewrite(message)
        pyautogui.press('enter',interval=0.75)
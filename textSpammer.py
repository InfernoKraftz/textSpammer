import pyautogui, time, keyboard
def sendText(n):
    pyautogui.typewrite(n + "\n")
sentence = input("Type your sentence: ")
while keyboard.is_pressed('q') == False:
    sendText(sentence)
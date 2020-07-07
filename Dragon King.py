import pyautogui,time
while True:
    for x in range(200):
        pyautogui.click(797,657,button='left')
        pyautogui.typewrite('జ్ఞ ా رً ॣ'+'longwang!'+str(x))
        pyautogui.typewrite(['enter'])
        time.sleep(0.1)
    time.sleep(600)
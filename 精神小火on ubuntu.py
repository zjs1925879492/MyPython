import pyautogui,time,socket

while True:
    now= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    hostname = socket.gethostname()
    pyautogui.click(797,657,button='left')
    pyautogui.typewrite('Send at:'+now +'  on'+hostname+'  for weichijunliaochiyan(wobuhuifanyi)')
    pyautogui.typewrite(['enter'])
    time.sleep(600)
from tkinter import Tk 
tk = Tk()
tk.overrideredirect(True)
tk.geometry('0x0+0+0')
import time
bug=0
x = None
while True:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        t = tk.selection_get(selection="CLIPBOARD")
        if x != t:
            x = t
            with open("./tmp.txt", 'a') as f:
                f.write('于'+timestamp+'复制了\n'+x)
                print('于',timestamp,'复制了\n'+x)
            bug=0
    except:
        if bug==0:
            bug=1
            print('于',timestamp,'复制了\n图片等非文字无法处理')


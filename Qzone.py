from pynput.keyboard import Controller,Key
import time,win32api,win32gui,win32con
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #Selenium包，根据浏览器内核不同请自选驱动安装

 
driver = webdriver.Chrome()
driver.get("https://i.qq.com/")         #电脑已登录QQ，点击快捷登录
elem = driver.find_element_by_class_name('login_wrap')
elem.click()
'''driver.find_element_by_id("u").send_keys("Your QQ ID xxxxxxx")
# #密码框输入密码
driver.find_element_by_id("p").send_keys("Your Password ********")
# #点击登陆按钮
driver.find_element_by_id("login_button").click()'''
print("成功登录QQ空间！")

time.sleep(8)
driver.find_element_by_id("$1_substitutor_content").click()
print('点击说说成功！')

time.sleep(2)
keyboard=Controller()
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
keyboard.type('Test by python at '+now)
print('文字输入成功')

win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(13,0,0,0)  #enter键位码是13
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
print('发送成功！')

 

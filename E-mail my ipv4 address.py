from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import socket,time,requests,re

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0'} 

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq邮箱号码
sender_qq = 'Your QQ email ID xxxxxxxxx@qq.com'
#pwd为qq邮箱的授权码
pwd = 'Your SMTP password ****************'
#收件人邮箱
receiver = 'receiver’s E-mail address'
def send(ip):
    print (ip[0])
    hostname = socket.gethostname()

    now= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    #邮件的正文内容
    mail_content = hostname+'\nIP address：'+ip[0]+'\nTime：'+now
    #邮件标题
    mail_title = 'IPv4 address！'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg["To"] = receiver
    smtp.sendmail(sender_qq, receiver, msg.as_string())
    smtp.quit()

while True:
    html_text = requests.get("https://ip.cn/",headers=headers).text
    ip = re.findall("<code>(.*?)</code>", html_text) 
    send(ip)
    time.sleep(3600)
    
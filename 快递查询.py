import requests,bs4,re,time

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0'}

number = (input('请输入快递单号'))
sort = input(
    '请输入快递服务商。顺丰：sfexpress，韵达：yunda，申通：sto，圆通：yto，中通：zto，EMS：ems，邮政：chinapost（请输入对应英文！）')


def get_url(code, id):
    url = 'http://m.46644.com/express/result.php?typetxt=%D6%D0%CD%A8&type=' + \
        code + '&number=' + id
    return url


url = get_url(sort, number)
print(url)

if __name__ == "__main__":
    while True:
        now= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        kuaidi = []
        response = requests.get(url, headers=headers)
        response.encoding = 'gb18030'
        response = response.text
        soup = bs4.BeautifulSoup(response, 'html.parser', from_encoding="utf8")
        for i in soup.findAll(name='div', attrs={'class': 'icontent'}):
            kuaidi.append(i.get_text())
            print(i.get_text())

        host_server = 'smtp.qq.com'
        # pwd为qq邮箱的授权码
        pwd = '16x* Your smtp password'
        # 发件人的邮箱
        sender_qq_mail = 'sender@qq.com'
        # 收件人邮箱
        receiver = 'receiver's E-mail address'

        # 邮件的正文内容
        mail_content = '\n'.join(kuaidi[::-1])+'\n\n发送于：'+now
        # 邮件标题
        mail_title = '快递追踪'

        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        time.sleep(3600)
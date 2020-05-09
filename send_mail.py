import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import unittest
import HTMLTestRunner
import os,time,datetime

#定义发送邮件
def sentmail(file_new):
    #发信邮箱
    mail_from="maoguoying@youedata.com"
    #收信邮箱
    mail_to="qiaoxin@youedata.com"
    # 定义正文
    f=open(file_new,"rb")
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype="html",_charset="utf-8")
    # 定义标题
    msg["Subject"]=u"测试报告"
    # 定义发送时间
    msg['date'] = time.strftime("%a, %d %b %Y %H:%M:%S %z")
    smtp = smtplib.SMTP()
    # 连接SMTP 服务器，此处用的126的SMTP 服务器
    smtp.connect("smtp.youedata.com")
    # 用户名密码
    smtp.login("maoguoying@youedata.com", "SbTfn1324")
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print("二毛发送")
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = "F:\\maoguoying\\report"
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'上一次生成的报告： '+lists[-2])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print (file_new)
    #调用发邮件模块
    sentmail(file_new)

if __name__ == "__main__":
    #执行测试用例
    # runner.run(alltestnames)
    #执行发邮件
    sendreport()





#
#
#
#
#
#
#
# # 发送邮箱
# sender="abc2123.com"
#
# # 接收邮箱
#  receiver="123@qq.com"
#
# # 发送邮件主题
# subject="python eail test"
#
# # 发送邮箱服务器
# smtpserver="smtp.126.com"
#
# # 发送邮箱用户/密码
# username="abc@126.com"
# password="123456"
#
# # 中文需参数"utf-8"单字节字符不需要
# # msg=MIMEText("你好","text","utf-8")
# msg["Subject"]=Header(subject,"utf-8")
# msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
# msg['Subject'] = subject
#
# smtp=smtplib.SMTP()
# smtp.connect("smtp.126.com")
# smtp.login(username,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()
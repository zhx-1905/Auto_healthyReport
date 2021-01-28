# coding:utf-8
import smtplib
from private_info import *
from email.mime.text import MIMEText
def mail(rec):
    # ----------1.跟发件相关的参数------
    # smtpserver = "smtp.163.com"         # 发件服务器
    smtpserver = "smtp.qq.com"
    port = 465                   # 端口
    sender = MAIL_SENDER         # 发件人
    psw = MAIL_PWD               # 密码
    receiver = rec               # 接收人
    
    # ----------2.编辑邮件的内容------
    subject =  '成功打卡提醒'             #邮件主题
    body = '<p>今日已成功打卡</p>'     # 定义邮件正文为html格式
    msg = MIMEText(body, "html", "utf-8")
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject

    # ----------3.发送邮件------
    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)                                 # 连服务器
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)                                      # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()                                                        # 关闭
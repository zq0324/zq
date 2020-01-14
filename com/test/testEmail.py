# coding=utf-8

import smtplib
from email.mime.text import MIMEText
import traceback


class SmtpSendMail:
    def __init__(self, config):
        try:
            # 设置发件服务器地址, 如: "smtp.qq.com"
            self.host = config["host"]

            # 设置发件服务器端口号. 有SSL(465)和非SSL(25)两种形式
            self.port = config["port"]

            # 设置发件邮箱, 一定要自己注册的邮箱, 如: "cheungmine@qq.com"
            self.sender = config["sender"]

            # 设置发件邮箱的密码, 登陆会用到
            self.password = config["password"]

            # 设置超时秒
            self.timeout = config["timeout"]

            # SSL
            if not config.get("SSL"):
                self.SSL = False
            else:
                self.SSL = True

                # session
            if self.SSL:
                session = smtplib.SMTP_SSL(self.host, self.port, self.timeout)
            else:
                session = smtplib.SMTP(self.host, self.port, self.timeout)

                # 登陆邮箱
            session.login(self.sender, self.password)

            self.session = session
        except Exception as e:
            traceback.print_exc()
        pass

    def sendmail(self, mailto):
        result = False
        try:
            # 设置正文为符合邮件格式的HTML内容
            msg = MIMEText(mailto["body"], 'html')

            # 设置邮件标题
            msg['subject'] = mailto["title"]

            # 设置发送人
            msg['from'] = self.sender

            # 设置邮件接收人
            msg['to'] = mailto["receiver"]

            # 发送邮件
            self.session.sendmail(self.sender, mailto["receiver"], msg.as_string())
            result = True
        except Exception as e:
            traceback.print_exc()
        finally:
            return result
        pass


        # test


mailfrom = {
    "host": "smtp.qq.com",
    "port": 465,
    "sender": "542722627@qq.com",
    "password": "JQzq0324",
    "timeout": 30,
    "SSL": True
}

mailto = {
    "receiver": "zhengqiang87@dingtalk.com",
    "title": "This is a test mail",
    "body": "<h1>Hi</h1><p>test mail from zq</p>"
}

smtp = SmtpSendMail(mailfrom)
print(smtp.sendmail(mailto))
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/05
# @Author  : Liufeiru

import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from conf.settings import *

class SendEmail():
    def __init__(self):
        self.test_report_path = REPORT_PATH
        # 发件箱用户名
        self.username = email_username
        # 发件箱密码
        self.password = email_password
        # 发件人邮箱
        self.sender = sender
        # 收件人邮箱
        self.receiver = receiver

    # 查找测试报告目录，找到最新生成的测试报告文件
    def new_report(self):
        # 列举report目录下的所有文件（名），结果以列表形式返回
        lists = os.listdir(self.test_report_path)
        # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，最终以文件时间从小到大排序
        # 最后对lists元素，按文件修改时间大小从小到大排序
        lists.sort(key=lambda fn: os.path.getmtime(self.test_report_path + "\\" + fn))
        # 获取最新文件的绝对路径
        file_new = os.path.join(self.test_report_path, lists[-1])
        # print(file_new)
        return file_new

    # 定义发送邮件
    def send_mail(self):
        file_new = self.new_report()
        with open(file_new, 'rb') as f:
            mail_body = f.read()

        # # 发件箱用户名
        # username = 'lfr_0123@yeah.net'
        # # 发件箱密码
        # password = 'xixi_2019'
        # # 发件人邮箱
        # sender = 'lfr_0123@yeah.net'
        # # 收件人邮箱
        # receiver = ['490635974@qq.com']

        # 邮件正文是MIMEText
        msg = MIMEText(mail_body, 'html', 'utf-8')
        # 邮件对象
        msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()
        msg['From'] = Header("测试机%s" % self.sender)
        msg['To'] = Header("测试负责人%s" % self.receiver)
        msg['date'] = time.strftime("%a, %d %b %Y %H:%M:%S %z")

        try:
            # 构造发送邮件对象
            smtpObj = smtplib.SMTP()
            # 连接邮箱服务器
            smtpObj.connect('smtp.yeah.net')
            # 登录邮箱
            smtpObj.login(self.username, self.password)
            # 发送者和接收者
            smtpObj.sendmail(self.sender, self.receiver, msg.as_string())
            smtpObj.quit()
            print("邮件已发出！注意查收")
        except Exception as e:
            print('error: %s' % e)

if __name__ == '__main__':
    s = SendEmail()
    s.send_mail()
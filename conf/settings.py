#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
# @Author  : Liufeiru

import os
import datetime
from dateutil.relativedelta import relativedelta

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例路径
TESTCASE_PATH = os.path.join(BASE_PATH, 'test_case')
# 定义测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report/')
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, 'log/log.txt')
# 定义token.yaml文件路劲
TOKEN_PATH  = os.path.join(BASE_PATH, 'common/token')
# 定义用例参数excel文件路径
EXCEL_PATH = os.path.join(BASE_PATH, 'common/testcase_data.xlsx')

# mysql数据库连接信息
DB_IP = '192.168.2.233'
PORT = 3308
DB_USERNAME = 'fxh_read'
DB_PASSWORD = 'fxhreadxxxx2019'
DB = 'dc'

# 项目接口基础连接
base_url = 'https://admin.myjhtech.com'

# 获取今天日期
today = datetime.date.today()
str_today = str(today)
# 获取昨天日期
yesterday = today - datetime.timedelta(1)
str_yesterday = str(yesterday)
# 前天
str_theDayBeforeYesterday = str(today - datetime.timedelta(2))
# 四天前日期
str_fourDays = str(today - datetime.timedelta(3))
# 五天前日期
str_fiveDays = str(today - datetime.timedelta(4))
# 六天前日期
str_sixDays = str(today - datetime.timedelta(5))
# 七天前日期
sevenDays = today - datetime.timedelta(6)
str_sevenDays = str(sevenDays)
# 八天前
str_eightDays = str(today - datetime.timedelta(7))
# 九天前
str_nineDays = str(today - datetime.timedelta(8))
# 十天前
str_tenDays = str(today - datetime.timedelta(9))
# 三十天前
str_thirtyDays = str(today - datetime.timedelta(30))

# 获取一个月前的今天的日期
aMonthAge = today - relativedelta(months=+1)
str_aMonthAge = str(aMonthAge)
# 两个月前的今天
tMonthAge = today - relativedelta(months=+2)
str_tMonthAge = str(tMonthAge)

# 邮件发送配置
# 发件箱用户名
email_username = 'lfr_0123@yeah.net'
# 发件箱第三方邮件客户端授权码
email_password = 'xixi2019'
# 发件人邮箱
sender = 'lfr_0123@yeah.net'
# 收件人邮箱
receiver = ['490635974@qq.com']




if __name__ == '__main__':
    print(str_tenDays)
    print(str_thirtyDays)
    print(BASE_PATH)
    print(EXCEL_PATH)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
# @Author  : Liufeiru

import os
import sys

# 获取项目目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 把path加入环境变量，0表示放在最前面，因为python解释器会按照列表顺序去依次到每个目录下去匹配你要导入的模块名，
# 只要在一个目录下匹配到了该模块名，就立刻导入，不再继续往后找
sys.path.insert(0, path)
# 导入配置文件中定义的测试用例的路径
from conf.settings import TESTCASE_PATH
# 导入配置文件中定义的测试报告的路径
from conf.settings import REPORT_PATH
import unittest
# 导入报告模板
from common import HTMLTestRunner
# 导入获取token模块
from common import login_token
# 导入发送邮件模块
from common import send_html_email
import time
# 自动根据测试用例的路径匹配查找测试用例文件（*.py）,并将查找到的测试用例组装到测试套件中
suite = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')

if __name__ == '__main__':
    # 获取token并写入token.yaml
    t = login_token.TokenToYaml()
    t.login_get_token()

    # 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="智选钱包管理后台项目接口自动化测试报告",
                                           description="测试用例情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()

    # 发送最新的测试报告
    s = send_html_email.SendEmail()
    s.send_mail()


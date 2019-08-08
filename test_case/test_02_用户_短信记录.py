#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/07
# @Author  : Liufeiru

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import json
import datetime
import unittest
import inspect
from conf import settings
from common import HTMLTestRunner
from common import logger
from common.tools import p
from common import read_token
from common.read_excel import *
from common.request_method import post_request
from db_operate.mysql_operate import *

class UserInfoUserMessage(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_sevenDays(self):
        """短信记录-默认搜索7天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        # 读取token.yaml中的token值
        Token = read_token.re_token()

        # 读取testcase_data.xlsx中的url与请求参数
        url = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 1, 6).get_body()

        today = datetime.date.today()
        sevenDays = today - datetime.timedelta(days=6)
        str_today = str(today)
        str_sevenDays = str(sevenDays)
        # 修改payloads中对应key的value值
        payloads.update(EndDate=str_today, StartDate=str_sevenDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_002_search_all(self):
        """短信记录-搜索全部"""
        logger.logger.logger.debug('当前方法: %s' % p.get_current_function_name())
        # 读取token.yaml中的token值
        Token = read_token.re_token()

        # 读取testcase_data.xlsx中的url与请求参数
        url = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_003_search_mobile(self):
        """短信记录-搜索手机号"""
        logger.logger.logger.debug('当前方法: %s' % p.get_current_function_name())
        # 读取token.yaml中的token值
        Token = read_token.re_token()

        # 读取testcase_data.xlsx中的url与请求参数
        url = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_usermessage', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)


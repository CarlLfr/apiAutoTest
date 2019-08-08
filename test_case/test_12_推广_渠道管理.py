#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/27
# @Author  : Liufeiru

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
import inspect
from common import logger
from common.tools import p
from common import read_token
from common.read_excel import *
from common.request_method import post_request
from db_operate.mysql_operate import *

class NewsList(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def setDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_channel_fault(self):
        """推广-渠道管理-默认页面"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM company"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_002_search_company(self):
        """推广-渠道管理-公司搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_003_billingMode_CPA2(self):
        """推广-渠道管理-计价方式-按激活收费（CPA2）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM company WHERE billing_mode = 'CPA2'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_004_billingMode_CPA(self):
        """推广-渠道管理-计价方式-按激活收费（CPA）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 4, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM company WHERE billing_mode = 'CPA'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_005_billingMode_CPS(self):
        """推广-渠道管理-计价方式-按激活收费（CPS）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM company WHERE billing_mode = 'CPS'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_006_billingMode_CPC(self):
        """推广-渠道管理-计价方式-按激活收费（CPC）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM company WHERE billing_mode = 'CPC'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_007_company_edit(self):
        """推广-渠道管理-公司编辑"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_list', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)
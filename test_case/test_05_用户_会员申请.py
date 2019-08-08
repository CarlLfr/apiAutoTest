#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/15
# @Author  : Liufeiru

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
import inspect
from conf import settings
from common import logger
from common.tools import p
from common import read_token
from common.read_excel import *
from common.request_method import post_request
from db_operate.mysql_operate import *

class VipApplyList(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_all(self):
        """用户-会员申请-默认搜索全部"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_002_search_mobile(self):
        """用户-会员申请-搜索手机号"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where uid = (select id from users where account='18768124236')"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_003_vipApplyTime_yesterday(self):
        """用户-会员申请-会员申请时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 3, 6).get_body()

        payloads.update(BeginTime=settings.str_yesterday, EndTime=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where begin_date = '"+settings.str_yesterday+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_004_vipApplyTime_sevenDays(self):
        """用户-会员申请-会员申请时间-七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 4, 6).get_body()

        payloads.update(BeginTime=settings.str_sevenDays, EndTime=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where begin_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_005_state_success(self):
        """用户-会员申请-状态-审核通过"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where state = 'SUCCESS'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_006_state_fail(self):
        """用户-会员申请-状态-审核拒绝"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where state = 'FAIL'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_007_state_examine(self):
        """用户-会员申请-状态-待审核"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where state = 'EXAMINE'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_008_state_refund(self):
        """用户-会员申请-状态-已退款"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'vip_vip_apply_list', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from vip_record where state = 'EXAMINE'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])
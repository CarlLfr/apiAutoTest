#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/18
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

class SysProductGetProductH5(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_all(self):
        """运营-H5产品-默认全部"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_002_search_mechanism(self):
        """运营-H5产品-机构搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where mechanism = '有呗'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_003_search_productName(self):
        """运营-H5产品-产品名称搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where mechanism = '优智借'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_004_amount_Under_5000(self):
        """运营-H5产品-可借金额-5000以内"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 4, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where max_amount > 0 and max_amount <= 5000"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_005_amount_5000_to_1w(self):
        """运营-H5产品-可借金额-5000-1万"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where max_amount >= 5000 and max_amount <= 10000"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_006_amount_1w_to_5w(self):
        """运营-H5产品-可借金额-1万-5万"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where max_amount >= 10000 and max_amount <= 50000"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_007_amount_5w_20w(self):
        """运营-H5产品-可借金额-5万-20万"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where max_amount >= 50000 and max_amount <= 200000"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_008_amount_over_20w(self):
        """运营-H5产品-可借金额-20万以上"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where max_amount >= 200000"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_009_surplus_use(self):
        """运营-H5产品-单日剩余投放数-有剩余"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        # sql = "select count(*) from product_h5 where max_amount >= 200000"
        # dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        # self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_010_surplus_temporaryunuse(self):
        """运营-H5产品-单日剩余投放数-无剩余"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 10, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 10, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        # sql = "select count(*) from product_h5 where max_amount >= 200000"
        # dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        # self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_011_isUsed_use(self):
        """运营-H5产品-状态-投放"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 11, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 11, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where is_used = 'USE'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_012_isUsed_unused(self):
        """运营-H5产品-状态-结束"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 12, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 12, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from product_h5 where is_used = 'UNUSED'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["ProductH5ListCount"], dbo[0])

    def test_013_product_h5_detail(self):
        """运营-H5产品-查看H5产品详情（机构：好借，产品名：好借）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 13, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_get_product_h5', 13, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

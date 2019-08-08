#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/22
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

class SysProductH5DataDetail(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_today_register_date(self):
        """运营-H5数据-默认搜索（当天、按注册日期统计）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 1, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select distinct count(product_id) from record_product_by_register_time where register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_002_product_name(self):
        """运营-H5数据-数据明细-产品名称搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 2, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select pv1, pv2, uv, register_count from record_product_by_register_time where product_id = 357 and register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo != None:
            self.assertEqual(result["SumPv1"], dbo[0])
            self.assertEqual(result["SumPv2"], dbo[1])
            self.assertEqual(result["SumUv"], dbo[2])
            self.assertEqual(result["SumRegisterCount"], dbo[3])
        else:
            pass

    def test_003_billingMode_CPA(self):
        """运营-H5数据-数据明细-结算方式：按注册收费（CPA）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 3, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(DISTINCT ph.name) FROM product_h5 as ph INNER JOIN record_product_by_register_time as rp on ph.id = rp.product_id WHERE rp.register_date='"+settings.str_today+"' AND ph.billing_mode='CPA'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_004_billingMode_CPS(self):
        """运营-H5数据-数据明细-结算方式：按成交收费（CPS）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 4, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(DISTINCT ph.name) FROM product_h5 as ph INNER JOIN record_product_by_register_time as rp on ph.id = rp.product_id WHERE rp.register_date='" + settings.str_today + "' AND ph.billing_mode='CPS'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_005_billingMode_CPC(self):
        """运营-H5数据-数据明细-结算方式：按点击收费（CPC）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 5, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(DISTINCT ph.name) FROM product_h5 as ph INNER JOIN record_product_by_register_time as rp on ph.id = rp.product_id WHERE rp.register_date='" + settings.str_today + "' AND ph.billing_mode='CPC'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_006_dateType_by_happen_time(self):
        """运营-H5数据-数据明细-统计口径：按发生日期统计"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 6, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select distinct count(product_id) from record_product_by_register_time where register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["UserSum"], dbo[0])

    def test_007_data_detail(self):
        """运营-H5数据-数据明细-明细"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_008_platform_summary_default(self):
        """运营-H5数据-平台汇总-默认搜索（1个月、按发生日期统计）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 8, 6).get_body()

        payloads.update(StartDate=settings.str_aMonthAge, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT SUM(pv1), SUM(pv2), SUM(register_count) FROM record_product_by_happen_time WHERE happen_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"][0]["Pv1"], str(dbo[0]))
        self.assertEqual(result["Result"][0]["Pv2"], str(dbo[1]))
        self.assertEqual(result["Result"][0]["Pv2"], str(dbo[2]))

    def test_009_platform_summary_by_register_time(self):
        """运营-H5数据-平台汇总-1个月、按注册日期统计"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_h5_date_detail', 9, 6).get_body()

        payloads.update(StartDate=settings.str_aMonthAge, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT SUM(pv1), SUM(pv2), SUM(register_count) FROM record_product_by_register_time WHERE register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"][0]["Pv1"], dbo[0])
        self.assertEqual(result["Result"][0]["Pv2"], dbo[1])
        self.assertEqual(result["Result"][0]["Pv2"], dbo[2])
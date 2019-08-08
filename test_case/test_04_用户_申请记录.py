#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/10
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

class UserInfoRecordProductH5(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_all(self):
        """申请记录-搜索全部（默认）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_002_search_mobile(self):
        """申请记录-手机号"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where uid = (select id from users where account = '18689505251')"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_003_search_product_H5(self):
        """申请记录-H5产品"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where product_id = (select id from product_h5 where mechanism = '51人品贷')"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_004_firstBrowsingTime_today(self):
        """申请记录-首次浏览时间-今天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 4, 6).get_body()
        payloads.update(BrowseStartDate=settings.str_today, BrowseEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_browse_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_005_firstBrowsingTime_yesterday(self):
        """申请记录-首次浏览时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 5, 6).get_body()
        payloads.update(BrowseStartDate=settings.str_yesterday, BrowseEndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_browse_date = '"+settings.str_yesterday+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_006_firstBrowsingTime_threedDays(self):
        """申请记录-首次浏览时间-近三天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 6, 6).get_body()
        payloads.update(BrowseStartDate=settings.str_theDayBeforeYesterday, BrowseEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_browse_date between '"+settings.str_theDayBeforeYesterday+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_007_firstBrowsingTime_sevenDays(self):
        """申请记录-首次浏览时间-近七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 7, 6).get_body()
        payloads.update(BrowseStartDate=settings.str_sevenDays, BrowseEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_browse_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_008_firstApply_today(self):
        """申请记录-首次点击申请时间-今天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 8, 6).get_body()
        payloads.update(ApplyStartDate=settings.str_today, ApplyEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_apply_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_009_firstApply_yesterday(self):
        """申请记录-首次点击申请时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 9, 6).get_body()
        payloads.update(ApplyStartDate=settings.str_yesterday, ApplyEndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_apply_date = '"+settings.str_yesterday+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_010_firstApply_threeDays(self):
        """申请记录-首次点击申请时间-近三天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 10, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 10, 6).get_body()
        payloads.update(ApplyStartDate=settings.str_theDayBeforeYesterday, ApplyEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_apply_date between '"+settings.str_theDayBeforeYesterday+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_011_firstApply_threeDays(self):
        """用户-申请记录-首次点击申请时间-近七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 11, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 11, 6).get_body()
        payloads.update(ApplyStartDate=settings.str_sevenDays, ApplyEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_apply_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_012_registerTime_today(self):
        """用户-申请记录:注册时间-今天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 12, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 12, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_today, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_013_registerTime_yesterday(self):
        """用户-申请记录:注册时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 13, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 13, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_yesterday, RegisterEndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_register_date = '"+settings.str_yesterday+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_014_registerTime_threeDays(self):
        """用户-申请记录:注册时间-近三天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 14, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 14, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_theDayBeforeYesterday, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_register_date between '"+settings.str_theDayBeforeYesterday+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_015_registerTime_sevenDays(self):
        """用户-申请记录:注册时间-近七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 15, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 15, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_sevenDays, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_register_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_016_registerTime_userDefine(self):
        """用户-申请记录:注册时间-自定义"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 16, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 16, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_nineDays, RegisterEndDate=settings.str_eightDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from record_product_h5 where first_register_date between '"+settings.str_nineDays+"' and '"+settings.str_eightDays+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_017_register_source(self):
        """用户-申请记录:注册渠道-电销5"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 16, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_record_product_h5', 16, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_nineDays, RegisterEndDate=settings.str_eightDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(rp.id) FROM users u LEFT JOIN record_product_h5 rp ON u.id=rp.uid WHERE u.out_put_source = '电销5'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])
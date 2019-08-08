#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
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

class UserInfoList(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        # 获取当前函数名
        return inspect.stack()[1][3]

    def test_001_search_mobile(self):
        """用户管理-搜索手机号"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        # 读取token.yaml中的token值
        Token = read_token.re_token()

        # 读取testcase_data.xlsx中的url与请求参数
        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = 'select id from users where account = "18768124236"'
        dbo = DbOperate(sql).db_operate()

        # 断言是否返回200
        self.assertEqual(res, 200)
        # 断言返回结果数量是否一致
        self.assertEqual(result["Result"]["UserSum"], 1)
        # 断言返回的id是否与该条件下数据库查询id一致
        self.assertEqual(result["Result"]["List"][0]["Id"], str(dbo[0]))

    def test_002_register_time_all(self):
        """用户管理-搜索注册时间-全部"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = 'select count(*) from users'
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_003_register_time_today(self):
        """用户管理-搜索注册时间-今天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 3, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_today, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where register_date = '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_004_register_time_yesterday(self):
        """用户管理-搜索注册时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 4, 6).get_body()
        # 获取昨天日期（年月日）加入payloads
        payloads.update(RegisterStartDate=settings.str_yesterday, RegisterEndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
        self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where register_date = '"+settings.str_yesterday+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_005_register_time_threeDays(self):
        """用户管理-搜索注册时间-近三天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 5, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_theDayBeforeYesterday, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where register_date between '"+settings.str_theDayBeforeYesterday+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_006_register_time_sevenDays(self):
        """用户管理-搜索注册时间-近七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 6, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_sevenDays, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where register_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    @unittest.skip("跳过自定义注册时间搜索")
    def test_007_register_time_userDefine(self):
        """用户管理-搜索注册时间-自定义"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 7, 6).get_body()
        payloads.update(RegisterStartDate=settings.str_nineDays, RegisterEndDate=settings.str_eightDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where register_date between '"+settings.str_nineDays+"' and '"+settings.str_eightDays+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo[0] != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_008_search_source(self):
        """用户管理—搜索渠道"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users where out_put_source = '电销5'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_009_authType_no(self):
        """用户管理-认证状态-未实名认证"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users_auth where is_real_name = 0"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_010_authType_yes(self):
        """用户管理-认证状态-已实名认证"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 10, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 10, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users_auth where is_real_name = 1"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    @unittest.skip("APP上已无填写资料入口")
    def test_011_authType_infoFilled(self):
        """用户管理-认证状态-已填写资料"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 11, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 11, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users_auth where is_real_name = 2"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_012_search_userName(self):
        """用户管理-搜索姓名"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select uid from users_info where id_name = '刘斐汝'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], 1)
        self.assertEqual(result["Result"]["List"][0]["Id"], str(dbo[0]))

    @unittest.skip("APP已无大额贷项目")
    def test_013_isLarger_yes(self):
        """用户管理-是否申请大额贷-是"""
        pass

    def test_015_register_method(self):
        """用户-用户管理:注册方式-H5"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(*) FROM `users` WHERE register_app = 5"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_016_search_multiCondition(self):
        """用户-用户管理-综合查询：注册时间-全部，注册渠道-电销5，注册方式-H5，激活状态-已激活"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_list', 12, 6).get_body()

        payloads.update(RegisterStartDate=settings.str_theDayBeforeYesterday, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(*) FROM `users` WHERE register_app = 5 AND out_put_source = '电销5' AND register_date BETWEEN '"+settings.str_sevenDays+"' AND '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass


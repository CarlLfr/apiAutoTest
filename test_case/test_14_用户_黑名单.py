#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/07
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

class UserInfo(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_userInfo_black_list_default(self):
        """用户-用户管理-黑名单-默认页面（注册时间：全部）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from users_black"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo != None:
            self.assertEqual(result["Result"]["UserSum"], dbo[0])
        else:
            pass

    def test_002_userInfo_black_list_search_account(self):
        """用户-用户管理-黑名单-手机号搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select uid from users_black where account = '15968856860'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        if dbo != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo[0])
        else:
            pass

    def test_003_userInfo_black_list_register_time_today(self):
        """用户-用户管理-黑名单-注册时间-今天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 3, 6).get_body()

        payloads.update(RegisterStartDate=settings.str_today, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date = '"+settings.str_today+"'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date = '"+settings.str_today+"' ORDER BY ub.create_time LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_004_userInfo_black_list_register_time_yesterday(self):
        """用户-用户管理-黑名单-注册时间-昨天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 4, 6).get_body()

        payloads.update(RegisterStartDate=settings.str_yesterday, RegisterEndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date = '" + settings.str_yesterday + "'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date = '" + settings.str_yesterday + "' ORDER BY ub.create_time LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_005_userInfo_black_list_register_time_threeDays(self):
        """用户-用户管理-黑名单-注册时间-近三天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 5, 6).get_body()

        payloads.update(RegisterStartDate=settings.str_theDayBeforeYesterday, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date BETWEEN '"+settings.str_theDayBeforeYesterday+"' AND '"+settings.str_today+"'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date BETWEEN '"+settings.str_theDayBeforeYesterday+"' AND '"+settings.str_today+"' ORDER BY ub.create_time LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_006_userInfo_black_list_register_time_sevenDays(self):
        """用户-用户管理-黑名单-注册时间-近七天"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 6, 6).get_body()

        payloads.update(RegisterStartDate=settings.str_sevenDays, RegisterEndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date BETWEEN '" + settings.str_sevenDays + "' AND '" + settings.str_today + "'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.register_date BETWEEN '" + settings.str_sevenDays + "' AND '" + settings.str_today + "' ORDER BY ub.create_time LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_007_userInfo_users_black_source_search(self):
        """用户-用户管理-黑名单-注册时间-注册渠道搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.market_source = '官网iOS' OR u.out_put_source = '官网iOS'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users u ON u.id = ub.uid WHERE u.market_source = '官网iOS' OR u.out_put_source = '官网iOS' ORDER BY ub.create_time LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_008_userInfo_users_black_name_search(self):
        """用户-用户管理-黑名单-注册时间-姓名搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_black ub LEFT JOIN users_info ui ON ui.uid = ub.uid WHERE ui.id_name = '黄超斌'"
        sql2 = "SELECT ub.uid FROM users_black ub LEFT JOIN users_info ui ON ui.uid = ub.uid WHERE ui.id_name = '黄超斌'"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        if dbo2 != None:
            self.assertEqual(result["Result"]["List"][0]["Uid"], dbo2[0])
        else:
            pass

    def test_009_userInfo_black_add(self):
        """用户-用户管理-黑名单-注册时间-添加黑名单"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT id FROM users_black WHERE account = '18768124236'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertIsNotNone(dbo)

    def test_010_userInfo_black_add_edit(self):
        """用户-用户管理-黑名单-注册时间-编辑黑名单"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 10, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 10, 6).get_body()
        remark = payloads["Remark"]

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT remark FROM users_black WHERE account = '18768124236'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(remark, dbo[0])

    def test_011_userInfo_black_add_delete(self):
        """用户-用户管理-黑名单-注册时间-删除黑名单"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 11, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_black_list', 11, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT remark FROM users_black WHERE account = '18768124236'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertIsNone(dbo)
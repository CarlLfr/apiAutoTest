#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/17
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

    def test_001_userInfo(self):
        """用户-查看用户详情-【查看】按钮userinfo"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select coalesce(out_put_source, market_source) from users where id='1008623658'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["List"]["MarketSource"], dbo[0])

    def test_002_userInformation_oldUsers(self):
        """用户-查看用户详情-老用户(已填写基础信息)"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select id_no from users_info where account='18768124236'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["RealNameInfo"]["IdNo"], dbo[0])

    def test_003_userInformation_newUsers(self):
        """用户-查看用户详情-新用户(未填写基础信息)"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)
        self.assertEqual(result["RealNameInfo"]["IdNo"], "")

    def test_004_userInfo_h5list(self):
        """用户-用户管理-用户详情【查看】按钮-H5记录"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 4, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(ph.name) FROM record_product_h5 rp LEFT JOIN users u ON u.id=rp.uid LEFT JOIN product_h5 ph ON rp.product_id = ph.id WHERE u.id = '1008624327' AND rp.first_register_time IS NOT NULL"
        dbo1 = DbOperate(sql).db_operate()
        dbo2 = DbOperate(sql).db_operate_fetchall()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        self.assertEqual(result["Result"]["List"][0]["ProductName"], dbo2[0][0])
        self.assertEqual(result["Result"]["List"][1]["ProductName"], dbo2[1][0])

    def test_005_large_loan_list(self):
        """用户-用户管理-用户详情【查看】按钮-大额贷记录"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_006_userInfo_sysmessage(self):
        """用户-查看用户详情-查看-帖子记录/系统消息"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users_msg WHERE uid = 1008624327"
        sql2 = "SELECT msg_title, msg_content FROM users_msg WHERE uid = 1008624327 ORDER BY create_time DESC LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        # 判段数据库搜索结果是否为空
        if dbo1 != None:
            self.assertEqual(result["Result"]["UserSum"], dbo1[0])
            # self.assertEqual(result["Result"]["List"][0]["MsgTitle"], dbo2[0])
            # self.assertEqual(result["Result"]["List"][0]["MsgContent"], dbo2[1])
        else:
            pass

    def test_007_userInfo_userMessage(self):
        """用户-查看用户详情-查看-短信记录"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_008_userInfo_loginHistory(self):
        """用户-查看用户详情-查看-登录历史"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM login_record WHERE uid = 1008624327"
        sql2 = "SELECT create_time, stage, ip_address FROM login_record WHERE uid = 1008624327 ORDER BY create_time DESC LIMIT 1"
        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo1[0])
        self.assertEqual(result["Result"]["List"][0]["CreateTime"], dbo2[0])

        # 判断stage
        stage_dict = {"login": "密码登录", "fastlogin": "验证码登录", "silentlogin": "静默登录", "register": "注册"}
        # print(stage_dict[dbo2[1]])
        self.assertEqual(result["Result"]["List"][0]["Stage"], stage_dict[dbo2[1]])

        # 判段数据库搜索结果是否为空
        if dbo2[2] != None:
            self.assertEqual(result["Result"]["List"][0]["IpAddress"], dbo2[2])
        else:
            pass
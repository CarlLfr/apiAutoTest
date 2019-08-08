#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/08
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

class UserInfoFeedBack(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def tearDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_sevenDays(self):
        """意见反馈-搜索时间 默认（7天）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 1, 6).get_body()
        # 获取日期并加入payloads
        payloads.update(EndDate=settings.str_today, StartDate=settings.str_sevenDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where create_date between '"+settings.str_sevenDays+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_002_search_mobile(self):
        """意见反馈-搜索手机号"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 2, 6).get_body()
        # 获取日期并加入payloads
        payloads.update(EndDate=settings.str_today, StartDate=settings.str_sevenDays)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where uid=(select id from users where account='18768124236')"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_003_state_noProcessed(self):
        """意见反馈-处理状态-待处理"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '待处理'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_004_state_processed(self):
        """意见反馈-处理状态-已处理"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 4, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type != '待处理'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_005_feedbackType_contacted(self):
        """意见反馈-快捷备注-已联系"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '已联系'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_006_feedbackType_following(self):
        """意见反馈-快捷备注-持续跟进"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '持续跟进'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_007_feedbackType_addWeChat(self):
        """意见反馈-快捷备注-已加微信"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '快捷备注'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_008_feedbackType_noAnswer(self):
        """意见反馈-快捷备注-无人接听"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 8, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '无人接听'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_009_feedbackType_hangUp(self):
        """意见反馈-快捷备注-挂断"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '挂断'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_010_feedbackType_callReject(self):
        """意见反馈-快捷备注-拒接"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '拒接'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_011_feedbackType_callReminder(self):
        """意见反馈-快捷备注-来电提醒"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '来电提醒'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_012_feedbackType_intervention(self):
        """意见反馈-快捷备注-产品部介入"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'userinfo_feedback', 9, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "select count(*) from feedback where feedback_type = '产品部介入'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])
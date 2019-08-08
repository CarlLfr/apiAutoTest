#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/24
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

class NewsList(unittest.TestCase):
    def setUp(self):
        print('%s测试用例开始执行...' % p.get_current_class_name())

    def setDown(self):
        print('%s测试用例执行完毕...' % p.get_current_class_name())

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_001_search_default(self):
        """运营-文章列表-默认搜索（创建时间：今天-前一个月）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 1, 6).get_body()

        payloads.update(StartDate=settings.str_aMonthAge, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE create_time between '"+settings.str_aMonthAge+"' and '"+settings.str_today+"'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_002_search_title(self):
        """运营-文章列表-标题搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE title = '贷款老被拒?你可能踩到雷区了'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_003_newsType_shangAnzhuanQu(self):
        """运营-文章列表-文章分类-上岸专区"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE news_type = '上岸专区'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_004_newsType_jieKuanJiQiao(self):
        """运营-文章列表-文章分类-借款技巧"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 4, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE news_type = '借款技巧'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_005_newsType_tiEMiaoZhao(self):
        """运营-文章列表-文章分类-提额妙招"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE news_type = '提额妙招'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_006_newsType_shenKaGongNue(self):
        """运营-文章列表-文章分类-申卡攻略"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 6, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM dc_news WHERE news_type = '申卡攻略'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(result["Result"]["UserSum"], dbo[0])

    def test_007_newsEdit(self):
        """运营-文章列表-查看文章"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'news_news_list', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'news_news_list', 7, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    @unittest.skip("跳过运营-文章列表-添加文章")
    def test_008_add_news(self):
        """运营-文章列表-添加文章"""
        pass
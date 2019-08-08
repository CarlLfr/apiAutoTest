#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/26
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

    def test_001_recommend_default(self):
        """运营-推荐位管理-推荐位管理-默认页面"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 1, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM down_list WHERE pid != 0"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(len(result["Result"]), dbo[0])

    def test_002_addRecommend_add(self):
        """运营-推荐位管理-点击添加按钮"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 2, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql = "SELECT COUNT(id) FROM product_h5 WHERE is_used = 'USE'"
        dbo = DbOperate(sql).db_operate()

        self.assertEqual(res, 200)
        self.assertEqual(len(result["Result"]), dbo[0])

    def test_003_addRecommend_sure(self):
        """运营-推荐位管理-添加-确定"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 3, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_004_addRecommend_delete(self):
        """运营-推荐位管理-删除"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 4, 6).get_body()

        # 通过pid获取down_list的id
        sql = "SELECT id FROM down_list WHERE pid = '357'"
        dbo = DbOperate(sql).db_operate()
        payloads.update(Id=str(dbo[0]))

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)

    def test_005_recommend_edit(self):
        """运营-推荐位管理-编辑-确定"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'sysproduct_down_list', 5, 6).get_body()

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        self.assertEqual(res, 200)
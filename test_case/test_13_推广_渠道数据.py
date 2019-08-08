#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/31
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

    def test_001_summary_detail_default(self):
        """推广-渠道数据-每日汇总-默认页面"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 1, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 1, 6).get_body()

        payloads.update(StartDate=settings.str_thirtyDays, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        # 验证接口返回状态码
        self.assertEqual(res, 200)

    def test_002_statistical_by_register_time(self):
        """推广-渠道数据-每日汇总-统计口径-按注册日期"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 2, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 2, 6).get_body()

        payloads.update(StartDate=settings.str_thirtyDays, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT SUM(page_uv), SUM(register_count), SUM(active_count), SUM(h5_uv), SUM(h5_register) FROM record_source_by_register_time WHERE register_date = '" + settings.str_yesterday + "'"
        sql2 = "SELECT SUM(register_count), SUM(active_count), SUM(h5_register) FROM record_source_by_register_time WHERE register_date BETWEEN '" + settings.str_thirtyDays + "' AND '" + settings.str_today + "'"
        sql3 = "SELECT COUNT(id) FROM users WHERE register_date = '"+settings.str_yesterday+"'"
        sql4 = "SELECT COUNT(id) FROM users WHERE register_date = '"+settings.str_yesterday+"' and login_date = '"+settings.str_yesterday+"'"
        sql5 = "SELECT COUNT(id) FROM users WHERE register_date BETWEEN '"+settings.str_thirtyDays+"' AND '"+settings.str_today+"'"
        sql6 = "SELECT COUNT(id) FROM users WHERE register_date = login_date AND register_date BETWEEN '"+settings.str_thirtyDays+"' AND '"+settings.str_today+"'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()
        dbo5 = DbOperate(sql5).db_operate()
        dbo6 = DbOperate(sql6).db_operate()

        # 验证接口返回状态码
        self.assertEqual(res, 200)

        # 断言请求返回的数据跟数据库record_source_by_register_time()查询数据是否一致

        # 核对昨天进入产品详情页面的人数
        self.assertEqual(result["Result"][1]["PageUv"], str(dbo1[0]))
        # 核对昨天APP的注册人数
        self.assertEqual(result["Result"][1]["RegisterCount"], str(dbo1[1]))
        # 核对昨天的激活人数
        self.assertEqual(result["Result"][1]["ActiveCount"], str(dbo1[2]))
        # 核对昨天的h5UV
        self.assertEqual(result["Result"][1]["H5Uv"], str(dbo1[3]))
        # 核对昨天的h5注册数
        self.assertEqual(result["Result"][1]["H5Register"], str(dbo1[4]))
        # 核对总注册量
        self.assertEqual(result["SumRegisterCount"], str(dbo2[0]))
        # 核对总激活量
        self.assertEqual(result["SumActiveCount"], str(dbo2[1]))
        # 核对总H5注册量
        self.assertEqual(result["SumH5Register"], str(dbo2[2]))

        # 断言请求返回数据跟数据库别的表查询数据是否一致
        self.assertEqual(result["Result"][1]["RegisterCount"], str(dbo3[0]))
        self.assertEqual(result["Result"][1]["ActiveCount"], str(dbo4[0]))
        self.assertEqual(result["SumRegisterCount"], str(dbo5[0]))
        self.assertEqual(result["SumActiveCount"], str(dbo6[0]))

    def test_003_statistical_by_happen_time(self):
        """推广-渠道数据-每日汇总-统计口径-按发生日期"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 3, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 3, 6).get_body()

        payloads.update(StartDate=settings.str_thirtyDays, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT SUM(page_uv), SUM(register_count), SUM(active_count), SUM(h5_uv), SUM(h5_register) FROM record_source_by_happen_time WHERE happen_date = '"+settings.str_yesterday+"'"
        sql2 = "SELECT SUM(register_count), SUM(active_count), SUM(h5_register) FROM record_source_by_happen_time WHERE happen_date BETWEEN '"+settings.str_thirtyDays+"' AND '"+settings.str_today+"'"
        sql3 = "SELECT COUNT(id) FROM users WHERE register_date = '"+settings.str_yesterday+"'"
        sql4 = "SELECT COUNT(id) FROM users WHERE register_date = '"+settings.str_yesterday+"' and login_date = '"+settings.str_yesterday+"'"
        sql5 = "SELECT COUNT(id) FROM users WHERE register_date BETWEEN '"+settings.str_thirtyDays+"' AND '"+settings.str_today+"'"
        sql6 = "SELECT COUNT(id) FROM users WHERE register_date = login_date AND register_date BETWEEN '"+settings.str_thirtyDays+"' AND '"+settings.str_today+"'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()
        dbo5 = DbOperate(sql5).db_operate()
        dbo6 = DbOperate(sql6).db_operate()

        # 验证接口返回状态码
        self.assertEqual(res, 200)

        # 断言请求返回的数据跟数据库record_source_by_happen_time()查询数据是否一致

        # 核对昨天进入产品详情页面的人数
        self.assertEqual(result["Result"][1]["PageUv"], str(dbo1[0]))
        # 核对昨天APP的注册人数
        self.assertEqual(result["Result"][1]["RegisterCount"], str(dbo1[1]))
        # 核对昨天的激活人数
        self.assertEqual(result["Result"][1]["ActiveCount"], str(dbo1[2]))
        # 核对昨天的h5UV
        self.assertEqual(result["Result"][1]["H5Uv"], str(dbo1[3]))
        # 核对昨天的h5注册数
        self.assertEqual(result["Result"][1]["H5Register"], str(dbo1[4]))
        # 核对总注册量
        self.assertEqual(result["SumRegisterCount"], str(dbo2[0]))
        # 核对总激活量
        self.assertEqual(result["SumActiveCount"], str(dbo2[1]))
        # 核对总H5注册量
        self.assertEqual(result["SumH5Register"], str(dbo2[2]))

        # 断言请求返回数据跟数据库别的表查询数据是否一致
        self.assertEqual(result["Result"][1]["RegisterCount"], str(dbo3[0]))
        self.assertEqual(result["Result"][1]["ActiveCount"], str(dbo4[0]))
        self.assertEqual(result["SumRegisterCount"], str(dbo5[0]))
        self.assertEqual(result["SumActiveCount"], str(dbo6[0]))

    def test_004_single_channel_statistics_default(self):
        """推广-渠道数据-单渠道统计-默认页面（按注册日期）"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 4, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 4, 6).get_body()

        payloads.update(StartDate=settings.str_today, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        # sql1 = "SELECT COUNT(id) FROM record_source_by_register_time WHERE register_date = '"+settings.str_today+"'"
        # sql2 = "SELECT page_uv, register_count, active_count, h5_register FROM record_source_by_register_time WHERE register_date = '"+settings.str_today+"' ORDER BY id LIMIT 1;"
        #
        # dbo1 = DbOperate(sql1).db_operate()
        # dbo2 = DbOperate(sql2).db_operate()

        self.assertEqual(res, 200)
        # self.assertEqual(result["UserSum"], dbo1[0])
        # self.assertEqual(result["Result"][0]["PageUv"], dbo2[0])
        # self.assertEqual(result["Result"][0]["RegisterCount"], dbo2[1])
        # self.assertEqual(result["Result"][0]["ActiveCount"], dbo2[2])
        # self.assertEqual(result["Result"][0]["H5Register"], dbo2[3])

    def test_005_single_channel_statistics_register_time(self):
        """推广-渠道数据-单渠道统计-按注册日期"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 5, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 5, 6).get_body()

        payloads.update(StartDate=settings.str_yesterday, EndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(rr.id), SUM(rr.register_count), SUM(rr.active_count), SUM(rr.h5_register) FROM source AS s LEFT JOIN record_source_by_register_time AS rr ON rr.source = s.source LEFT JOIN company AS c ON s.company_id = c.id WHERE rr.register_date = '"+settings.str_yesterday+"'"
        sql2 = "SELECT page_uv, register_count, active_count, h5_register FROM record_source_by_register_time WHERE register_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1"
        sql3 = "SELECT COUNT(id) FROM users WHERE out_put_source = (SELECT source FROM record_source_by_register_time WHERE register_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1) AND register_date = '"+settings.str_yesterday+"'"
        sql4 = "SELECT COUNT(id) FROM users WHERE out_put_source = (SELECT source FROM record_source_by_register_time WHERE register_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1) AND register_date = '"+settings.str_yesterday+"' AND login_date = '"+settings.str_yesterday+"'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()

        self.assertEqual(res, 200)

        # 断言请求返回的数据跟数据库record_source_by_happen_time()查询数据是否一致
        self.assertEqual(result["UserSum"], dbo1[0])
        self.assertEqual(result["SumRegisterCount"], str(dbo1[1]))
        self.assertEqual(result["SumActiveCount"], str(dbo1[2]))
        self.assertEqual(result["SumH5Register"], str(dbo1[3]))
        self.assertEqual(result["Result"][0]["PageUv"], str(dbo2[0]))
        self.assertEqual(result["Result"][0]["RegisterCount"], str(dbo2[1]))
        self.assertEqual(result["Result"][0]["ActiveCount"], str(dbo2[2]))
        self.assertEqual(result["Result"][0]["H5Register"], str(dbo2[3]))

        # 断言请求返回数据跟数据库别的表查询数据是否一致
        self.assertEqual(result["Result"][0]["RegisterCount"], str(dbo3[0]))
        self.assertEqual(result["Result"][0]["ActiveCount"], str(dbo4[0]))

    def test_006_single_channel_statistics_happen_time(self):
        """推广-渠道数据-单渠道统计-按发生日期"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 6, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 6, 6).get_body()

        payloads.update(StartDate=settings.str_yesterday, EndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT SUM(rr.register_count), SUM(rr.active_count), SUM(rr.h5_register) FROM source AS s LEFT JOIN record_source_by_happen_time AS rr ON rr.source = s.source LEFT JOIN company AS c ON s.company_id = c.id WHERE rr.happen_date = '"+settings.str_yesterday+"'"
        sql2 = "SELECT page_uv, register_count, active_count, h5_register FROM record_source_by_happen_time WHERE happen_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1"
        sql3 = "SELECT COUNT(id) FROM users WHERE out_put_source = (SELECT source FROM record_source_by_register_time WHERE register_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1) AND register_date = '"+settings.str_yesterday+"'"
        sql4 = "SELECT COUNT(id) FROM users WHERE out_put_source = (SELECT source FROM record_source_by_register_time WHERE register_date = '"+settings.str_yesterday+"' ORDER BY id LIMIT 1) AND login_date = '"+settings.str_yesterday+"'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()

        self.assertEqual(res, 200)

        # 断言请求返回的数据跟数据库record_source_by_happen_time()查询数据是否一致
        self.assertEqual(result["SumRegisterCount"], str(dbo1[0]))
        self.assertEqual(result["SumActiveCount"], str(dbo1[1]))
        self.assertEqual(result["SumH5Register"], str(dbo1[2]))
        self.assertEqual(result["Result"][0]["PageUv"], str(dbo2[0]))
        self.assertEqual(result["Result"][0]["RegisterCount"], str(dbo2[1]))
        self.assertEqual(result["Result"][0]["ActiveCount"], str(dbo2[2]))
        self.assertEqual(result["Result"][0]["H5Register"], str(dbo2[3]))

        # 断言请求返回数据跟数据库别的表查询数据是否一致
        self.assertEqual(result["Result"][0]["RegisterCount"], str(dbo3[0]))
        self.assertEqual(result["Result"][0]["ActiveCount"], str(dbo4[0]))

    def test_007_single_channel_statistics_search_company(self):
        """推广-渠道数据-单渠道统计-公司搜索(按注册日期统计)"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 7, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 7, 6).get_body()

        payloads.update(StartDate=settings.str_yesterday, EndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(rr.id) FROM source AS s LEFT JOIN record_source_by_register_time AS rr ON rr.source = s.source LEFT JOIN company AS c ON s.company_id = c.id WHERE rr.register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_yesterday+"' AND c. name = '多选科技'"
        sql2 = "SELECT SUM(rr.register_count), SUM(rr.active_count), SUM(rr.h5_register) FROM source AS s LEFT JOIN record_source_by_register_time AS rr ON rr.source = s.source LEFT JOIN company AS c ON s.company_id = c.id WHERE rr.register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_yesterday+"' AND c. name = '多选科技'"
        # sql4 = "SELECT COUNT(id) FROM `users` WHERE register_date = '" + settings.str_yesterday + "'"
        # sql3 = "SELECT c.name, rr.source, rr.page_uv, rr.register_count, rr.active_count, rr.h5_register, rr.register_date FROM source AS s LEFT JOIN record_source_by_register_time AS rr ON rr.source = s.source LEFT JOIN company AS c ON s.company_id = c.id WHERE rr.register_date BETWEEN '" + settings.str_yesterday + "' AND '" + settings.str_yesterday + "' AND c. name = '多选科技'"
        sql5 = "SELECT COUNT(*) FROM source AS so LEFT JOIN company AS co ON so.company_id=co.id LEFT JOIN users AS u ON so.source=u.out_put_source WHERE u.register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_yesterday+"' AND co.name='多选科技'"
        sql6 = "SELECT COUNT(*) FROM source AS so LEFT JOIN company AS co ON so.company_id=co.id LEFT JOIN users AS u ON so.source=u.out_put_source WHERE u.register_date = u.login_date AND u.register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_yesterday+"' AND co.name='多选科技'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo5 = DbOperate(sql5).db_operate()
        dbo6 = DbOperate(sql6).db_operate()

        self.assertEqual(res, 200)

        # 断言请求返回的数据跟数据库record_source_by_register_time()查询数据是否一致
        self.assertEqual(result["UserSum"], dbo1[0])
        self.assertEqual(result["SumRegisterCount"], str(dbo2[0]))
        self.assertEqual(result["SumActiveCount"], str(dbo2[1]))
        self.assertEqual(result["SumH5Register"], str(dbo2[2]))

        # 断言请求返回数据跟数据库别的表查询数据是否一致
        self.assertEqual(result["SumRegisterCount"], str(dbo5[0]))
        self.assertEqual(result["SumActiveCount"], str(dbo6[0]))

    def test_008_single_channel_statistics_search_company_source(self):
        """推广-渠道数据-单渠道统计-渠道名称搜索"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 8, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 8, 6).get_body()

        payloads.update(StartDate=settings.str_eightDays, EndDate=settings.str_yesterday)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT SUM(register_count), SUM(active_count), SUM(h5_register) FROM record_source_by_register_time WHERE register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_today+"' AND source = '电销5'"
        sql2 = "SELECT COUNT(*) FROM users WHERE register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_today+"' AND out_put_source = '电销5'"
        sql3 = "SELECT COUNT(*) FROM users WHERE register_date = login_date AND register_date BETWEEN '"+settings.str_eightDays+"' AND '"+settings.str_today+"' AND out_put_source = '电销5'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()

        self.assertEqual(res, 200)
        # 判断record_source_by_register_time表与users表 数据是否相等
        self.assertEqual(str(dbo1[0]), str(dbo2[0]))
        self.assertEqual(str(dbo1[1]), str(dbo3[0]))

    def test_009_active_summary_default(self):
        """推广-渠道数据-激活汇总-默认页面"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 9, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 9, 6).get_body()

        payloads.update(StartDate=settings.str_thirtyDays, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users WHERE register_date='"+settings.str_tenDays+"'"
        sql2 = "SELECT COUNT(*) FROM users WHERE login_date='"+settings.str_tenDays+"'"
        # day1
        sql3 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_nineDays+"'"
        # day2
        sql4 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_eightDays+"'"
        # day3
        sql5 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_sevenDays+"'"
        # day4
        sql6 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_sixDays+"'"
        # day5
        sql7 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_fiveDays+"'"
        # day6
        sql8 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_fourDays+"'"
        # day7
        sql9 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_theDayBeforeYesterday+"'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()
        dbo5 = DbOperate(sql5).db_operate()
        dbo6 = DbOperate(sql6).db_operate()
        dbo7 = DbOperate(sql7).db_operate()
        dbo8 = DbOperate(sql8).db_operate()
        dbo9 = DbOperate(sql9).db_operate()

        self.assertEqual(res, 200)
        # 判断10天前(今天-9天)的数据是否正确
        self.assertEqual(result["List1"][7]["RegisterCount"], dbo1[0])
        self.assertEqual(result["List1"][7]["ActiveCount"], dbo2[0])
        self.assertEqual(result["List1"][7]["Day1"], dbo3[0])
        self.assertEqual(result["List1"][7]["Day2"], dbo4[0])
        self.assertEqual(result["List1"][7]["Day3"], dbo5[0])
        self.assertEqual(result["List1"][7]["Day4"], dbo6[0])
        self.assertEqual(result["List1"][7]["Day5"], dbo7[0])
        self.assertEqual(result["List1"][7]["Day6"], dbo8[0])
        self.assertEqual(result["List1"][7]["Day7"], dbo9[0])

    def test_010_active_summary_source_name(self):
        """推广-渠道数据-激活汇总-渠道名称"""
        logger.logger.logger.debug('当前方法：%s' % p.get_current_function_name())
        Token = read_token.re_token()

        url = ReadExcel(EXCEL_PATH, 'channel_summary_details', 10, 3).get_url()
        payloads = ReadExcel(EXCEL_PATH, 'channel_summary_details', 10, 6).get_body()

        payloads.update(StartDate=settings.str_thirtyDays, EndDate=settings.str_today)

        result = post_request(url, payloads, Token)
        res = result["Ret"]
        logger.logger.logger.debug('是测试点"%s"下的用例"%s"，返回的结果res=%s]' % (
            self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))

        sql1 = "SELECT COUNT(*) FROM users WHERE register_date='"+settings.str_tenDays+"' AND out_put_source = '电销5'"
        sql2 = "SELECT COUNT(*) FROM users WHERE login_date='"+settings.str_tenDays+"' AND out_put_source = '电销5'"
        # day1
        sql3 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_nineDays+"' AND u.out_put_source = '电销5'"
        # day2
        sql4 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_eightDays+"' AND u.out_put_source = '电销5'"
        # day3
        sql5 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_sevenDays+"' AND u.out_put_source = '电销5'"
        # day4
        sql6 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_sixDays+"' AND u.out_put_source = '电销5'"
        # day5
        sql7 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_fiveDays+"' AND u.out_put_source = '电销5'"
        # day6
        sql8 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_fourDays+"' AND u.out_put_source = '电销5'"
        # day7
        sql9 = "SELECT count(DISTINCT u.id) FROM users as u LEFT JOIN login_record as lr ON u.id=lr.uid WHERE u.register_date = '"+settings.str_tenDays+"' AND lr.create_date = '"+settings.str_theDayBeforeYesterday+"' AND u.out_put_source = '电销5'"

        dbo1 = DbOperate(sql1).db_operate()
        dbo2 = DbOperate(sql2).db_operate()
        dbo3 = DbOperate(sql3).db_operate()
        dbo4 = DbOperate(sql4).db_operate()
        dbo5 = DbOperate(sql5).db_operate()
        dbo6 = DbOperate(sql6).db_operate()
        dbo7 = DbOperate(sql7).db_operate()
        dbo8 = DbOperate(sql8).db_operate()
        dbo9 = DbOperate(sql9).db_operate()

        self.assertEqual(res, 200)
        # 判断10天前(今天-9天)的数据是否正确
        self.assertEqual(result["List1"][7]["RegisterCount"], dbo1[0])
        self.assertEqual(result["List1"][7]["ActiveCount"], dbo2[0])
        self.assertEqual(result["List1"][7]["Day1"], dbo3[0])
        self.assertEqual(result["List1"][7]["Day2"], dbo4[0])
        self.assertEqual(result["List1"][7]["Day3"], dbo5[0])
        self.assertEqual(result["List1"][7]["Day4"], dbo6[0])
        self.assertEqual(result["List1"][7]["Day5"], dbo7[0])
        self.assertEqual(result["List1"][7]["Day6"], dbo8[0])
        self.assertEqual(result["List1"][7]["Day7"], dbo9[0])
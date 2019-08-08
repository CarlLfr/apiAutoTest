#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
# @Author  : Liufeiru

from conf.settings import EXCEL_PATH

import xlrd

class ReadExcel():
    def __init__(self, excelPath, sheetName, rowIndex, colIndex):
        # 获取数据
        self.data = xlrd.open_workbook(excelPath)
        # 通过worksheet名称获取sheet数据
        self.table = self.data.sheet_by_name(sheetName)

        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

        # 行索引
        self.rowIndex = rowIndex
        # 列索引
        self.colIndex = colIndex

    def get_body(self):
        """获取body值"""
        cell_value = self.table.cell(self.rowIndex, self.colIndex).value
        # eval将str转换成dict
        return eval(cell_value)

    def get_url(self):
        """获取url"""
        return self.table.cell(self.rowIndex, self.colIndex).value

if __name__ == '__main__':
    r = ReadExcel(EXCEL_PATH, 'Sheet1', 1, 3)
    v = r.get_url()
    print(v)
    print(type(v))

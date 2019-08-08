#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
# @Author  : Liufeiru

import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import pymysql
import datetime
from conf.settings import DB_USERNAME
from conf.settings import DB_PASSWORD
from conf.settings import DB_IP
from conf.settings import PORT
from conf.settings import DB

class DbOperate(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, sql):
        self.username = DB_USERNAME
        self.password = DB_PASSWORD
        self.ip = DB_IP
        self.port = PORT
        self.db = DB
        self.sql = sql.strip().lower()

    def db_operate(self):
        # 连接数据库
        try:
            self.conn = pymysql.connect(host=self.ip, port=self.port, user=self.username, passwd=self.password, db=self.db, charset="utf8")
        except Exception as e:
            return {'code': '12306', 'msg': '数据库连接异常>>>%s' % e}

        self.cur = self.conn.cursor()

        try:
            self.cur.execute(self.sql)
        except Exception as e:
            return {'code': '12307', 'msg': 'sql错误>>>%s' % e}
        else:
            if self.sql.startswith('select'):
                ret = self.cur.fetchone()
            else:
                if self.sql.startswith('delete') and self.sql.count('=') != 1:
                    return {'code': '12308', 'msg': 'delete操作必须带where条件，一次只能删除一条数据'}
                elif self.sql.startswith('update') and self.sql.count('=') != 1:
                    return {'code': '12309', 'msg': 'update操作必须带where条件，一次只能删除一条数据'}
                elif self.sql.startswith('create') or self.sql.startswith('alter') or self.sql.startswith('drop') or self.sql.startswith('truncate'):
                    return {'code': '12310', 'msg': '只能进行select/update/insert/delete操作'}
                else:
                    self.conn.commit()
                    ret = {'code': '12200', 'msg': '数据操作成功'}
            return ret
        finally:
            self.cur.close()
            self.conn.close()

    def db_operate_fetchall(self):
        # 连接数据库
        try:
            self.conn = pymysql.connect(host=self.ip, port=self.port, user=self.username, passwd=self.password, db=self.db, charset="utf8")
        except Exception as e:
            return {'code': '12306', 'msg': '数据库连接异常>>>%s' % e}

        self.cur = self.conn.cursor()

        try:
            self.cur.execute(self.sql)
        except Exception as e:
            return {'code': '12307', 'msg': 'sql错误>>>%s' % e}
        else:
            if self.sql.startswith('select'):
                ret = self.cur.fetchall()
            else:
                if self.sql.startswith('delete') and self.sql.count('=') != 1:
                    return {'code': '12308', 'msg': 'delete操作必须带where条件，一次只能删除一条数据'}
                elif self.sql.startswith('update') and self.sql.count('=') != 1:
                    return {'code': '12309', 'msg': 'update操作必须带where条件，一次只能删除一条数据'}
                elif self.sql.startswith('create') or self.sql.startswith('alter') or self.sql.startswith('drop') or self.sql.startswith('truncate'):
                    return {'code': '12310', 'msg': '只能进行select/update/insert/delete操作'}
                else:
                    self.conn.commit()
                    ret = {'code': '12200', 'msg': '数据操作成功'}
            return ret
        finally:
            self.cur.close()
            self.conn.close()

if __name__ == '__main__':
    today = datetime.date.today()
    str_today = str(today)
    str_theDayBeforeYesterday = str(today - datetime.timedelta(days=2))

    sql = "select uid from users_info where id_name = '刘斐汝'"
    ret = DbOperate(sql).db_operate()
    print(ret)
    print(type(ret))




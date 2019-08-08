#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/05
# @Author  : Liufeiru

import requests
import json

# 定义get请求方法
def get_request(url, params):
    try:
        response = requests.get(url, params=params)
        # response.raise_for_status()
        return response
    except TimeoutError:
        # logger.error("Time out!")
        return None

# 封装用户-用户管理模块list接口请求
def post_request(url, payloads, token):
    # 将获取的token加入payloads
    payloads.update(Token=token)
    # 字典转换成json
    data = json.dumps(payloads)

    try:
        res = requests.post(url, data=data).json()
    except Exception as e:
        res = {'code': '911', 'msg': '连接错误，错误原因为：%s' % e}
    return res

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/04
# @Author  : Liufeiru

"""读取yaml中的数据"""

import yaml
from conf.settings import TOKEN_PATH

def re_token():
    # 从token.yaml文件中读取token值
    with open(TOKEN_PATH, 'r') as f:
        result = yaml.load(f)
        return result["Token"]

if __name__ == '__main__':
    print(re_token())
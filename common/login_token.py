#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/07/04
# @Author  : Liufeiru

"""通过登录接口获取token，并写入yaml文件"""
import json
import requests
from ruamel import yaml
from conf.settings import TOKEN_PATH

class TokenToYaml(object):
    def __init__(self):
        self.login_url = "https://admin.myjhtech.com/v1/account/login"
        self.VerifyCode = input("请输入谷歌验证码：")
        self.token_path = TOKEN_PATH

    # 请求管理后台登录接口获取Token
    def login_get_token(self):
        payload = {
            "Account": "liufr",
            "VerifyCode": self.VerifyCode
        }
        try:
            resp = requests.post(url=self.login_url, data=json.dumps(payload))
            token = resp.json()["Token"]
        except Exception as e:
            print(e)

        # 将获取的token写入token.yaml文件
        dic = {'Token': token}
        self.write_to_yaml(self.token_path, dic)

    # 写入yaml文件方法
    def write_to_yaml(self, yamlpath, data):
        try:
            with open(yamlpath, "w", encoding="utf-8") as f:
                yaml.dump(data, f, Dumper=yaml.RoundTripDumper)
        except Exception as e:
            print("token写入文件失败，原因是：%s" % e)

if __name__ == '__main__':
    token = TokenToYaml()
    token.login_get_token()
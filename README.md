## 项目简介

这是一个基于已有的接口自动化测试框架写成的项目，用于公司项目管理后台的回归性测试。整个项目由requests + unittest + logging + pymysql + xlrd + BeautifulReport + smtplib + email模块组成， 测试用例在excel文件中，能连数据库查询。 项目需要在后续的使用中进一步优化，目前尚未使用jenkins做集成，后续打算结合jenkins做成持续集成

## 项目依赖
获取token值。方法：请求登录接口（账号 + 谷歌验证码）——>返回token值——>写入yaml文件——>执行测试用例、读取yaml文件中的token（其他接口请求时token需作为请求参数）

1.该项目为线上管理后台项目，接口请求参数需要加入token值，通过登录获取token值

2.获取token值的方法说明。登录时需要输入 账号+谷歌验证码，所以项目运行后需输入对应账号绑定的谷歌验证码，请求登录接口获取token值，再写入common中的token.yaml文件

3.后续脚本执行测试用例（即请求接口）时，通过读取token.yaml文件获取token值

## 环境配置

python3.6 + requests + unittest + pymysql + HTMLTestRunner + os + sys + json + time + redis

1.Python3.6，解释器环境

2.requests，模拟用户发送http协议get或者post类型请求

3.unittest，组织运行测试用例

4.pymysql，操作数据库

5.HTMLTestRunner，生成html格式报告模板

6.os，获取路径

7.sys，设置环境变量

8.json，根据项目需要，发送请求前先将请求参数由dict转换成json

9.time，时间戳，生成的报告名称是：time_report.html

10.smtplib,email，发送邮件

## 功能实现

1.用例数据分离

2.接口依赖

3.连接数据库查询

4.自动生成测试报告

5.自动发送测试邮件

## 框架目录结构

1.bin 中的run.py为测试用例运行入口

2.common 中主要放公共方法，日志模块、项目请求函数、读取excel文件、读写token、发送邮件、读取当前类、方法、行的tool等，测试用例存放在testcast_date.xlsx中

3.conf 中的settings.py放文件路径、数据库地址、接口信息、日期、邮箱等数据

4.db_operate 中的mysql_operate.py存放mysql数据库操作方法

5.log 中存放项目执行过程中的日志信息

6.test_case 中存放每个接口的测试脚本

7.report 中存放测试报告

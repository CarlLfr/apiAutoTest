# 项目简介
这是一个基于已有的接口自动化测试框架写成的项目，用于公司项目管理后台的回归性测试。整个项目由requests + unittest + logging + pymysql + xlrd + BeautifulReport + smtplib + email模块组成， 测试用例在excel文件中，能连数据库查询。 项目需要在后续的使用中进一步优化，目前尚未使用jenkins做集成，后续打算结合jenkins做成持续集成

# 环境配置
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

# 功能实现
1.用例数据分离
2.接口依赖
3.连接数据库查询
4.自动生成测试报告
5.自动发送测试邮件

# 框架目录结构
1.bin 中的run.py为测试用例运行入口
2.common 中主要放公共方法，日志模块、项目请求函数、读取excel文件、读写token、发送邮件、读取当前类、方法、行的tool等，测试用例存放在testcast_date.xlsx文件中
3.conf 中的settings.py文件放文件路径、数据库地址、接口信息、日期、邮箱等数据
4.db_operate 中的mysql_operate.py存放mysql数据库操作方法
5.log 文件夹存放项目执行过程中的日志信息
6.test_case 文件夹存放每个接口的测试脚本
7.report 文件夹存放测试报告

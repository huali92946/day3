# 1导包
import unittest
from tools.HTMLTestRunner import HTMLTestRunner

# 2定义测试套件
suite = unittest.defaultTestLoader.discover("./scripts", pattern="test*.py")

# 3获取报告存储路径文件流并实例化HTMLTestRunner,调用run执行套件
with open("./report/ihrm_report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)

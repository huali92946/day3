# 1. 导包
import unittest
import api
from parameterized import parameterized

# 2. 新建测试类 继承 unittest.TestCase
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestLogin(unittest.TestCase):
    # 1. 初始化
    def setUp(self) -> None:
        # 获取ApiLogin对象
        self.login = ApiLogin()  # 注意：实例化需要括号

    # 2. 登录测试接口方法
    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, mobile, password):
        # 调用登录接口
        result = self.login.api_login(mobile, password)
        print("登录结果：", result.json())
        r = result.json()
        # 断言
        assert_common(self, result)
        # 提取token
        token = r.get("data")
        log.info("正在提取token：{}".format(token))
        # 追加到公共变量 headers
        api.headers['Authorization'] = "Bearer " + token
        print("追加token后的headers为：", api.headers)

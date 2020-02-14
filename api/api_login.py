import api
import requests
from tools.get_log import GetLog

# 获取日志器
log = GetLog.get_logger()


class ApiLogin:
    # 1. 初始化
    def __init__(self):
        # 组装 登录url
        self.url_login = api.host + "/api/sys/login"
        # 日志
        log.info("正在初始化登录url：{}".format(self.url_login))

    # 2. 登录接口封装
    def api_login(self, mobile, password):
        # 1. 定义测试数据
        data = {"mobile": mobile, "password": password}
        # 日志
        log.info("正在初始化登录数据：{} 请求信息头：{}".format(data, api.headers))
        # 2. 调用post方法 注意：一定要将响应对象返回
        return requests.post(url=self.url_login, json=data, headers=api.headers)

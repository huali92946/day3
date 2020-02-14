from tools.get_log import GetLog

log = GetLog.get_logger()


def assert_common(self, response,
                  status_code=200,
                  success=True,
                  message="操作成功！",
                  code=10000):
    """
    :param self: TestCase实例
    :param response: 响应对象
    """
    try:
        r = response.json()
        # 断言
        # 1. 断言状态吗 200
        self.assertEqual(status_code, response.status_code)
        # 2. 断言 success true
        self.assertEqual(success, r.get("success"))
        # 3. 断言 code 10000
        self.assertEqual(code, r.get("code"))
        # 4. 断言 msg
        self.assertEqual(message, r.get("message"))
    except Exception as e:
        # 日志
        log.error(e)
        # 抛异常
        raise

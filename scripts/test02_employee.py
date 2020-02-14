import unittest
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.get_log import GetLog
from parameterized import parameterized
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestEmployee(unittest.TestCase):
    # 1. 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        # 获取ApiEmployee对象
        cls.api = ApiEmployee()

    # 2. 新增员工 接口测试方法
    @parameterized.expand(read_yaml("employee_post.yaml"))
    def test01_post(self, username, mobile, worNumber):
        # 调用新增员工接口
        r = self.api.api_post_employee(username, mobile, worNumber)
        # 断言
        assert_common(self, r)
        print("新增员工结果：", r.json())
        log.info("新增员工结果为：{}".format(r.json()))
        # 提取 user_id
        api.user_id = r.json().get("data").get("id")
        print("员工user_id值为：", api.user_id)
        log.info("新增员工后提取的员工id为：：{}".format(api.user_id))

    # 3. 更新员工 接口测试方法
    def test02_put(self):
        # 1. 调用更新接口
        r = self.api.api_put_employee()
        log.info("更新员工结果为：{}".format(r.json()))
        # 2. 断言
        assert_common(self, r)

    # 4. 查询员工 接口测试方法
    def test03_get(self):
        # 1. 调用查询接口
        r = self.api.api_get_employee()
        log.info("查询员工结果为：{}".format(r.json()))
        # 2. 断言
        assert_common(self, r)

    # 5. 删除员工 接口测试方法
    def test04_delete(self):
        # 调用删除员工接口
        r = self.api.api_delete_employee()
        log.info("删除员工结果为：{}".format(r.json()))
        # 断言
        assert_common(self, r)

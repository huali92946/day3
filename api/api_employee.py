import api
import requests
from tools.get_log import GetLog
log = GetLog.get_logger()


class ApiEmployee:
    # 1. 初始化
    def __init__(self):
        # 新增员工 url
        self.url_post = api.host + "/api/sys/user"
        # 修改员工 url
        self.url_put = api.host + "/api/sys/user/{}"
        # 查询员工 url
        self.url_get = api.host + "/api/sys/user/{}"
        # 删除员工 url
        self.url_delete = api.host + "/api/sys/user/{}"

        log.info("新增员工url: {}".format(self.url_post))
        log.info("删除、更新、查询url：{}".format(self.url_delete))

    # 2. 新增员工
    def api_post_employee(self, username, mobile, workNumber):
        # 1. 参数数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}
        log.info("新增员工数据：{} 新增员工请求信息头：{}".format(data, api.headers))
        # 2. 调用post方法 ->返回响应对象    注意：json接受参数
        return requests.post(url=self.url_post, json=data, headers=api.headers)

    # 3. 修改员工
    def api_put_employee(self):
        # 1. 参数数据
        data = {"username": "yinjian1"}
        # 2. 调用put方法 ->返回响应对象
        return requests.put(url=self.url_put.format(api.user_id), json=data, headers=api.headers)

    # 4. 查询员工
    def api_get_employee(self):
        # 1. 调用get方法 ->返回响应对象   注意：当前headers中存在 Content-Type不影响使用
        return requests.get(url=self.url_get.format(api.user_id), headers=api.headers)

    # 5. 删除员工
    def api_delete_employee(self):
        log.info("删除员工请求信息头：{}".format(api.headers))
        # 1. 调用delete方法 ->返回响应对象
        return requests.delete(url=self.url_delete.format(api.user_id), headers=api.headers)

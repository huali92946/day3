import yaml
from config import base_url
import os


def read_yaml(filename):
    # 1.获取数据文件流
    with open(base_url + os.sep + "data" + os.sep + filename, "r", encoding="utf-8") as f:
        arr = []
        # 调用方法解析 文件流
        for data in yaml.safe_load(f).values():
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    print(read_yaml("login.yaml"))
    """
        参数化引用的格式：[(),()]
    """
    print("--" * 50)
    # 1.遍历 拿取 {"mobile":...}
    # arr = []
    # for data in read_yaml().values():
    #     arr.append(tuple(data.values()))
    # print(arr)

    print(base_url)
    print(base_url + os.sep + "data" + os.sep + "login.yaml")
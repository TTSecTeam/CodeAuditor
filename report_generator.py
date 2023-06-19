'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:29
@Author:尘心||rocky
'''


class ReportGenerator:
    def generate(self, errors):
        # 遍历错误信息并打印
        for error in errors:
            print(f"文件: {error['file']}")
            print(f"错误: {error['error']}")
            print(f"代码: {error['code']}")
            print("------------------------")

'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:29
@Author:尘心||rocky
'''


class ReportGenerator:
    def generate(self, errors):
        for lineno, error in errors:
            print(f"行 {lineno}: {error}")

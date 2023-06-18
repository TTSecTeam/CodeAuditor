'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import ast

class CodeParser:
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.tree = ast.parse(file.read())

'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import os
import ast

class CodeParser:
    def __init__(self, directory):
        self.trees = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith('.py'):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        self.trees.append(ast.parse(file.read()))


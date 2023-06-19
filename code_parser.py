'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import os
import ast

import ast
import os

class CodeParser:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    @property
    def trees(self):
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.py'):
                    with open(os.path.join(root, file), 'r') as f:
                        code = f.read()
                        try:
                            # Parse the code and yield the file path and the AST
                            yield os.path.join(root, file), ast.parse(code)
                        except SyntaxError as e:
                            print(f"语法错误在文件 {os.path.join(root, file)}: {e}")



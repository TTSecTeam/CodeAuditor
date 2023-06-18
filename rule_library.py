'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import ast

class Rule:
    def check(self, node):
        pass

class ImportRule(Rule):
    def check(self, node):
        if isinstance(node, ast.Import):
            if any(alias.name == "os" for alias in node.names):
                return "不应直接导入 'os' 模块"
        return None

class FunctionDefRule(Rule):
    def check(self, node):
        if isinstance(node, ast.FunctionDef):
            if len(node.body) == 0:
                return "函数定义不能为空"
        return None

class DangerousFunctionRule(Rule):
    def check(self, node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in ['eval', 'exec']:
                    return "请避免使用 'eval' 或 'exec' 函数"
        return None

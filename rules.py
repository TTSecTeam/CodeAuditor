'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 13:50
@Author:尘心||rocky
'''

import ast

# 未使用的变量规则
class UnusedVariableRule:
    def check(self, node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and '_' == target.id[0]:
                    return f"未使用的变量：{ast.unparse(target)}"
        return None

# 类型不匹配规则
class TypeErrorRule:
    def check(self, node):
        if isinstance(node, ast.Compare):
            left = node.left
            for comparator in node.comparators:
                if type(left) != type(comparator):
                    return f"类型不匹配：{ast.unparse(node)}"
        return None

# 异常处理不全规则
class ExceptionNotHandledRule:
    def check(self, node):
        if isinstance(node, ast.Try):
            if not node.handlers:
                return f"异常未被处理：{ast.unparse(node)}"
        return None

# 确保使用安全函数
class InsecureFunctionRule:
    insecure_functions = ['eval', 'exec', 'input']

    def check(self, node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in self.insecure_functions:
            return f"使用不安全的函数：{ast.unparse(node)}"
        return None


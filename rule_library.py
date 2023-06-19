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

# 定义 EvalUsageRule
class EvalUsageRule:
    def check(self, node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'eval':
            return f"使用了 eval() 函数：{ast.unparse(node)}"
        return None


class UnusedVariableRule:
    def __init__(self):
        self.names = set()

    def check(self, node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.names.add(target.id)
        elif isinstance(node, ast.Name):
            if node.id in self.names:
                self.names.remove(node.id)
        elif isinstance(node, ast.FunctionDef):
            for arg in node.args.args:
                if isinstance(arg, ast.arg):
                    self.names.add(arg.arg)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                self.names.add(node.target.id)
        return None

    def final_check(self):
        if self.names:
            return f"检测到未使用的变量：{', '.join(self.names)}"
        return None


class TypeErrorRule:
    def check(self, node):
        if isinstance(node, ast.Call):
            # 假设我们想检查所有没有明确类型声明的函数调用
            if not isinstance(node.func, ast.Attribute) and not isinstance(node.func, ast.Name):
                return f"存在可能的类型错误：{ast.unparse(node)}"
        return None


class ExceptionNotHandledRule:
    def check(self, node):
        if isinstance(node, ast.Raise):
            if not any(isinstance(n, ast.ExceptHandler) for n in ast.walk(node)):
                return f"检测到未处理的异常：{ast.unparse(node)}"
        return None


class InsecureFunctionRule:
    insecure_functions = ['exec', 'eval', 'open']

    def check(self, node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in self.insecure_functions:
            return f"检测到使用了不安全的函数：{node.func.id}"
        return None
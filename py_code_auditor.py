'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/18 22:38
@Author:尘心||rocky
'''


import ast
import sys

# 规则库
class RuleLibrary:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

# 规则
class Rule:
    def check(self, node):
        pass

class ImportRule(Rule):
    def check(self, node):
        if isinstance(node, ast.Import):
            if any(alias.name == "os" for alias in node.names):
                return "不应直接导入 'os' 模块"
        return None

# 规则执行引擎
class RuleEngine(ast.NodeVisitor):
    def __init__(self, rules):
        self.rules = rules
        self.errors = []

    def visit(self, node):
        for rule in self.rules:
            error = rule.check(node)
            if error:
                self.errors.append((node.lineno, error))
        self.generic_visit(node)

# 报告生成器
class ReportGenerator:
    def generate(self, errors):
        for lineno, error in errors:
            print(f"行 {lineno}: {error}")

# CLI
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"用法: python {sys.argv[0]} <代码文件路径>")
        sys.exit(1)

    # 创建规则库并添加规则
    library = RuleLibrary()
    library.add_rule(ImportRule())

    # 创建规则执行引擎并加载规则库
    engine = RuleEngine(library.rules)

    # 解析代码文件并执行规则
    with open(sys.argv[1], "r") as file:
        tree = ast.parse(file.read())
    engine.visit(tree)

    # 生成和打印报告
    report_generator = ReportGenerator()
    report_generator.generate(engine.errors)

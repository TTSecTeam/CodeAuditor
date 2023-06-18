'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/18 21:32
@Author:尘心||rocky
'''


import ast
import sys

class CodeAuditor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_Import(self, node):
        # 示例规则: 检查是否导入了os模块
        if any(alias.name == "os" for alias in node.names):
            self.errors.append((node.lineno, "不应直接导入 'os' 模块"))
        self.generic_visit(node)

    def report(self):
        for lineno, error in self.errors:
            print(f"行 {lineno}: {error}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"用法: python {sys.argv[0]} <代码文件路径>")
        sys.exit(1)

    with open(sys.argv[1], "r") as file:
        tree = ast.parse(file.read())

    auditor = CodeAuditor()
    auditor.visit(tree)
    auditor.report()

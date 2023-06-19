'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:28
@Author:尘心||rocky
'''

import ast

class RuleEngine(ast.NodeVisitor):
    def __init__(self, rules):
        self.rules = rules
        self.errors = []
        self.current_file = ''

    def visit(self, tree):
        # 前序遍历 AST
        super().visit(tree)

    def check(self, node):
        # 检查当前节点是否违反了规则
        for rule in self.rules:
            error = rule.check(node)
            if error is not None:
                # 将错误信息，文件路径和有问题的代码部分一起记录下来
                self.errors.append({
                    'file': self.current_file,
                    'error': error,
                    'code': ast.unparse(node),
                })

    def process_file(self, file, tree):
        # 记录当前处理的文件路径
        self.current_file = file
        self.visit(tree)


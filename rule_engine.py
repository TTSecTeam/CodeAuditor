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

    def visit(self, node):
        for rule in self.rules:
            error = rule.check(node)
            if error:
                self.errors.append((node.lineno, error))
        self.generic_visit(node)

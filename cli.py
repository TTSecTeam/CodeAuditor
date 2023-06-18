'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import sys
from code_parser import CodeParser
from rule_engine import RuleEngine
from report_generator import ReportGenerator
from rule_library import ImportRule, FunctionDefRule

def main():
    if len(sys.argv) != 2:
        print(f"用法: python -m py_code_auditor.cli <代码文件路径>")
        sys.exit(1)

    # 创建规则库并添加规则
    rules = [ImportRule(), FunctionDefRule()]

    # 创建规则执行引擎并加载规则库
    engine = RuleEngine(rules)

    # 解析代码文件并执行规则
    parser = CodeParser(sys.argv[1])
    engine.visit(parser.tree)

    # 生成和打印报告
    report_generator = ReportGenerator()
    report_generator.generate(engine.errors)


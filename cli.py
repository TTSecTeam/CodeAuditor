'''
coding:utf-8
@Software:PyCharm
@Time:2023/6/19 07:27
@Author:尘心||rocky
'''

import sys
import logging
from tqdm import tqdm
from code_parser import CodeParser
from rule_engine import RuleEngine
from report_generator import ReportGenerator
from rule_library import ImportRule, FunctionDefRule, DangerousFunctionRule


def main():
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 2:
        print(f"用法: python -m cli <代码目录>")
        sys.exit(1)

    # 创建规则库并添加规则
    logging.info("创建规则库...")
    rules = [ImportRule(), FunctionDefRule(), DangerousFunctionRule()]

    # 创建规则执行引擎并加载规则库
    logging.info("创建规则执行引擎...")
    engine = RuleEngine(rules)

    # 解析代码目录并执行规则
    logging.info("开始解析和审计代码...")
    try:
        parser = CodeParser(sys.argv[1])
        for tree in tqdm(parser.trees, desc="审计进度"):
            engine.visit(tree)
    except Exception as e:
        logging.error(f"在代码审计过程中出错: {e}")
        sys.exit(1)

    # 生成和打印报告
    logging.info("生成报告...")
    report_generator = ReportGenerator()
    report_generator.generate(engine.errors)

    logging.info("完成代码审计。")

if __name__ == '__main__':
    main()




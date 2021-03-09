import unittest
from unittestreport import TestRunner
from common.handler_path import case_path,reports_path


print('哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈')

suit = unittest.defaultTestLoader.discover(case_path)
runner = TestRunner(suite=suit,
                 filename="report.html",
                 report_dir=reports_path,
                 title='测试报告',
                 tester='tester',
                 desc="测开项目测试生成的报告",
                 templates=1)
runner.run()
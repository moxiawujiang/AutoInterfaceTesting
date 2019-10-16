#coding:utf-8
import time
import HTMLReport
import unittest
from common.generate_test_case import GenerateTestCase

class TestRunner:
    def __init__(self):
        pass

    #生成测试用例集合
    def generate_test_suite(self):
        case_dir='test_cases'
        test_suite=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
        for cases in  discover:
            for case in cases:
                test_suite.addTest(case)

        return test_suite

    def run(self):
        report_name='report'+time.strftime('%y-%m-%d %H-%M-%S')
        runner=HTMLReport.TestRunner(output_path='test_report',report_file_name=report_name)
        my_suite=self.generate_test_suite()
        runner.run(my_suite)



if __name__ == '__main__':
    # 生成测试用例
    GenerateTestCase().create_case_files()
    #执行测试
    TestRunner().run()
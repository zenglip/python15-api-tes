import unittest
import HTMLTestRunnerNew
from API_0419.test_cases import test_login
from API_0419.common import contants
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromModule(test_login))

discover = unittest.defaultTestLoader.discover(contants.case_dir,'test_*.py')

with open(contants.report_dir+'/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='前程贷API',
                                              description='2019.0508')
    runner.run(discover)

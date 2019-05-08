#name
import unittest
import json
from ddt import *
from API_0419.common.do_excel import excel_practice
from API_0419.common.http_request import Http_Request2
from API_0419.common import contants
from API_0419.common import context
from API_0419.common import logger

logger = logger.get_logger(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel = excel_practice(contants.case_file, "login")
    cases = excel.read_excel()
    @classmethod#变成类方法，使全部用例执行完之后才生效
    def setUpClass(cls):
        logger.info('测试前置')
        cls.http_request = Http_Request2()

    @data(*cases)
    def test_login(self,case):
        logger.info('开始测试：{0}'.format(case.title))
        case.data = context.replace(case.data)  # 使用封装好的正则表达式替换数据
        resp = self.http_request.request(case.method,case.url,case.data)
        try:

            self.assertEqual(case.expected,resp.text)
            self.excel.write_excel(case.case_id+1,resp.text,"PASS")
        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, resp.text, "FAIL")
            logger.error('报错：{}'.format(e))
            raise e
        logger.info('结束测试：{0}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置')
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()

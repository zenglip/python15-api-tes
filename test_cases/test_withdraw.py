#name
import unittest
import json
from ddt import *
from API_0419.common.do_excel import excel_practice
from API_0419.common.http_request import Http_Request2
from API_0419.common import contants
from API_0419.common import context
@ddt
class LoginTest(unittest.TestCase):
    excel = excel_practice(contants.case_file, "withdraw")
    cases = excel.read_excel()
    @classmethod#变成类方法，使全部用例执行完之后才生效
    def setUpClass(cls):
        cls.http_request = Http_Request2()
    @data(*cases)
    def test_withdraw(self,case):
        case.data = context.replace(case.data)  # 使用封装好的正则表达式替换数据
        resp = self.http_request.request(case.method,case.url,case.data)
        actual_code = resp.json()["code"]
        #actual_code = int(actual_code),或者把actual转成整数也可以
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_excel(case.case_id+1,actual_code,"PASS")
            print("成功案例：", case.title)
        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, actual_code, "FAIL")
            print("失败案例：",case.title)
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()
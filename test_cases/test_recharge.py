#name
import unittest
import json
from ddt import *
from API_0419.common.do_excel import excel_practice
from API_0419.common.http_request import Http_Request2
from API_0419.common import contants
from API_0419.common import context
from API_0419.common.do_mysql import DoMysql
@ddt
class LoginTest(unittest.TestCase):
    excel = excel_practice(contants.case_file, "recharge")
    cases = excel.read_excel()
    @classmethod#变成类方法，使全部用例执行完之后才生效
    def setUpClass(cls):
        cls.http_request = Http_Request2()
        cls.mysql = DoMysql()
    @data(*cases)
    def test_recharge(self,case):
        #判断请求之前，是否需要执行sql
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print('before',type(member['LeaveAmount']),member['LeaveAmount'])
            before = member['LeaveAmount']
        case.data = context.replace(case.data)  # 使用封装好的正则表达式替换数据
        resp = self.http_request.request(case.method,case.url,case.data)
        actual_code = resp.json()["code"]
        #actual_code = int(actual_code),或者把actual转成整数也可以
        print(case.title)
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_excel(case.case_id + 1, actual_code, "PASS")
            #成功之后，再次判断是否需要执行sql
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print('after',type(member['LeaveAmount']),member['LeaveAmount'])
                after = member['LeaveAmount']
                self.assertEqual(before+int(eval(case.data)['amount']),after)
        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, actual_code, "FAIL")
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()
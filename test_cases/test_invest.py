import unittest
import json
from ddt import *
from API_0419.common.do_excel import excel_practice
from API_0419.common.http_request import Http_Request2
from API_0419.common import contants
from API_0419.common import context
from API_0419.common import do_mysql
from API_0419.common.context import  Context
@ddt
class InvestTest(unittest.TestCase):
    excel = excel_practice(contants.case_file, "invest")
    cases = excel.read_excel()
    @classmethod#变成类方法，使全部用例执行完之后才生效
    def setUpClass(cls):
        cls.http_request = Http_Request2()
        cls.mysql = do_mysql.DoMysql()
    @data(*cases)
    def test_invest(self,case):
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            print('before_LeaveAmount',self.mysql.fetch_one(sql)['LeaveAmount'])
            # print('before_LeaveAmount', self.mysql.fetch_one(sql))
            before_LeaveAmount = self.mysql.fetch_one(sql)['LeaveAmount']

        case.data = context.replace(case.data)  # 使用封装好的正则表达式替换数据
        resp = self.http_request.request(case.method,case.url,case.data)
        # print(resp.json())
        actual_code = resp.json()["code"]
        # print(resp.json())
        #actual_code = int(actual_code),或者把actual转成整数也可以
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_excel(case.case_id+1,actual_code,"PASS")
            print("成功案例：", case.title)
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                after_LeaveAmount = self.mysql.fetch_one(sql)['LeaveAmount']
                print('after_LeaveAmount',after_LeaveAmount)
                self.assertEqual(before_LeaveAmount - int(eval(case.data)['amount']), after_LeaveAmount)

            #判断加标成功后，查询数据库，得到loan_id
            if resp.json()['msg'] == '加标成功':
                sql = 'select id from future.loan where MemberID = 375 ORDER BY CreateTime DESC LIMIT 1;'
                loan_id = str(self.mysql.fetch_one(sql)['id'])
                setattr(Context,'loan_id',str(loan_id))
                # print("标ID:", type(Context.loan_id),Context.loan_id)
        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, actual_code, "FAIL")
            print("失败案例：",case.title)
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
if __name__ == '__main__':
    unittest.main()
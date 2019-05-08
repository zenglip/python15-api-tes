#name
import unittest
import json
from ddt import *
from API_0419.common.do_excel import excel_practice
from API_0419.common.http_request import Http_Request2
from API_0419.common import contants
from API_0419.common import do_mysql
from API_0419.common.config import config
from API_0419.common import context
@ddt
class LoginTest(unittest.TestCase):
    excel = excel_practice(contants.case_file, "register")
    cases = excel.read_excel()

    @classmethod#变成类方法，使全部用例执行完之后才生效
    def setUpClass(cls):
        cls.http_request = Http_Request2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_login(self,case):
        if case.data.find('register_mobilephone'):
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
            # sql = 'select max(mobilephone) from future.member'

                min_phone = self.mysql.fetch_one(sql)['max(mobilephone)'] # 查询最小手机号码
                # print(self.mysql.fetch_one(sql)['max(mobilephone)'])
                min_phone = int(min_phone) + 1
                min_phone = str(min_phone)
                print('min_phone',min_phone)
                case.data = case.data.replace('register_mobilephone', str(min_phone))
        # if case.data.find('normal_mobile'):
        #     normal_mobile = config.get('data', 'normal_mobile')
        #     case.data = case.data.replace('normal_mobile', str(normal_mobile))
        #
        # if case.data.find('normal_pwd'):
        #     normal_pwd = config.get('data', 'normal_pwd')
        #     case.data = case.data.replace('normal_pwd', str(normal_pwd))
        case.data = context.replace(case.data)#使用封装好的正则表达式替换数据
        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_excel(case.case_id+1,resp.text,"PASS")
            print('成功用例：', case.title)
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                after_min_phone = self.mysql.fetch_one(sql)['max(mobilephone)']
                print('after_min_phone',after_min_phone)
                self.assertEqual(int(min_phone),int(after_min_phone))
        except AssertionError as e:
            print(case.case_id)
            self.excel.write_excel(case.case_id + 1, resp.text, "FAIL")
            print("失败用例：",case.title)
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()

if __name__ == '__main__':
    unittest.main()
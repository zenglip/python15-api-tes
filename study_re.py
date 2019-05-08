#name
# import re
# from API_0419.common.config import config
# data = '{"mobilephone":"#normal_mobile#","pwd":"#normal_pwd#"}'
# # 原本字符
# # p = 'mobilephone'
# # m = re.search(p,data)
# # print(m)
# # 元字符
# p = "#(.*?)#"
# m = re.search(p,data)#找到第一个就返回
# print(m)
# print(type(m.group(1)),m.group(1))#返回表达式和组里面内容
# g = m.group(1)#返回指定组里面内容
#
# v = config.get('data',g)
# print(type(v),v)
# data_new = re.sub(p,v,data,count = 1)#查找替换
# print(data_new)
# ms = re.findall(p,data)#查找全部
# print(ms)
# # 如果要匹配多次，使用循环
# while re.search(p,data):
#     print(data)
#     m = re.search(p, data)
#     g = m.group(1)
#     v = config.get('data', g)
#     data = re.sub(p, v, data, count=1)
# print('最终',data)

import  requests
from API_0419.common.config import config

class Http_Request2():
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self,method,url,data):
        '''判断请求方式是get还是post'''
        if type(data) == str:
            data = eval(data)
        if method.lower() == 'get':
            res=self.session.request(method = method,url = url,params=data)
            # print("请求参数:",data)
            return res
        elif method.lower() == 'post':
            res=self.session.request(method = method,url = url,data=data)
            return res
        else:
            print('你输入的请求方式错误')
    def close(self):
        self.session.close()
http_request = Http_Request2()
{'mobilephone':'#normal_mobile#','pwd':'#normal_pwd#'}
{'memberId':'#normal_member_id#','password': '#normal_pwd#','loanId':'#loan_id#','amount':'100'}
res1 = http_request.request('get','http://test.lemonban.com/futureloan/mvc/api/member/login',"{'mobilephone':'13662278421','pwd':'123456789'}")
res2 = http_request.request('get','http://test.lemonban.com/futureloan/mvc/api/member/login',"{'mobilephone':'13662278421','pwd':'123456789'}")
res = http_request.request('get','http://test.lemonban.com/futureloan/mvc/api/member/bidLoan',"{'memberId':'1068','password': '123456789','loanId':'100','amount':'100'}")
print(res.text)
print(res)
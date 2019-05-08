#name
#name
import  requests
from API_0419.common.config import config
from API_0419.common import logger

logger = logger.get_logger(__name__)
# class Http_Request():
#     '''初始化参数'''
#     def __init__(self,url,method,data,cookies = None):
#         self.url = url
#         self.method = method
#         self.data = data
#         self.cookies = cookies

    # def http_request(self):
    #     '''判断请求方式是get还是post'''
    #     if type(self.data) == str:
    #         self.data = eval(self.data)
    #     url = config.get('api','pre_url')+url
    #     if self.method.lower() == 'get':
    #         res=requests.get(self.url,params=self.data,cookies = self.cookies)
    #         return res
    #     elif self.method.lower() == 'post':
    #         res=requests.post(self.url,data=self.data,cookies = self.cookies)
    #         return res
    #     else:
    #         print('你输入的请求方式错误')

class Http_Request2():
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self,method,url,data):
        '''判断请求方式是get还是post'''
        if type(data) == str:
            data = eval(data)
        #拼接url
        url = config.get('api','pre_url')+url
        logger.debug('请求url：{}'.format(url))
        logger.debug('请求data：{}'.format(data))
        if method.lower() == 'get':
            res=self.session.request(method = method,url = url,params=data)
            # print("请求参数:",data)
            return res
        elif method.lower() == 'post':
            res=self.session.request(method = method,url = url,data=data)
            return res
        else:
            # print('你输入的请求方式错误')
            logger.error("'你输入的请求方式错误'")
    def close(self):
        self.session.close()




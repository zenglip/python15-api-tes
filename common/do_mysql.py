#name
import pymysql
import configparser
from API_0419.common.config import config
from API_0419.common import contants

class DoMysql():
    '''
    完成与MySql数据库交互
    '''
    def __init__(self):

        self.mysql = pymysql.connect(
            host= config.get("mysql","host"),
            user=config.get("mysql","username"),
            password=config.get("mysql","password"),
            port=config.get("mysql","port"),
            charset='utf8'
        )
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)
        #self.cursor = self.mysql.cursor()

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        sele.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()
#

# #1、建立连接
# config = configparser.ConfigParser()
# config.read(contants.mysql_file)
# #数据需要用eval转化，虽然都是字符串，但是不一样！！！！！！！！11
# host = eval(config.get('mysql', 'host'))
# print(type(host),host)
# username = eval(config.get('mysql', 'username'))
# print(type(username),username)
# password = eval(config.get('mysql', 'password'))
# print(type(password),password)
# port = eval(config.get('mysql', 'port'))
#
#
#
#
#
# mysql = pymysql.connect(
#     host = host,
#     user = username,
#     password = password,
#     port = 3306,
#     charset = 'utf8'
# )
#
# #2、新建查询页面，建立游标
# cursor = mysql.cursor()
#
# #3、编写SQL
# sql = 'select max(mobilephone) from future.member'
# # sql = 'select * from future.member limit 10'
# #4、执行SQL
# cursor.execute(sql)
#
# #5、查看结果
# #result = cursor.fetchone()#获取查询结果集里面最近的一条数据返回
# result = cursor.fetchall()#获取全部结果集
# print(type(result),result)
#
# #6、关闭查询
# cursor.close()
# #7、关闭数据连接
# mysql.close()




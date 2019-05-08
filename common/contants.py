#获取文件路径
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

case_file = os.path.join(base_dir,'data','cases.xlsx')

log_dir = os.path.join(base_dir,'log')

global_file = os.path.join(base_dir,'config','global.conf')
# print(global_file)

online_file = os.path.join(base_dir,'config','online.conf')
# print(online_file)

test_file = os.path.join(base_dir,'config','test.conf')
# print(test_file)

normal_number = os.path.join(base_dir,'config','normal_number.conf')

mysql_file = os.path.join(base_dir,'config','mysql.conf')

case_dir = os.path.join(base_dir,'test_cases')

report_dir = os.path.join(base_dir,'reports')

#name
import configparser
from API_qianchengdai.common import contants

config = configparser.ConfigParser()

config.read(contants.global_file)  # 先加载global

switch = config.getboolean('switch','on')


print(switch)
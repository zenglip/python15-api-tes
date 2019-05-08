#name
import configparser
from API_0419.common import contants
class ReadConfig:
    '''完成配置文件的读取
    '''
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)#先加载global
        switch = self.config.getboolean('switch','on')

        if switch:#如果为True，使用online配置
            self.config.read(contants.online_file)

        else:#为False,使用test配置
            self.config.read(contants.test_file)

    def get(self,section,option):
        return eval(self.config.get(section, option))


config = ReadConfig()
if __name__ == '__main__':
    config = ReadConfig()
    print(config.get('api','pre_url'))
    # print(config.get('mysql', 'host'))
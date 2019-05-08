import logging
from configparser import RawConfigParser
from API_0419.common import contants

#读取配置文件的输出格式和水平
cf = RawConfigParser()
cf.read(contants.online_file,encoding="utf-8")

Level_name = cf.get("Log", "Level_name")  # 读取配置文件的级别和格式
Formatter_name = cf.get("Log", "Formatter_name")

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(Level_name)#收集水平设置

    # fmt = "%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=Formatter_name)#设置日志格式

    console_handler = logging.StreamHandler()#指定输出到控制台
    console_handler.setLevel(Level_name)#输出水平设置
    console_handler.setFormatter(formatter)#指定输出格式


    file_handler = logging.FileHandler(contants.log_dir+'/case.log',encoding='utf8')#指定输出到文件
    file_handler.setLevel('INFO')#输出水平设置
    file_handler.setFormatter(formatter)#指定输出格式

    logger.addHandler(console_handler)#添加输出渠道
    logger.addHandler(file_handler)
    return logger
# logger = get_logger('case')
# logger.info('测试开始')
# logger.error('测试报错')
# logger.debug('测试数据')
# logger.info('测试结束')
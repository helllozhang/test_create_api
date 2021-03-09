import logging
from common.handler_conf import conf

def create_log(name='111.logs', level='DEBUG', filename='logs.logs', Terminal_level ='DEBUG', File_level='DEBUG'):
    # 创建日志收集器
    my_log = logging.getLogger(name)
    # 设置收集器收集日志等级
    my_log.setLevel(level)
    # 创建输出渠道
    # 1.输出到控制台
    Terminal_log = logging.StreamHandler()
    Terminal_log.setLevel(Terminal_level)
    my_log.addHandler(Terminal_log)
    # 2.输出到日志文件
    File_log = logging.FileHandler(filename,encoding='utf-8',mode='w')
    File_log.setLevel(File_level)
    my_log.addHandler(File_log)

    # 设置日志输入格式
    log_formate = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
    # 设置输入日志到控制台
    Terminal_log.setFormatter(log_formate)
    # 设置输入日志到文件
    File_log.setFormatter(log_formate)
    return my_log


log = create_log(name=conf.get('logging','name'),
                 level=conf.get('logging','level'),
                 filename=r'D:\pycharm\py35_api_cekai\logs\log.log',
                 Terminal_level=conf.get('logging','Terminal_level'),
                 File_level=conf.get('logging','File_level'))

from configparser import ConfigParser
# import os


class Config(ConfigParser):
    # 在创建对象时,直接加载配置文件中得内容

    def __init__(self,conf_file):
        super().__init__()
        self.read(conf_file,encoding='utf-8')

# conf = Config(os.path.join(conf_path,'config.ini'))
conf = Config(r'D:\pycharm\py35_api_cekai\conf\config.ini')


if __name__ == '__main__':
    conf = Config(r'D:\pycharm\py35_api_cekai\conf\config.ini')
    name = conf.get('logging','name')
    print(name)
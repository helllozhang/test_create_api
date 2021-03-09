import random
from common.handler_db import DB

db = DB()
def random_name():
    """随机生成一个用户名"""
    while True:
        s1 = random.choice(["a", "b", "c", "d", "e"])
        number = random.randint(1, 999999)
        name = s1 + str(number)
        email = str(number) + '@163.com'
        # 判断数据库中是否存在该用户名，
        res = db.find_count("SELECT * FROM test.auth_user WHERE username='{}'".format(name))
        if res == 0:
            return name, email


import unittest

import jsonpath
import requests
import os
from unittestreport import ddt,list_data

from common.handler_conf import conf
from common.handler_log import log
from common.handler_re import Asser
from common.handler_excel import Do_excel
from common.handler_path import excel_path
from common.handler_replac import replace_data,CaseDate
from common.handler_ran_name import random_name



@ddt
class Test_Project(unittest.TestCase):
    ast = Asser()
    excel = Do_excel(os.path.join(excel_path,'api_data.xlsx'),'project')
    cases = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        CaseDate.name,CaseDate.email = random_name()
        parm = {
            "username": CaseDate.name,
            "email": CaseDate.email,
            "password": "123456",
            "password_confirm": "123456"
        }
        rg_res = requests.post(url='http://api.keyou.site:8000/user/register/',json=parm).json()
        token = jsonpath.jsonpath(rg_res,'$.token')[0]
        CaseDate.token= "JWT " + token

    @list_data(cases)
    def test_project(self,item):
        url = conf.get('env','url')+ item['url']
        method = item['method']
        parms = eval(replace_data(item['data']))
        headers = {
            "Authorization": getattr(CaseDate, "token")
        }
        res = requests.request(method=method,url=url,json=parms,headers=headers).json()
        print(res)
        while jsonpath.jsonpath(res,'$.id'):
            print(1)
            CaseDate.id = jsonpath.jsonpath(res,'$.id')[0]
            CaseDate.time = jsonpath.jsonpath(res,'$.create_time')[0]
            break
        expected = eval(replace_data(item['expected']))
        try:
            self.ast.ass(expected,res)
        except AssertionError as e:
            log.info('用例--【{}】---执行失败'.format(item['title']))
            raise e
        else:
            log.info('用例--【{}】---执行成功'.format(item['title']))
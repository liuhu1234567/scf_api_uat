from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest


def api_template_find(token, id):
    """【平台方】通过模板CODE查询"""
    url = f'{api_host}/api-scf/template/find'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    params = {'id': id}
    r = requests.get(url, headers=headers, params=params)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{params}')
    print(f'接口响应为：{r.text}')
    return r


class TemplateFind(unittest.TestCase):
    def test_template_find(self):
        """【平台方】通过模板CODE查询"""
        id = {}
        r = api_template_find(token_scf_supplier, id)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now


        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

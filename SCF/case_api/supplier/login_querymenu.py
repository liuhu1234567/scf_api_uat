from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest


def api_login_querymenu(token):
    """【供应商/经销商】登陆查询菜单"""
    url = f'{api_host}/api-scf/login/query/menu'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "5",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


class LoginQueryMenu(unittest.TestCase):
    def test_login_querymenu(self):
        """【供应商/经销商】登陆查询菜单"""
        r = api_login_querymenu(token_scf_supplier)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_faker import get_number, get_name, get_company, get_phone, get_email ,get_sfz
import requests
import unittest
import json

def api_user_insert_user(token, payload):
    """【平台方】用户新增"""
    url = f'{api_host}/api-scf/user/insert/user'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r

def api_user_auth_user_role(token, payload):
    """【平台方】用户分配角色"""
    url = f'{api_host}/api-scf/user/auth/user/role'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r

def api_user_query_users_page(token, payload):
    """【平台方】用户分页查询"""
    url = f'{api_host}/api-scf/user/query/users/page'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r

class User(unittest.TestCase):
    def test_001_user_insert_user(self):
        """【平台方】用户新增"""
        rolename = get_name()
        descnum = get_number(10)
        sfz = get_sfz()
        email = get_email()
        payload = {
            "employeeNo": "123123",
            "mailbox": f"{email}",
            "mobile": f"{descnum}",
            "nickName": f"{rolename}",
            "numId": f"{sfz}",
            "organizationName": "123123",
            "postName": "123123",
            "roleId": "1549711236625432577"
        }
        r = api_user_insert_user(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_user_auth_user_role(self):
        """【平台方】用户分配角色"""
        payload = {
            "roleId": 0,
            "userId": 0
        }
        r = api_user_auth_user_role(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


    def test_003_user_query_users_page(self):
        """【平台方】用户分页查询"""
        payload = {
            "num": 1,
            "size": 10,
        }
        r = api_user_query_users_page(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

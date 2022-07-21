from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_email, get_phone, get_sfz
from case_api.role import api_role_insert
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


def api_user_query_users_page(token, payload):
    """【平台方】用户分页查询"""
    url = f'{api_host}/api-scf/user/query/users/page'
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
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


g_d = {}


class User(unittest.TestCase):
    def test_001_user_insert_user(self):
        """【平台方】用户新增"""
        payload_one = {
            "roleName": f"角色名称{get_number(6)}",
            "roleDesc": ""
        }
        roleId = api_role_insert(token_scf_platform, payload_one).json()['datas']
        g_d['roleId'] = roleId
        payload = {
            "employeeNo": "",
            "mailbox": get_email(),
            "mobile": get_phone(),
            "nickName": get_name(),
            "numId": get_sfz(),
            "organizationName": "",
            "postName": "",
            "roleId": roleId
        }
        r = api_user_insert_user(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_user_query_users_page(self):
        """【平台方】用户分页查询"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "mobile": "",
            "nickName": "",
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": "",
            "userName": ""
        }
        r = api_user_query_users_page(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_user_auth_user_role(self):
        """【平台方】用户分配角色"""
        payload = {
            "roleId": g_d.get('roleId'),
            "userId": g_d.get('id')
        }
        r = api_user_auth_user_role(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)



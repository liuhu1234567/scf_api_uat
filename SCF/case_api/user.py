from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_email, get_company, get_phone, get_sfz
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
        nickname = get_name()
        companyname = get_company()
        mobile = get_phone()
        numid = get_sfz()
        mailbox = get_email()
        descnum = get_number(6)
        payload = {"nickName": nickname, "organizationName": companyname, "mobile": mobile, "numId": numid,
                   "mailbox": mailbox, "employeeNo": descnum, "postName": "CEO",
                   "roleId": "1549325719312375809"}
        r = api_user_insert_user(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_user_auth_user_role(self):
        """【平台方】用户分配角色"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "roleId": 0,
            "userId": 0
        }
        r = api_user_insert_user(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


    def test_003_user_query_users_page(self):
        """【平台方】用户分页查询"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "mobile": "",
            "nickName": "",
            "num": 0,
            "size": 0,
            "updateBy": 0,
            "updateTime": "",
            "userName": ""
        }
        r = api_user_insert_user(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)
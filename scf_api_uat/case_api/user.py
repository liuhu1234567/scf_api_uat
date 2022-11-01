from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.do_faker import get_number, get_name, get_company, get_phone, get_email, get_sfz
from common.global_variable import customize_dict
import requests
import unittest
import json
from case_api.enterprise import api_enterprise_queryEntArchivesDetail

"""用户逻辑处理层"""


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


def api_user_checkUserInfo(token, payload):
    """【平台方】检测云中云与金点信用户关系-无参"""
    url = f'{api_host}/api-scf/user/checkUserInfo'
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


def api_user_initUserInfo(token, payload):
    """【平台方】初始化云中云与金点信用户关系-有参"""
    url = f'{api_host}/api-scf/user/initUserInfo'
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


def api_user_selectCustomerType(token, payload):
    """登录后选择客户类型"""
    url = f'{api_host}/api-scf/user/selectCustomerType'
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


def api_user_listCoree(token, payload):
    """获取核心企业"""
    url = f'{api_host}/api-scf/user/listCoree'
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


def api_user_customerTypeList(token, payload):
    """获取客户类型列表"""
    url = f'{api_host}/api-scf/user/customerTypeList'
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


def api_user_cloudUserInfo(token, payload):
    """对接云中云2.0-进入供应链金融平台时初始化用户相关信息"""
    url = f'{api_host}/api-scf/user/cloudUserInfo'
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
    # def test_001_user_insert_user(self):
    #     """【平台方】用户新增"""
    #     rolename = get_name()
    #     descnum = get_number(10)
    #     sfz = get_sfz()
    #     email = get_email()
    #     payload = {
    #         "employeeNo": "123123",
    #         "mailbox": f"{email}",
    #         "mobile": f"{descnum}",
    #         "nickName": f"{rolename}",
    #         "numId": f"{sfz}",
    #         "organizationName": "123123",
    #         "postName": "123123",
    #         "roleId": "1549711236625432577"
    #     }
    #     r = api_user_insert_user(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #
    #     self.assertEqual(200, r_json['resp_code'])
    #     # self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_user_checkUserInfo(self):
        """【平台方】检测云中云与金点信用户关系-无参"""
        payload = {}
        r = api_user_checkUserInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_user_initUserInfo(self):
        """【平台方】初始化云中云与金点信用户关系-有参"""
        coreEntName = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['entName']
        payload = {
            "coreEntName": coreEntName,
            "customerType": 1
        }
        r = api_user_initUserInfo(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_user_selectCustomerType(self):
        """登录后选择客户类型 V2.1.1 新增"""
        payload = {
            "coreId": 0,
            "customerType": 5
        }
        r = api_user_selectCustomerType(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_user_listCore(self):
        """获取核心企业 V2.1.1 新增"""
        payload = {}
        r = api_user_listCoree(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_user_customerTypeList(self):
        """获取客户类型列表 V2.1.1 新增"""
        payload = {}
        r = api_user_customerTypeList(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_009_user_cloudUserInfo(self):
        """对接云中云2.0-进入供应链金融平台时初始化用户相关信息 V2.1.1 新增"""
        payload = {}
        r = api_user_cloudUserInfo(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

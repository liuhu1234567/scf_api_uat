from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name
import requests
import unittest
import json

def api_role_insert(token, payload):
    """【供应商/经销商】新增角色"""
    url = f'{api_host}/api-scf/role/insert'
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

def api_roles_all(token, payload):
    """【供应商/经销商】查询所有角色"""
    url = f'{api_host}/api-scf/role/query/roles/all'
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

def api_roles_page(token, payload):
    """【供应商/经销商】角色分页查询"""
    url = f'{api_host}/api-scf/role/query/roles/page'
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

def api_role_update(token, payload):
    """【供应商/经销商】编辑角色"""
    url = f'{api_host}/api-scf/role/update'
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

def api_role_updateenabled(token, payload):
    """【供应商/经销商】编辑角色状态"""
    url = f'{api_host}/api-scf/role/update/enabled'
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

def api_role_delete(token, payload):
    """【供应商/经销商】删除角色"""
    url = f'{api_host}/api-scf/role/delete'
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

g_d = {}

class Role(unittest.TestCase):
    def test_001_role_insert(self):
        """【供应商/经销商】新增角色"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "roleName": f"{rolename}",
            "roleDesc": f"{descnum}"
        }
        r = api_role_insert(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_roles_page(self):
        """【供应商/经销商】角色分页查询"""
        payload = {
            "num": "1",
            "size": "100"
        }
        r = api_roles_page(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_role_update(self):
        """【供应商/经销商】编辑角色"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "id": g_d.get('id'),
            "roleName": f"修改后的{rolename}",
            "roleDesc": f"修改后的{descnum}"
        }
        r = api_role_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_role_updateenabled(self):
        """【供应商/经销商】编辑角色状态"""
        payload = {
            "enabled": "1",
            "id": g_d.get('id')
        }
        r = api_role_updateenabled(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_role_delete(self):
        """【供应商/经销商】删除角色"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_role_delete(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_roles_all(self):
        """【供应商/经销商】查询所有角色"""
        payload = {}
        r = api_roles_page(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
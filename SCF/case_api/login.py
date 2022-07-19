from common.do_config import api_host, restime
from common.get_token import token_scf_supplier, token_scf_platform, token_scf_financier, token_scf_enterprise
from common.global_variable import customize_dict
import json
import requests
import unittest
from jsonpath import jsonpath


def api_login_querymenu(token):
    """登陆查询菜单"""
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

def api_login_auth_role_menu(token, payload):
    """角色分配菜单"""
    url = f'{api_host}/api-scf/login/auth/role/menu'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "5",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r

def api_login_auth_query_menu(token, payload):
    """角色分配菜单展示"""
    url = f'{api_host}/api-scf/login/auth/query/menu'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "5",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r

class Login(unittest.TestCase):
    def test_login_querymenu_supplier(self):
        """【供应商/经销商】登陆查询菜单"""
        r = api_login_querymenu(token_scf_supplier)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['系统管理', '角色管理', '用户管理', '企业中心', '企业档案', '档案修改', '企业认证', '银行账户管理', '数据管理', '采购数据', '财务数据', '金融产品管理', '产品申请']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime)

    def test_login_querymenu_platform(self):
        """【平台方】登陆查询菜单"""
        r = api_login_querymenu(token_scf_platform)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['系统管理', '角色管理', '用户管理', '企业中心', '企业档案', '档案修改', '企业认证', '银行账户管理', '客户管理', '客户列表', '客户审批', '数据管理', '采购数据', '财务数据', '金融产品管理', '产品列表', '产品分配列表', '产品申请', '配置管理', '产品配置', '数据表配置']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime)

    def test_login_querymenu_financier(self):
        """【资金方】登陆查询菜单"""
        r = api_login_querymenu(token_scf_financier)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['系统管理', '角色管理', '用户管理', '企业中心', '企业档案', '档案修改', '企业认证', '银行账户管理', '金融产品管理', '产品列表', '产品分配列表']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime)

    def test_login_querymenu_enterprise(self):
        """【核心企业/核企子公司】登陆查询菜单"""
        r = api_login_querymenu(token_scf_enterprise)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['系统管理', '角色管理', '用户管理', '企业中心', '企业档案', '档案修改', '企业认证', '银行账户管理', '客户管理', '客户列表', '数据管理', '采购数据', '财务数据', '金融产品管理', '产品列表', '产品分配列表']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime)

    def test_login_auth_role_menu(self):
        """【平台方】角色分配菜单"""
        payload = {"menuSorts": [],"roleId": 0}
        r = api_login_auth_role_menu(token_scf_supplier, payload)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_login_auth_query_menu(self):
        """【平台方】角色分配菜单展示"""
        payload = {"id": 0}
        r = api_login_auth_query_menu(token_scf_supplier, payload)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


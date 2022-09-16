import logging

from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
import json
import requests
import unittest
from jsonpath import jsonpath
from XTestRunner import HTMLTestRunner


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
        menuName = ['企业中心', '企业档案', '企业认证', '银行账户管理', '金融产品管理', '产品申请', '准入管理', '准入申请', '准入审批', '授信管理', '授信申请', '授信审批', '授信结果', '金点信', '金点信列表', '开立管理', '转让管理', '转让审批', '保理融资', '融资审批', '清分管理', '普惠融资', '订单融资', '订单审批', '贷后管理', '放款管理', '数据管理', '采购数据', '财务数据', '系统管理', '角色管理', '用户管理']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_login_querymenu_platform(self):
        """【平台方】登陆查询菜单"""
        r = api_login_querymenu(token_scf_platform)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['企业中心', '企业档案', '企业认证', '银行账户管理', '客户管理', '客户列表', '客户审批', '金融产品管理', '产品列表', '融资客户列表', '准入管理', '准入申请', '准入审批', '授信管理', '授信申请', '授信审批', '授信结果', '额度管理', '额度审批', '金点信', '金点信列表', '开立管理', '转让管理', '转让审批', '保理融资', '融资审批', '再保理融资', '再保理审批', '清分管理', '普惠融资', '订单融资', '订单审批', '贷后管理', '放款管理', '数据管理', '采购数据', '财务数据', '配置管理', '产品配置', '金点信配置', '全量字段表模板', '数据表配置', '系统管理', '角色管理', '用户管理']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_login_querymenu_financier(self):
        """【资金方】登陆查询菜单"""
        r = api_login_querymenu(token_scf_financier)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['企业中心', '企业档案', '企业认证', '银行账户管理', '金融产品管理', '产品列表', '融资客户列表', '准入管理', '准入审批', '授信管理', '授信审批', '授信结果', '额度管理', '金点信', '金点信列表', '开立管理', '转让审批', '融资审批', '再保理审批', '清分管理', '普惠融资', '订单审批', '贷后管理', '放款管理', '系统管理', '角色管理', '用户管理']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_login_querymenu_enterprise(self):
        """【核心企业/核企子公司】登陆查询菜单"""
        r = api_login_querymenu(token_scf_enterprise)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        menuName = ['企业中心', '企业档案', '企业认证', '银行账户管理', '金融产品管理', '产品列表', '融资客户列表', '准入管理', '准入审批', '授信管理', '授信审批', '授信结果', '额度管理', '额度分配', '金点信', '金点信列表', '开立管理', '转让审批', '融资审批', '再保理审批', '清分管理', '普惠融资', '订单审批', '贷后管理', '放款管理', '数据管理', '采购数据', '财务数据', '系统管理', '角色管理', '用户管理']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(menuName, jsonpath(r_json, '$..menuName'))
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_login_auth_role_menu(self):
        """【平台方】角色分配菜单"""
        payload = {"menuSorts": [],"roleId": 0}
        r = api_login_auth_role_menu(token_scf_supplier, payload)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_login_auth_query_menu(self):
        """【平台方】角色分配菜单展示"""
        payload = {"id": 1564450377663664130}
        r = api_login_auth_query_menu(token_scf_supplier, payload)
        r_json = r.json()

        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

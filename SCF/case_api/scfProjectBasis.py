from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
from case_api.scfFinanceProduct import api_scfFinanceProduct_insert
import json
import requests
import unittest


def api_scfProjectBasis_insert(token, payload):
    """【平台方】新增项目配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/insert'
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

def api_scfProjectBasis_listEnterprise(token, payload):
    """【平台方】查询融资企业"""
    url = f'{api_host}/api-scf/scfProjectBasis/listEnterprise'
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

def api_scfProjectBasis_enter(token, payload):
    """【平台方】产品配置-准入配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/enter'
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

def api_scfProjectBasis_grant(token, payload):
    """【平台方】产品配置-授信配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/grant'
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

def api_scfProjectBasis_open(token, payload):
    """【平台方】产品配置-开立配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/open'
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

def api_scfProjectBasis_transfer(token, payload):
    """【平台方】产品配置-转让配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/transfer'
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

def api_scfProjectBasis_finance(token, payload):
    """【平台方】产品配置-融资配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/finance'
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

def api_scfProjectBasis_refactor(token, payload):
    """【平台方】产品配置-再保理配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/refactor'
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

def api_scfProjectBasis_search(token, payload):
    """【平台方】项目配置搜索"""
    url = f'{api_host}/api-scf/scfProjectBasis/search'
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

def api_scfProjectBasis_enable(token, payload):
    """【平台方】项目配置启用-停用"""
    url = f'{api_host}/api-scf/scfProjectBasis/enable'
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

def api_scfProjectBasis_deliver(token, payload):
    """【平台方】产品配置-再保理配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/deliver'
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

def api_scfProjectBasis_delete(token, payload):
    """【平台方】项目配置删除"""
    url = f'{api_host}/api-scf/scfProjectBasis/delete'
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

class ScfProjectBasis(unittest.TestCase):
    def test_001_scfProjectBasis_insert(self):
        """【平台方】新增项目配置"""
        creditCode = get_number(10)
        payload = {
            "bankId": creditCode,
            "businessType": creditCode,
            "enable": True,
            "enterpriseId": 1,
            "name": "",
            "scfFinanceProductId": creditCode
        }
        r = api_scfProjectBasis_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        g_d['id'] = r_json['datas']
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


    def test_002_scfProjectBasis_enter(self):
        """【平台方】产品配置-准入配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "filePath": "",
            "flowId": 0,
            "grantFlowItemId": 0,
            "link": ""
        }
        r = api_scfProjectBasis_enter(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfProjectBasis_grant(self):
        """【平台方】产品配置-授信配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "basisId": 0,
            "flowId": 0
        }
        r = api_scfProjectBasis_grant(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfProjectBasis_open(self):
        """【平台方】产品配置-开立配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "basisId": 0,
            "flowId": 0
        }
        r = api_scfProjectBasis_open(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfProjectBasis_transfer(self):
        """【平台方】产品配置-转让配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "basisId": 0,
            "flowId": 0
        }
        r = api_scfProjectBasis_transfer(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfProjectBasis_finance(self):
        """【平台方】产品配置-融资配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "basisId": 0,
            "flowId": 0
        }
        r = api_scfProjectBasis_finance(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfProjectBasis_refactor(self):
        """【平台方】产品配置-再保理配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "basisId": 0,
            "flowId": 0
        }
        r = api_scfProjectBasis_refactor(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_scfProjectBasis_listEnterprise(self):
        """【平台方】查询融资企业"""
        payload = {}
        r = api_scfProjectBasis_listEnterprise(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_scfProjectBasis_search(self):
        """【平台方】产品配置列表-搜索"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "enable": True,
            "enterpriseName": "",
            "name": "",
            "num": 0,
            "size": 0
        }
        r = api_scfProjectBasis_search(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_scfProjectBasis_enable(self):
        """【平台方】项目配置启用-停用"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "enable": 1,
            "id": g_d['id']
        }
        r = api_scfProjectBasis_enable(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_scfProjectBasis_deliver(self):
        """【平台方】项目配置分配"""
        payload_one = {
            "amountMax": 100000,
            "amountMin": 1000,
            "availableBegin": "2022-7-13 13:54:30",
            "availableEnd": "2023-7-13 13:54:30",
            "enable": 1,
            "financeName": "中信银行",
            "introduction": "供应链企业申请微粒贷",
            "loanBegin": "2022-7-13 13:54:30",
            "loanEnd": "2023-7-13 13:54:30",
            "loop": True,
            "name": "企业微粒贷",
            "pay": True,
            "purpose": "购买原材料",
            "rateMax": "0.3",
            "rateMin": "0.1",
            "single": True,
            "source": "线上"
        }
        enterpriseId = api_scfFinanceProduct_insert(token_scf_supplier, payload_one).json()["datas"]
        payload = {
            "basisId": g_d['id'],
            "enterpriseId": enterpriseId
        }
        r = api_scfProjectBasis_deliver(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_scfProjectBasis_delete(self):
        """【平台方】项目配置删除"""
        payload = {"id": g_d.get('id')}
        r = api_scfProjectBasis_delete(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)
from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import json
import requests
import unittest


def api_scfFinanceProduct_insert(token, payload):
    """【平台方】新增金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/insert'
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

def api_scfFinanceProduct_search(token, payload):
    """【平台方】搜索金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/search'
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

def api_scfFinanceProduct_projectDeliverSearch(token, payload):
    """【平台方】产品分配列表-搜索"""
    url = f'{api_host}/api-scf/scfFinanceProduct/projectDeliverSearch'
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

def api_scfFinanceProduct_update(token, payload):
    """【平台方】修改金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/update'
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

def api_scfFinanceProduct_enable(token, payload):
    """【平台方】启用-停用金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/enable'
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

def api_scfFinanceProduct_delete(token, payload):
    """【平台方】删除金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/delete'
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

class ScfFinanceProductInsert(unittest.TestCase):
    def test_001_scfFinanceProduct_insert(self):
        """【平台方】新增金融产品"""
        payload = {
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
        r = api_scfFinanceProduct_insert(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfFinanceProduct_search(self):
        """【平台方】搜索金融产品"""
        payload = {
            "enable": 1,
            "financeName": "",
            "name": "",
            "num": 1,
            "size": 100
        }
        r = api_scfFinanceProduct_search(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def api_003_scfFinanceProduct_projectDeliverSearch(self):
        """【平台方】产品分配列表-搜索"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "enable": 1,
            "financeName": "",
            "name": "",
            "num": 1,
            "size": 100
        }
        r = api_scfFinanceProduct_search(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfFinanceProduct_update(self):
        """【平台方】修改金融产品"""
        true = True
        payload = {
            "amountMax": 100000,
            "amountMin": 1000,
            "availableBegin": "2022-7-13 13:54:30",
            "availableEnd": "2023-7-13 13:54:30",
            "enable": 1,
            "financeName": "中信银行",
            "id": 0,
            "introduction": "供应链企业申请微粒贷",
            "loanBegin": "2022-7-13 13:54:30",
            "loanEnd": "2023-7-13 13:54:30",
            "loop": true,
            "name": "企业微粒贷",
            "pay": true,
            "purpose": "购买原材料",
            "rateMax": "0.3",
            "rateMin": "0.1",
            "single": true,
            "source": "线上"
        }
        r = api_scfFinanceProduct_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfFinanceProduct_enable(self):
        """【平台方】启用-停用金融产品"""
        true = True
        payload = {
            "amountMax": 100000,
            "amountMin": 1000,
            "availableBegin": "2022-7-13 13:54:30",
            "availableEnd": "2023-7-13 13:54:30",
            "enable": 0,
            "financeName": "中信银行",
            "id": g_d['id'],
            "introduction": "供应链企业申请微粒贷",
            "loanBegin": "2022-7-13 13:54:30",
            "loanEnd": "2023-7-13 13:54:30",
            "loop": true,
            "name": "企业微粒贷",
            "pay": true,
            "purpose": "购买原材料",
            "rateMax": "0.3",
            "rateMin": "0.1",
            "single": true,
            "source": "线上"
        }
        r = api_scfFinanceProduct_enable(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfFinanceProduct_delete(self):
        """【平台方】删除金融产品"""
        payload = {"id": g_d.get('id')}
        r = api_scfFinanceProduct_delete(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

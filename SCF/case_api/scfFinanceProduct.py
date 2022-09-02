from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_number
import datetime
import json
import requests
import unittest


def api_scfFinanceProduct_listBank(token):
    """【平台方】查询金融机构(银行、保理商)"""
    url = f'{api_host}/api-scf/scfFinanceProduct/listBank'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


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


def api_scfFinanceProduct_simpleList(token):
    """产品下拉列表"""
    url = f'{api_host}/api-scf/scfFinanceProduct/simpleList'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfFinanceProduct_projectDeliverSearch(token, payload):
    """产品分配列表(平台、供应商)-搜索"""
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


def api_scfFinanceProduct_projectDeliverBankSearch(token, payload):
    """产品分配列表(金融机构)-搜索"""
    url = f'{api_host}/api-scf/scfFinanceProduct/projectDeliverBankSearch'
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


def api_scfFinanceProduct_projectDeliverCoreSearch(token, payload):
    """产品分配列表(核心企业)-搜索"""
    url = f'{api_host}/api-scf/scfFinanceProduct/projectDeliverCoreSearch'
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


class ScfFinanceProduct(unittest.TestCase):
    def test_001_scfFinanceProduct_listBank(self):
        """【平台方】查询金融机构(银行、保理商)"""
        r = api_scfFinanceProduct_listBank(token_scf_platform)
        r_json = r.json()
        g_d['financeId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfFinanceProduct_insert(self):
        """【平台方】新增金融产品"""
        nowTime = str(datetime.datetime.now()).split('.')[0]
        futureTime = str(datetime.datetime.now() + datetime.timedelta(days=365)).split('.')[0]
        payload = {
            "amountMax": "100000",
            "amountMin": "1000",
            "availableBegin": nowTime,
            "availableEnd": futureTime,
            "enable": True,
            "financeId": g_d.get('financeId'),
            "id": 0,
            "loanBegin": nowTime,
            "loanEnd": futureTime,
            "loop": True,
            "name": f"金融产品名称{get_number(6)}",
            "pay": True,
            "rateMax": "3.8",
            "rateMin": "0.1",
            "single": True
        }
        r = api_scfFinanceProduct_insert(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfFinanceProduct_update(self):
        """【平台方】修改金融产品"""
        nowTime = str(datetime.datetime.now()).split('.')[0]
        futureTime = str(datetime.datetime.now() + datetime.timedelta(days=365)).split('.')[0]
        payload = {
            "amountMax": "100000",
            "amountMin": "1000",
            "availableBegin": nowTime,
            "availableEnd": futureTime,
            "financeId": g_d.get('financeId'),
            "id": g_d.get('id'),
            "introduction": f"产品介绍{get_number(6)}",
            "loanBegin": nowTime,
            "loanEnd": futureTime,
            "loop": True,
            "name": f"金融产品名称{get_number(6)}",
            "pay": True,
            "purpose": f"资金用途{get_number(6)}",
            "rateMax": "3.8",
            "rateMin": "0.1",
            "single": False,
            "source": f"还款来源{get_number(6)}"
        }
        r = api_scfFinanceProduct_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfFinanceProduct_enable(self):
        """【平台方】启用-停用金融产品"""
        payload = {
            "enable": 1,
            "id": g_d['id']
        }
        r = api_scfFinanceProduct_enable(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfFinanceProduct_delete(self):
        """【平台方】删除金融产品"""
        nowTime = str(datetime.datetime.now()).split('.')[0]
        futureTime = str(datetime.datetime.now() + datetime.timedelta(days=365)).split('.')[0]
        payload = {
            "amountMax": "100000",
            "amountMin": "1000",
            "availableBegin": nowTime,
            "availableEnd": futureTime,
            "enable": True,
            "financeId": g_d.get('financeId'),
            "id": 0,
            "loanBegin": nowTime,
            "loanEnd": futureTime,
            "loop": True,
            "name": f"金融产品名称{get_number(6)}",
            "pay": True,
            "rateMax": "3.8",
            "rateMin": "0.1",
            "single": True
        }
        id = api_scfFinanceProduct_insert(token_scf_platform, payload).json()['datas']
        payload = {
            "id": id
        }
        r = api_scfFinanceProduct_delete(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfFinanceProduct_search(self):
        """【平台方】搜索金融产品"""
        payload = {
            "enable": 1,
            "financeName": "",
            "name": "",
            "num": 1,
            "size": 100
        }
        r = api_scfFinanceProduct_search(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfFinanceProduct_simpleList(self):
        """【平台方】产品下拉列表"""
        r = api_scfFinanceProduct_simpleList(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_scfFinanceProduct_projectDeliverSearch(self):
        """【平台方】产品分配列表(平台、供应商)-搜索"""
        payload = {
            "enable": True,
            "entName": "",
            "enterpriseId": 0,
            "financeName": "",
            "isApply": False,
            "num": 1,
            "productName": "",
            "projectName": "",
            "size": 100
        }
        r = api_scfFinanceProduct_projectDeliverSearch(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_scfFinanceProduct_projectDeliverBankSearch(self):
        """【资金方】搜索金融产品"""
        payload = {
            "enable": True,
            "entName": "",
            "enterpriseId": 0,
            "financeName": "",
            "isApply": False,
            "num": 1,
            "productName": "",
            "projectName": "",
            "size": 10
        }
        r = api_scfFinanceProduct_projectDeliverBankSearch(token_scf_financier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_scfFinanceProduct_projectDeliverCoreSearch(self):
        """【核心企业】搜索金融产品"""
        payload = {
            "enable": True,
            "entName": "",
            "enterpriseId": 0,
            "financeName": "",
            "isApply": False,
            "num": 1,
            "productName": "",
            "projectName": "",
            "size": 10
        }
        r = api_scfFinanceProduct_projectDeliverCoreSearch(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

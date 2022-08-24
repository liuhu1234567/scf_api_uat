from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number
import requests
import unittest
import json

"""清分管理"""

def api_clearing_clearingDetail_list(token, payload):
    """日终对账明细"""
    url = f'{api_host}/api-scf/clearing/clearingDetail/list'
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

def api_clearing_historyClearingDetail_list(token, payload):
    """历史清分明细"""
    url = f'{api_host}/api-scf/clearing/historyClearingDetail/list'
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

def api_clearing_list(token, payload):
    """清分列表"""
    url = f'{api_host}/api-scf/clearing/list'
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

def api_clearing_revoke(token, payload):
    """撤销"""
    url = f'{api_host}/api-scf/clearing/revoke'
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

class  Clearing(unittest.TestCase):
    def test_001_clearing_clearingDetail_list(self):
        """日终对账明细"""
        payload = {
          "num": 1,
          "payerAccountNumber": "",
          "payerName": "",
          "recipientAccountNumber": "",
          "recipientName": "",
          "size": 10
        }
        r = api_clearing_clearingDetail_list(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_clearing_historyClearingDetail_list(self):
        """历史清分明细"""
        payload = {
          "num": 1,
          "payerAccountNumber": "",
          "payerName": "",
          "recipientAccountNumber": "",
          "recipientName": "",
          "size": 10
        }
        r = api_clearing_historyClearingDetail_list(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_clearing_list(self):
        """清分列表"""
        payload = {
          "num": 0,
          "payerAccountNumber": "",
          "payerName": "",
          "recipientAccountNumber": "",
          "recipientName": "",
          "size": 0
        }
        r = api_clearing_list(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_clearing_revoke(self):
        """清分列表"""
        payload = {
          "goldenLetterCode": "0"
        }
        r = api_clearing_revoke(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)
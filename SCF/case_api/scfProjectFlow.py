from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number
import requests
import unittest
import json

def api_scfProjectFlow_enterFlow(token, payload):
    """【平台方】准入配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/enterFlow'
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

def api_scfProjectFlow_financeFlow(token, payload):
    """【平台方】融资配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/financeFlow'
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

def api_scfProjectFlow_grantFlow(token, payload):
    """【平台方】授信配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/grantFlow'
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

def api_scfProjectFlow_openFlow(token, payload):
    """【平台方】开立配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/openFlow'
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

def api_scfProjectFlow_refactorFlow(token, payload):
    """【平台方】再保理配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/refactorFlow'
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

def api_scfProjectFlow_transferFlow(token, payload):
    """【平台方】转让配置-创建流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/transferFlow'
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

def api_scfProjectFlow_selectFlow(token, payload):
    """【平台方】查询流程"""
    url = f'{api_host}/api-scf/scfProjectFlow/selectFlow'
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

class ScfProjectFlow(unittest.TestCase):
    def test_001_scfProjectFlow_enterFlow(self):
        """【平台方】准入配置-创建流程"""
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": f"准入流程{get_number(6)}",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_enterFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfProjectFlow_grantFlow(self):
        """【平台方】授信配置-创建流程"""
        payload = {
              "customerType": 0,
              "flowItems": [
                {
                  "customerType": 0,
                  "flowItems": [],
                  "isExternal": True,
                  "isProtocol": True,
                  "isPush": True,
                  "name": f"授信流程{get_number(6)}",
                  "reportId": 0,
                  "step": 0,
                  "subs": []
                }
              ],
              "isExternal": True,
              "isProtocol": True,
              "isPush": True,
              "name": "",
              "reportId": 0,
              "step": 0,
              "subs": [
                {
                  "fileName": "",
                  "filePath": "",
                  "signType": 0
                }
              ]
            }
        r = api_scfProjectFlow_grantFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfProjectFlow_openFlow(self):
        """【平台方】开立配置-创建流程"""
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": f"开立流程{get_number(6)}",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_openFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfProjectFlow_transferFlow(self):
        """【平台方】转让配置-创建流程"""
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": f"转让流程{get_number(6)}",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_transferFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfProjectFlow_financeFlow(self):
        """【平台方】融资配置-创建流程"""
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": f"融资流程{get_number(6)}",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_financeFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfProjectFlow_refactorFlow(self):
        """【平台方】再保理配置-创建流程"""
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": f"再保理流程{get_number(6)}",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_refactorFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfProjectFlow_selectFlow(self):
        """【平台方】查询流程"""
        payload = {
            "projectEnum": 0
        }
        r = api_scfProjectFlow_selectFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

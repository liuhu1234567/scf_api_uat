from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number
from case_api.scfProjectFlow import api_scfProjectFlow_enterFlow, api_scfProjectFlow_grantFlow, api_scfProjectFlow_openFlow, api_scfProjectFlow_transferFlow, api_scfProjectFlow_financeFlow, api_scfProjectFlow_refactorFlow
import json
import requests
import unittest

def api_scfProjectBasis_listBank(token, payload):
    """【平台方】查询金融机构"""
    url = f'{api_host}/api-scf/scfProjectBasis/listBank'
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


def api_scfProjectBasis_listCore(token, payload):
    """【平台方】查询核心企业"""
    url = f'{api_host}/api-scf/scfProjectBasis/listCore'
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


def api_scfProjectBasis_listFinanceProduct(token, payload):
    """【平台方】金融产品列表"""
    url = f'{api_host}/api-scf/scfProjectBasis/listFinanceProduct'
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
    def test_001_scfProjectBasis_listBank(self):
        """【平台方】金融产品列表"""
        payload = {}
        r = api_scfProjectBasis_listBank(token_scf_platform, payload)
        r_json = r.json()
        g_d['bankId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfProjectBasis_listCore(self):
        """【平台方】查询核心企业"""
        payload = {}
        r = api_scfProjectBasis_listCore(token_scf_platform, payload)
        r_json = r.json()
        g_d['coreEnterpriseId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfProjectBasis_listFinanceProduct(self):
        """【平台方】金融产品列表"""
        payload = {}
        r = api_scfProjectBasis_listFinanceProduct(token_scf_platform, payload)
        r_json = r.json()
        g_d['scfFinanceProductId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfProjectBasis_insert(self):
        """【平台方】新增项目配置"""
        payload = {
            "bankId": g_d.get('bankId'),
            "businessType": 0,
            "enable": True,
            "enter": True,
            "enterpriseId": g_d.get('coreEnterpriseId'),
            "finance": True,
            "grants": True,
            "name": f"项目名称{get_number(6)}",
            "open": True,
            "refactor": True,
            "scfFinanceProductId": g_d.get('scfFinanceProductId'),
            "transfer": True
        }
        r = api_scfProjectBasis_insert(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfProjectBasis_enter(self):
        """【平台方】产品配置-准入配置"""
        payload_one = {
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
                    "name": f"流程名称{get_number(6)}",
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
        flowId = api_scfProjectFlow_enterFlow(token_scf_platform, payload_one).json()["datas"]
        payload = {
            "filePath": "",
            "flowId": flowId,
            "grantFlowItemId": 0,
            "link": ""
        }
        r = api_scfProjectBasis_enter(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfProjectBasis_grant(self):
        """【平台方】产品配置-授信配置"""
        payload_one = {
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
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        flowId = api_scfProjectFlow_grantFlow(token_scf_platform, payload_one).json()["datas"]
        payload = {
            "basisId": g_d.get('id'),
            "flowId": flowId
        }
        r = api_scfProjectBasis_grant(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfProjectBasis_open(self):
        """【平台方】产品配置-开立配置"""
        payload_one = {
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
        flowId = api_scfProjectFlow_openFlow(token_scf_platform, payload_one).json()['datas']
        payload = {
            "basisId": g_d.get('id'),
            "flowId": flowId
        }
        r = api_scfProjectBasis_open(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_scfProjectBasis_transfer(self):
        """【平台方】产品配置-转让配置"""
        payload_one = {
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
        flowId = api_scfProjectFlow_transferFlow(token_scf_platform, payload_one).json()['datas']
        payload = {
            "basisId": g_d.get('id'),
            "flowId": flowId
        }
        r = api_scfProjectBasis_transfer(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_scfProjectBasis_finance(self):
        """【平台方】产品配置-融资配置"""
        payload_one = {
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
        flowId = api_scfProjectFlow_financeFlow(token_scf_platform, payload_one).json()['datas']
        payload = {
            "basisId": g_d.get('id'),
            "flowId": flowId
        }
        r = api_scfProjectBasis_finance(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_scfProjectBasis_refactor(self):
        """【平台方】产品配置-再保理配置"""
        payload_one = {
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
        flowId = api_scfProjectFlow_refactorFlow(token_scf_platform, payload_one).json()['datas']
        payload = {
            "basisId": g_d.get('id'),
            "flowId": flowId
        }
        r = api_scfProjectBasis_refactor(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_scfProjectBasis_listEnterprise(self):
        """【平台方】查询融资企业"""
        payload = {}
        r = api_scfProjectBasis_listEnterprise(token_scf_platform, payload)
        r_json = r.json()
        g_d['enterpriseId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_scfProjectBasis_search(self):
        """【平台方】产品配置列表-搜索"""
        payload = {
            "enable": True,
            "enterpriseName": "",
            "name": "",
            "num": 0,
            "size": 10
        }
        r = api_scfProjectBasis_search(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_013_scfProjectBasis_enable(self):
        """【平台方】项目配置启用-停用"""
        payload = {
            "enable": 1,
            "id": g_d.get('id')
        }
        r = api_scfProjectBasis_enable(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_014_scfProjectBasis_deliver(self):
        """【平台方】项目配置分配"""
        payload = {
            "basisId": g_d.get('id'),
            "enterpriseId": g_d.get('enterpriseId')
        }
        r = api_scfProjectBasis_deliver(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_015_scfProjectBasis_delete(self):
        """【平台方】项目配置删除"""
        payload = {"id": g_d.get('id')}
        r = api_scfProjectBasis_delete(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

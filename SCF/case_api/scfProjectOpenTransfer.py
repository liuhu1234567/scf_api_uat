from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_faker import get_number
from common.global_variable import customize_dict
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
import requests
import unittest
import json

"""金点信配置"""


def api_scfProjectOpenTransfer_delete(token, payload):
    """【平台方】删除(入参：核心企业ID)"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/delete'
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


def api_scfProjectOpenTransfer_editOpenTransfer(token, payload):
    """【平台方】开立、转让编辑(入参为核心企业ID)"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/editOpenTransfer'
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


def api_scfProjectOpenTransfer_enable(token, payload):
    """【平台方】启用-停用"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/enable'
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


def api_scfProjectOpenTransfer_insertOpenTransfer(token, payload):
    """【平台方】开立、转让新增"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/insertOpenTransfer'
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


def api_scfProjectOpenTransfer_searchProjectOpenTransfer(token, payload):
    """【平台方】金点信配置列表-搜索"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/searchProjectOpenTransfer'
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


def api_scfProjectOpenTransfer_selectName(token, payload):
    """【平台方】选择流程节点名称-开立、转让"""
    url = f'{api_host}/api-scf/scfProjectOpenTransfer/selectName'
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


class ScfProjectOpenTransfer(unittest.TestCase):
    def test_001_scfProjectOpenTransfer_editOpenTransfer(self):
        """【平台方】开立、转让编辑(入参为核心企业ID)"""
        payload = {
            "coreName": "",
            "enable": "",
            "num": 1,
            "size": 10
        }
        coreId = api_scfProjectOpenTransfer_searchProjectOpenTransfer(token_scf_platform, payload).json()["datas"][0][
            "coreId"]
        payload_new = {
            "id": coreId
        }
        r = api_scfProjectOpenTransfer_editOpenTransfer(token_scf_platform, payload_new)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfProjectOpenTransfer_enable(self):
        """【平台方】启用-停用"""
        payload = {
            "coreName": "",
            "enable": "",
            "num": 1,
            "size": 10
        }
        coreId = api_scfProjectOpenTransfer_searchProjectOpenTransfer(token_scf_platform, payload).json()["datas"][0][
            "coreId"]
        payload_new = {
            "coreId": coreId,
            "enable": True
        }
        r = api_scfProjectOpenTransfer_enable(token_scf_platform, payload_new)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfProjectOpenTransfer_insertOpenTransfer(self):
        """【平台方】开立、转让新增"""
        payload = {
            "scfProjectOpenReq": {
                "coreId": 1549224468155265025,
                "isTemplate": False,
                "scfProjectFlowReq": {
                    "name": "开立流程名称-" + get_number(5),
                    "step": 2,
                    "flowItems": [
                        {
                            "customerType": 1,
                            "isExternal": True,
                            "isProtocol": True,
                            "isPush": True,
                            "reportId": 3,
                            "subs": [
                                {
                                    "fileName": "fileName",
                                    "filePath": "filePath",
                                    "signType": 1
                                }
                            ]
                        },
                        {
                            "customerType": 3,
                            "isExternal": True,
                            "isProtocol": True,
                            "isPush": True,
                            "reportId": 3,
                            "subs": [
                                {
                                    "fileName": "fileName",
                                    "filePath": "filePath",
                                    "signType": 1
                                }
                            ]
                        }
                    ]
                }
            },
            "scfProjectTransferReq": {
                "isTemplate": True,
                "isPush": True,
                "isHistory": True,
                "pushMaterial": 3,
                "serviceRate": "1.01",
                "scfProjectFlowReq": {
                    "name": "转让流程名称-" + get_number(5),
                    "step": 2,
                    "flowItems": [
                        {
                            "customerType": 3,
                            "isExternal": True,
                            "isProtocol": True,
                            "isPush": True,
                            "reportId": 3,
                            "subs": [
                                {
                                    "fileName": "fileName",
                                    "filePath": "filePath",
                                    "signType": 1
                                }
                            ]
                        }
                    ]
                }
            }
        }
        r = api_scfProjectOpenTransfer_insertOpenTransfer(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfProjectOpenTransfer_searchProjectOpenTransfer(self):
        """【平台方】金点信配置列表-搜索"""
        payload = {
            "coreName": "",
            "enable": "",
            "num": 1,
            "size": 10
        }
        r = api_scfProjectOpenTransfer_searchProjectOpenTransfer(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfProjectOpenTransfer_selectName(self):
        """【平台方】选择流程节点名称-开立、转让"""
        payload = {
        }
        r = api_scfProjectOpenTransfer_selectName(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfProjectOpenTransfer_delete(self):
        """【平台方】删除(入参：核心企业ID)"""
        payload = {
            "coreName": "",
            "enable": "",
            "num": 1,
            "size": 10
        }
        coreId = api_scfProjectOpenTransfer_searchProjectOpenTransfer(token_scf_platform, payload).json()["datas"][0][
            "coreId"]
        payload_new = {
            "id": coreId
        }
        r = api_scfProjectOpenTransfer_delete(token_scf_platform, payload_new)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

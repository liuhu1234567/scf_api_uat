from common.global_variable import customize_dict
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_config import api_host, restime
import requests
import json
import unittest
import random
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_getBusinessTypes, api_scfProjectBasis_listProjectBasisByType


def api_blockchain_upload(token, payload):
    """入库区块链信息"""
    url = f'{api_host}/api-scf/blockchain/upload'
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


def api_blockchain_info(token, payload):
    """查询区块链信息"""
    url = f'{api_host}/api-scf/blockchain/info'
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


g_d = {}


class Blockchain(unittest.TestCase):
    def test_001_blockchain_info(self):
        """【平台方】入库区块链信息"""
        g_d['busType'] = api_scfProjectBasis_getBusinessTypes(token_scf_platform).json()['datas'][0]['value']
        payload = {
            "businessType": random.randint(1, 5)
        }
        g_d['busId'] = api_scfProjectBasis_listProjectBasisByType(token_scf_platform, payload).json()['datas'][0]['id']
        payload = {
            "busId": g_d.get('busId'),
            "busType": g_d.get('busType'),
            "dataArea": [
                {
                    "label": "",
                    "value": ""
                }
            ]
        }
        r = api_blockchain_upload(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_blockchain_info(self):
        """【平台方】查询区块链信息"""
        payload = {
            "busId": g_d.get('busId'),
            "busType": g_d.get('busType'),
            "dataArea": [
                {
                    "label": "",
                    "value": ""
                }
            ]
        }
        r = api_blockchain_info(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

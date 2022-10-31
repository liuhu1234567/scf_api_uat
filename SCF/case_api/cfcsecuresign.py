from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from case_api.otherApi import api_otherApi_queryProjectList
from common.do_faker import get_number, get_card_number
import requests
import unittest
import json


def api_cfcsecuresign_upload_contract_url(token, payload):
    """【平台方】上传合同签署:流程3203"""
    url = f'{api_host}/cfc/secure/sign/upload/contract/url'
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

def api_cfcsecuresign_upload_contract_url(token, payload):
    """【平台方】上传合同签署:流程3203"""
    url = f'{api_host}/cfc/secure/sign/upload/contract/url'
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


class BackAccount(unittest.TestCase):
    def test_001_backAccount_insert(self):
        """【平台方】上传合同签署:流程3203 V2.1.1新增"""
        payload = {
            "contractName": "1585899879465320450",
            "contractTypeCode": "",
            "isSign": "",
            "otherSignInfo": [
                {
                    "projectCode": "1585899879465320450",
                    "userId": "1585834025305903106"
                }
            ],
            "url": "1585899879465320450"
        }
        r = api_cfcsecuresign_upload_contract_url(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

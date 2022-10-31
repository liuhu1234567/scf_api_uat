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
    "https://service-dev.dianliantech.com"
    url = f'{api_host}/api-ep/cfc/secure/sign/upload/contract/url'
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


def api_cfcsecuresign_send_sms(token, payload):
    """发送授权短信验证码3101"""
    url = f'{api_host}/api-ep/cfc/secure/sign/send/sms'
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


def api_cfcsecuresign_check_sms(token, payload):
    """短信授权3102"""
    url = f'{api_host}/api-ep/cfc/secure/sign/send/sms'
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


def api_cfcsecuresign_check_signature_contract(token, payload):
    """批量签署合同:流程3207签署合同"""
    url = f'{api_host}cfc/secure/sign/check/signature/contract'
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


class CfcSecureSign(unittest.TestCase):
    def test_001_CfcSecureSign_upload_contract_url(self):
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

    def test_002_CfcSecureSign_send_sms(self):
        """【平台方】发送授权短信验证码3101 V2.1.1新增"""
        payload = {
            "isSendVoice": True,
            "projectCode": "1585899879465320450",
            "userId": "1585834025305903106"
        }
        r = api_cfcsecuresign_send_sms(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_CfcSecureSign_check_sms(self):
        """【平台方】短信授权3102 V2.1.1新增"""
        payload = {
            "checkCode": True,
            "projectCode": "1585899879465320450",
            "userId": "1585834025305903106"
        }
        r = api_cfcsecuresign_check_sms(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_CfcSecureSign_check_signature_contract(self):
        """【平台方】批量签署合同:流程3207签署合同 V2.1.1新增"""
        payload = {
            "checkCode": "",
            "signContractByKeyword": [
                {
                    "contractNo": "1585834025305903106",
                    "signKeyword": {
                        "imageHeight": "",
                        "imageWidth": "",
                        "keyword": "关键字",
                        "offsetCoordX": "",
                        "offsetCoordY": ""
                    }
                }
            ],
            "signInfo": {
                "authorizationTime": "2023-10-31T07:41:48.897",
                "location": "1585834025305903106",
                "projectCode": "1585834025305903106",
                "userId": "1585834025305903106"
            }
        }
        r = api_cfcsecuresign_check_signature_contract(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

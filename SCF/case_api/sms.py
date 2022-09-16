from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_phone
import json
import requests
import unittest


def api_sms_send(token, payload):
    """【平台方】发送短信"""
    url = f'{api_host}/api-ep/sms/send'
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


def api_sms_valid(token, payload):
    """【平台方】手机与短信检测"""
    url = f'{api_host}/api-ep/sms/sendUserPwdSms'
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

class Sms(unittest.TestCase):
    def test_001_sms_send(self):
        """【平台方】发送短信"""
        phone = get_phone()
        payload = {
              "code": "1234",
              "entName": "",
              "password": "",
              "phone": 15338760344,
              "to": "",
              "userName": ""
            }
        r = api_sms_send(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_sms_valid(self):
        """【平台方】手机与短信检测"""
        phone = get_phone()
        payload = {
              "code": "1234",
              "entName": "",
              "password": "",
              "phone": 15338760344,
              "to": "",
              "userName": ""
            }
        r = api_sms_valid(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
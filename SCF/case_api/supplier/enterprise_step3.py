from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest
import json

def api_enterprise_step3(token, payload):
    """【供应商/经销商】企业认证步骤3-签署授权书及平台协议"""
    url = f'{api_host}/api-scf/enterprise/step3'
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


class EnterpriseStep2(unittest.TestCase):
    def test_enterprise_step2(self):
        """【供应商/经销商】企业认证步骤3-签署授权书及平台协议"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "confirmLicense": "",
            "id": 0,
            "ruleLicense": "",
            "serviceLicense": ""
        }
        r = api_enterprise_step3(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

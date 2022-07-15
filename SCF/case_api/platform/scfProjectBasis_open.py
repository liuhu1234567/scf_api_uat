from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest


def api_scfProjectBasis_open(token, payload):
    """【平台方】产品配置-开立配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/open'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=payload)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


class ScfProjectBasisOpen(unittest.TestCase):
    def test_scfProjectBasis_open(self):
        """【平台方】产品配置-开立配置"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "businessType": 0,
            "flowItems": [
                {
                    "businessType": 0,
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": "",
                    "projectEnum": 0,
                    "reportId": "",
                    "step": 0
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "projectEnum": 0,
            "reportId": "",
            "step": 0
        }
        r = api_scfProjectBasis_insertFlow(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

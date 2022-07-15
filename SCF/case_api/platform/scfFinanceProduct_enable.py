from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest


def api_scfFinanceProduct_enable(token, payload):
    """【平台方】启用-停用金融产品"""
    url = f'{api_host}/api-scf/scfFinanceProduct/insert'
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


class ScfFinanceProductEnable(unittest.TestCase):
    def test_scfFinanceProduct_enable(self):
        """【平台方】启用-停用金融产品"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        true = True
        payload = {
            "amountMax": 100000,
            "amountMin": 1000,
            "availableBegin": "2022-7-13 13:54:30",
            "availableEnd": "2023-7-13 13:54:30",
            "enable": 0,
            "financeName": "中信银行",
            "introduction": "供应链企业申请微粒贷",
            "loanBegin": "2022-7-13 13:54:30",
            "loanEnd": "2023-7-13 13:54:30",
            "loop": true,
            "name": "企业微粒贷",
            "pay": true,
            "purpose": "购买原材料",
            "rateMax": "0.3",
            "rateMin": "0.1",
            "single": true,
            "source": "线上"
        }
        r = api_scfFinanceProduct_enable(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

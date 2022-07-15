from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_card_number
import requests
import unittest


def api_backAccount_queryPage(token, payload):
    """【平台方】分页查询银行账户"""
    url = f'{api_host}/api-scf/backAccount/queryPage'
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


class BackAccountQueryPage(unittest.TestCase):
    def test_backAccount_queryPage(self):
        """【平台方】分页查询银行账户"""
        creditCode = get_number(10)
        bankAccountNo = get_card_number()
        payload = {
            "bankAccountName": "",
            "bankAccountNo": "",
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 0,
            "size": 0,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_backAccount_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

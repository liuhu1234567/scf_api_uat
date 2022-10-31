from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
import json

"""流程审批"""


def api_auditFlow_queryByFlowItemId(token, payload):
    """查询流程详情"""
    url = f'{api_host}/api-scf/auditFlow/queryByFlowItemId'
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


class Clearing(unittest.TestCase):
    def test_001_clearing_clearingDetail_list(self):
        """【平台方】查询流程详情"""
        payload = {
            "flowItemId": 0
        }
        r = api_auditFlow_queryByFlowItemId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

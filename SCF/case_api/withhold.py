from common.global_variable import customize_dict
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from case_api.template import api_template_uploadfile
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
from case_api.backAccount import api_backAccount_queryPage, api_backAccount_bindByProjectId
from common.do_config import api_host, restime
import requests
import json
import unittest
from common.do_excel import DoExcel
from common.do_faker import get_number
from jsonpath import jsonpath
import datetime

"""代扣逻辑处理层"""


def api_withhold_update(token, payload):
    """代扣编辑"""
    url = f'{api_host}/api-scf/withhold/update'
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


class OrderLoan(unittest.TestCase):
    def test_001_orderLoan_import(self):
        """代扣编辑 V2.1.1新增"""
        payload = {
            "busId": "5072473899979523927",
            "platformName": "111111",
            "platformCode": "22222",
            "withholdServiceCharge": "100.00",
            "withholdingInstructions": "说明"
        }
        r = api_withhold_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

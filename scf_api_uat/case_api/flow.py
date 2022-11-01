from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_company, get_number, get_name, get_phone, get_email, get_money
from common.do_excel import DoExcel
from common.do_time import time_format
from case_api.template import api_template_uploadfile
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
import requests
import unittest
import json
import time
import datetime

"""金点信"""


def api_flow_downPriorMaterial(token, payload):
    """下载前手资料"""
    url = f'{api_host}/api-scf/flow/downPriorMaterial'
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


class Flow(unittest.TestCase):
    def test_001_flow_downPriorMaterial(self):
        """下载前手资料 V2.1.1新增"""
        payload = {
            "goldenLetterId": "1562982170314465281",
            "projectId": "1585944444477997057"
        }
        r = api_flow_downPriorMaterial(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

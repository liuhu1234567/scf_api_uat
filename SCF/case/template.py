from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json


def api_template_insert(token, payload):
    """【平台方】新增模板"""
    url = f'{api_host}/api-scf/template/insert'
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


g_d = {}


class Template(unittest.TestCase):
    def test_001_template_insert(self):
        """【平台方】新增模板"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 0,
            "size": 0,
            "templateCode": "",
            "templateGroup": "",
            "templateName": "",
            "templateUrl": "",
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_template_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

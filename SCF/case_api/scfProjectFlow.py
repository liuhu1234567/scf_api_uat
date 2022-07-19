from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name
import requests
import unittest
import json

def api_scfProjectFlow_enterFlow(token, payload):
    """【平台方】准入配置-创建流程"""
    url = f'{api_host}/scfProjectFlow/enterFlow'
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


class ScfProjectFlow(unittest.TestCase):
    def test_scfProjectFlow_enterFlow(self):
        """【平台方】准入配置-创建流程"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "customerType": 0,
            "filePaths": [],
            "flowItems": [
                {
                    "customerType": 0,
                    "filePaths": [],
                    "flowItems": [],
                    "isExternal": True,
                    "isProtocol": True,
                    "isPush": True,
                    "name": "",
                    "reportId": 0,
                    "step": 0,
                    "subs": []
                }
            ],
            "isExternal": True,
            "isProtocol": True,
            "isPush": True,
            "name": "",
            "reportId": 0,
            "step": 0,
            "subs": [
                {
                    "filePath": "",
                    "signType": 0
                }
            ]
        }
        r = api_scfProjectFlow_enterFlow(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

from common.global_variable import customize_dict
from common.get_token import token_scf_platform
from common.do_config import api_host, restime
import requests
import json
import unittest


def api_blockchain_info(token, payload):
    """查询区块链信息"""
    url = f'{api_host}/api-scf/blockchain/info'
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


class Blockchain(unittest.TestCase):
    def test_001_blockchain_info(self):
        """【平台方】查询区块链信息"""
        payload = {
            "id": 0
        }
        r = api_blockchain_info(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)
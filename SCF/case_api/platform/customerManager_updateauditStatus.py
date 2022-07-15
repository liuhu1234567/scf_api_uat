from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json

def api_customerManager_updateauditStatus(token, payload):
    """【平台方】修改审核状态"""
    url = f'{api_host}/api-scf/customerManager/update/auditStatus'
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


class CustomerManagerUpdateauditStatus(unittest.TestCase):
    def test_customerManager_updateauditStatus(self):
        """【平台方】修改审核状态"""
        payload = {"auditOpinion": "1", "auditStatus": "100", "id":""}
        r = api_customerManager_updateauditStatus(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

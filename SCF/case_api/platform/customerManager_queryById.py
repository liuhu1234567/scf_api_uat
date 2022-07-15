from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from case_api.platform.customerManager_queryPage import api_customerManager_queryPage
import requests
import unittest
import json

def api_customerManager_queryById(token, payload):
    """【平台方】根据ID查询客户详情"""
    url = f'{api_host}/api-scf/enterprise/queryById'
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


class CustomerManagerQueryById(unittest.TestCase):
    def test_customerManager_queryById(self):
        """【平台方】根据ID查询客户详情"""
        payload_one = {"num": "1", "size": "100"}
        Id = api_customerManager_queryPage(token_scf_supplier, payload_one).json()["datas"][0]["id"]
        payload = {"id": Id}
        r = api_customerManager_queryById(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

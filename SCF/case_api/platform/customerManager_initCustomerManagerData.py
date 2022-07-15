from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest


def api_customerManager_initCustomerManagerData(token):
    """【平台方】初始化客户新增页面列表信息"""
    url = f'{api_host}/api-scf/customerManager/initCustomerManagerData'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    payload = {}
    r = requests.post(url, headers=headers, data=payload)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


class CustomerManagerInitCustomerManagerData(unittest.TestCase):
    def test_customerManager_initCustomerManagerData(self):
        """【平台方】初始化客户新增页面列表信息"""
        r = api_customerManager_initCustomerManagerData(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

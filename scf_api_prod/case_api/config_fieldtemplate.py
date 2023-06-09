from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
import json


def api_config_fieldtemplate_detail(token, payload):
    """详情"""
    url = f'{api_host}/api-scf-data/config/fieldtemplate/detail'
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


def api_config_fieldtemplate_list(token, payload):
    """分页查询列表"""
    url = f'{api_host}/api-scf-data/config/fieldtemplate/list'
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


class ConfigFieldtemplate(unittest.TestCase):
    def test_001_config_fieldtemplate_detail(self):
        """详情"""
        payload = {
            "templateId": 0
        }
        r = api_config_fieldtemplate_detail(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_config_fieldtemplate_list(self):
        """分页查询列表"""
        payload = {
            "createBy": "",
            "createTime": "",
            "id": 0,
            "itemName": "",
            "name": "",
            "num": 1,
            "productName": "",
            "size": 10,
            "tenantName": "",
            "updateBy": "",
            "updateTime": ""
        }
        r = api_config_fieldtemplate_list(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

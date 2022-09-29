from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
import json


def api_dataManager_purchase_getSearchField(token, payload):
    """获取搜索表单数据"""
    url = f'{api_host}/api-scf-data/dataManager/getSearchField'
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

def api_dataManager_purchase_getTableHeader(token, payload):
    """获取表头"""
    url = f'{api_host}/api-scf-data/dataManager/getTableHeader'
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

def api_dataManager_purchase_kind(token):
    """获取采购数据种类"""
    url = f'{api_host}/api-scf-data/dataManager/purchase/kind'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r

g_d = {'id': api_dataManager_purchase_kind(token_scf_supplier).json()['datas'][0]['id']}

class DataManagerPurchase(unittest.TestCase):
    def test_dataManager_purchase_getSearchField(self):
        """获取搜索表单数据"""
        payload = {
            "id": g_d['id']
        }
        r = api_dataManager_purchase_getSearchField(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_dataManager_purchase_getTableHeader(self):
        """获取表头"""
        payload = {
            "id": g_d['id']
        }
        r = api_dataManager_purchase_getTableHeader(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_dataManager_purchase_kind(self):
        """获取采购数据种类"""
        r = api_dataManager_purchase_kind(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

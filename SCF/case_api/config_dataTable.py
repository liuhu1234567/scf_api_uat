from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json


def api_config_dataTable_customerList(token):
    """可查看的客户类型"""
    url = f'{api_host}/api-scf-data/config/dataTable/customerList'
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


def api_config_dataTable_detail(token, payload):
    """数据表详情"""
    url = f'{api_host}/api-scf-data/config/dataTable/detail'
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


def api_config_dataTable_fieldTable(token, payload):
    """根据模板ID查询模板"""
    url = f'{api_host}/api-scf-data/config/dataTable/fieldTable'
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


def api_config_dataTable_list(token, payload):
    """查询数据表列表"""
    url = f'{api_host}/api-scf-data/config/dataTable/list'
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


def api_config_dataTable_save(token, payload):
    """新增数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/save'
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


def api_config_dataTable_templateList_all(token):
    """数据字段来源列表"""
    url = f'{api_host}/api-scf-data/config/dataTable/templateList/all'
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


def api_config_dataTable_update(token, payload):
    """修改数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/update'
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


class ConfigDataTable(unittest.TestCase):
    def test_config_dataTable_customerList(self):
        """可查看的客户类型"""
        r = api_config_dataTable_customerList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_detail(self):
        """数据表详情"""
        payload = {
            "id": 1549312997482921986
        }
        r = api_config_dataTable_detail(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_fieldTable(self):
        """根据模板ID查询模板"""
        payload = {
            "templateId": 1
        }
        r = api_config_dataTable_fieldTable(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_list(self):
        """查询数据表列表"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "institutionName": "",
            "num": 0,
            "productName": "",
            "size": 0,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_config_dataTable_list(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_save(self):
        """新增数据表"""
        payload = {
            "fieldList": [
                {
                    "id": 0,
                    "isEdit": 0,
                    "isSearch": 0,
                    "isShow": 0,
                    "sort": 0
                }
            ],
            "name": "",
            "templateId": 0,
            "tenantType": "",
            "type": 0
        }
        r = api_config_dataTable_save(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_templateList_all(self):
        """数据字段来源列表"""
        r = api_config_dataTable_templateList_all(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_config_dataTable_update(self):
        """修改数据表"""
        payload = {
            "fieldList": [
                {
                    "id": 0,
                    "isEdit": 0,
                    "isSearch": 0,
                    "isShow": 0,
                    "sort": 0
                }
            ],
            "id": 0,
            "name": "",
            "templateId": 0,
            "tenantType": "",
            "type": 0
        }
        r = api_config_dataTable_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

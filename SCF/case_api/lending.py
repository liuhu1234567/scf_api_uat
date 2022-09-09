from common.global_variable import customize_dict
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_config import api_host, restime
import requests
import json
import unittest
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis


def api_lending_save(token, payload):
    """新增"""
    url = f'{api_host}/api-scf/lending/save'
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


def api_lending_findByItem(token, payload):
    """通过项目查询"""
    url = f'{api_host}/api-scf/lending/findByItem'
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


def api_lending_findDataTable(token, payload):
    """获取放款对应数据表"""
    url = f'{api_host}/api-scf/lending/findDataTable'
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


def api_lending_findDataTableContent(token, payload):
    """获取数据表内容"""
    url = f'{api_host}/api-scf/lending/findDataTableContent'
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


def api_lending_update(token, payload):
    """修改"""
    url = f'{api_host}/api-scf/lending/update'
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


def api_lending_detail(token, payload):
    """详情"""
    url = f'{api_host}/api-scf/lending/detail'
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


def api_lending_download(token, payload):
    """放款下载"""
    url = f'{api_host}/api-scf/lending/download'
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


g_d = {}


class Lending(unittest.TestCase):
    def test_001_lending_save(self):
        """【平台方】新增"""
        payload = {
            "data": [
                {}
            ],
            "tableId": 0
        }
        r = api_lending_save(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_lending_findByItem(self):
        """【平台方】通过项目查询"""
        g_d['projectId'] = api_scfProjectBasis_listProjectBasis(token_scf_platform).json()['datas'][0]['id']
        payload = {
            "projectId": g_d.get('projectId')
        }
        r = api_lending_findByItem(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_lending_findDataTable(self):
        """【平台方】获取放款对应数据表"""
        payload = {
            "bankId": 0,
            "coreId": 0,
            "productId": 0,
            "projectId": g_d.get('projectId')
        }
        r = api_lending_findDataTable(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_lending_findDataTableContent(self):
        """【平台方】获取数据表内容"""
        payload = {
            "ctfNum": "",
            "ctfTp": "",
            "tableId": 0
        }
        r = api_lending_findDataTableContent(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_lending_update(self):
        """【平台方】修改"""
        payload = {
            "data": {},
            "id": 0,
            "tableId": 0
        }
        r = api_lending_update(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


    def test_006_lending_detail(self):
        """【平台方】详情"""
        payload = {
            "id": 0
        }
        r = api_lending_detail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_lending_download(self):
        """【平台方】放款下载"""
        payload = {
            "bankId": 0,
            "coreId": 0,
            "productId": 0,
            "projectId": g_d.get('projectId')
        }
        r = api_lending_download(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json
from config.all_path import get_file_path
from common.do_faker import get_number


def api_template_uploadfile(token, file_name):
    """上传文件"""
    url = f'{api_host}/api-scf/template/upload/file'
    headers = {
        "x-appid-header": "2",
        "Authorization": token
    }
    png_path = get_file_path(file_name)
    with open(png_path, 'rb') as f:
        file_b = f.read()
    files = {
        'file': (file_name, file_b, "image/png")
    }
    r = requests.request("POST", url, headers=headers, files=files)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


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


def api_template_get_codeCustomerBase(token):
    """【平台方】批量邀请客户建档模板.xlsx"""
    url = f'{api_host}/api-scf/template/get/codeCustomerBase'
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


def api_template_findTemplates(token, payload):
    """【平台方】查询模板"""
    url = f'{api_host}/api-scf/template/findTemplates'
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


def api_template_find(token, code):
    """【平台方】通过模板 CODE查询"""
    url = f'{api_host}/api-scf/template/find/{code}'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.get(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_template_deleteRole(token, params):
    """【平台方】删除模板"""
    url = f'{api_host}/api-scf/template/deleteRole'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.get(url, headers=headers, params=params)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{params}')
    print(f'接口响应为：{r.text}')
    return r


g_d = {}


class Template(unittest.TestCase):
    def test_001_template_uploadfile(self):
        """【平台方】上传文件"""
        r = api_template_uploadfile(token_scf_supplier, 'test.png')
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(True, r_json['isImg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_template_insert(self):
        """【平台方】新增模板"""
        number = get_number(6)
        url = "http://172.30.206.52:8100/group1/M00/00/29/rB7ONGLU-OGANNSdAAOmhp5bz3w531.png"
        payload = {
            # "createBy": '',
            # "createTime": "",
            # "id": '',
            # "num": 1,
            # "size": 10,
            "templateCode": f"模板标识{number}",
            "templateGroup": f"模板组名{number}",
            "templateName": f"模板名称{number}",
            "templateUrl": url,
            # "updateBy": '',
            # "updateTime": ""
        }
        r = api_template_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_template_get_codeCustomerBase(self):
        """【平台方】批量邀请客户建档模板.xlsx"""
        r = api_template_get_codeCustomerBase(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_template_findTemplates(self):
        """【平台方】查询模板"""
        payload = {
            "createBy": "",
            "createTime": "",
            "id": "",
            "num": 1,
            "size": 10,
            "templateCode": "",
            "templateGroup": "",
            "templateName": "",
            "templateUrl": "",
            "updateBy": "",
            "updateTime": ""
        }
        r = api_template_findTemplates(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_template_find(self):
        """【平台方】通过模板CODE查询"""
        code = ''
        r = api_template_find(token_scf_supplier, code)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_template_deleteRole(self):
        """【平台方】删除模板"""
        params = {"id": ''}
        r = api_template_deleteRole(token_scf_supplier, params)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

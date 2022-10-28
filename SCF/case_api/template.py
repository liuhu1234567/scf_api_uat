from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
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

def api_template_get_codeBillBase(token, params):
    """导入发票模板.xlsx"""
    url = f'{api_host}/api-scf/template/get/codeBillBase'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, params=params)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{params}')
    print(f'接口响应为：{r.text}')
    return r


g_d = {}


# class Template(unittest.TestCase):
#     def test_001_template_uploadfile(self):
#         """【平台方】上传文件"""
#         r = api_template_uploadfile(token_scf_supplier, 'test.png')
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_002_template_get_codeCustomerBase(self):
#         """【平台方】批量邀请客户建档模板.xlsx"""
#         r = api_template_get_codeCustomerBase(token_scf_supplier)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')
#
#     def test_003_template_get_codeBillBase(self):
#         """导入发票模板.xlsx"""
#         params = {
#         }
#         r = api_template_get_codeBillBase(token_scf_platform, params)
#         r_json = r.json()
#         restime_now = r.elapsed.total_seconds()
#         customize_dict['restime_now'] = restime_now
#         self.assertEqual(200, r_json['resp_code'])
#         self.assertEqual('SUCCESS', r_json['resp_msg'])
#         self.assertLessEqual(restime_now, restime, 'Test api timeout')

from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from config.all_path import get_file_path
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasisByType
import requests
import unittest
import json

"""公共接口"""


def api_otherApi_initDropdownListInfo(token, payload):
    """枚举下拉列表信息集"""
    url = f'{api_host}/api-scf/otherApi/initDropdownListInfo'
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


def api_otherApi_queryById(token, payload):
    """根据传入的ID集返回名称详情"""
    url = f'{api_host}/api-scf/otherApi/queryById'
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


def api_otherApi_queryDownList(token, payload):
    """项目列表，核心企业，金融产品，金融机构下拉列表"""
    url = f'{api_host}/api-scf/otherApi/queryDownList'
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


def api_otherApi_queryProjectInfo(token, payload):
    """服务-查询项目相关信息"""
    url = f'{api_host}/api-scf/otherApi/queryProjectInfo'
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


def api_template_upload_file(token, file_name):
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
        'file': (file_name, file_b, "png")
    }
    r = requests.post(url, headers=headers, files=files)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


class OtherApi(unittest.TestCase):
    def test_001_otherApi_initDropdownListInfo(self):
        """【平台方】枚举下拉列表信息集"""
        payload = {
        }
        r = api_otherApi_initDropdownListInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_otherApi_queryById(self):
        """【平台方】根据传入的ID集返回名称详情"""
        payload = [
            {
                "institutionId": 0,
                "itemId": 0,
                "productId": 0,
                "templateId": 0,
                "tenantId": 0
            }
        ]
        r = api_otherApi_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_otherApi_queryDownList(self):
        """【平台方】项目列表，核心企业，金融产品，金融机构下拉列表"""
        payload = {
        }
        r = api_otherApi_queryDownList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_otherApi_queryProjectInfo(self):
        """【平台方】服务-查询项目相关信息"""
        payload = {
            "businessType": ""
        }
        itemId = api_scfProjectBasis_listProjectBasisByType(token_scf_platform, payload).json()["datas"][0]["id"]
        payload = {
            "itemId": itemId
        }
        r = api_otherApi_queryProjectInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_005_template_upload_file(self):
    #     """【平台方】上传文件"""
    #     r = api_template_upload_file(token_scf_platform, "test.png")
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

from common.do_config import api_host, restime
from common.do_excel import DoExcel
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from case_api.template import api_template_uploadfile
import requests
import unittest
import json
import random
from common.do_faker import get_number, get_name, get_phone, get_email, get_company


def api_customerManager_importCustomerFromExcel(token, payload):
    """【平台方】客户管理-导入用户数据"""
    url = f'{api_host}/api-scf/customerManager/importCustomerFromExcel'
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


def api_customerManager_insert(token, payload):
    """【平台方】客户新增"""
    url = f'{api_host}/api-scf/customerManager/insert'
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


def api_customerManager_queryAuditPage(token, payload):
    """分页查询客户审核列表"""
    url = f'{api_host}/api-scf/customerManager/queryAuditPage'
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


def api_customerManager_queryPage(token, payload):
    """【平台方】分页查询客户列表"""
    url = f'{api_host}/api-scf/customerManager/queryPage'
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


def api_customerManager_update_auditStatus(token, payload):
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


def insert_excel_importCustomerFromExcel(num):
    excel = DoExcel('批量导入客户.xlsx', '批量邀请客户建档模板')
    for n in range(num):
        row_value = (
            n + 1,
            get_company(),
            get_number(10),
            get_name(),
            get_phone(),
            get_email(),
            random.choice(['核心企业', '供应商', '经销商', '银行', '保理商'])
        )
        excel.insert(row_value, 3+n)
    file_name = excel.save()
    return file_name


g_d = {}


class CustomerManager(unittest.TestCase):
    def test_001_customerManager_importCustomerFromExcel(self):
        """【平台方】客户管理-导入用户数据"""
        file_name = insert_excel_importCustomerFromExcel(4)
        path = api_template_uploadfile(token_scf_platform, file_name).json()['datas']['path']
        fileId = "group1/" + path
        payload = {
            "fileId": fileId
        }
        r = api_customerManager_importCustomerFromExcel(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_customerManager_insert(self):
        """【平台方】客户新增"""
        payload = {
            "auditStatus": 0,
            "channel": 1,
            "contact": get_name(),
            "contactEmail": get_email(),
            "contactMobile": get_phone(),
            "coreEnterprise": "",
            "creditCode": get_number(10),
            "customerType": 0,
            "entName": get_company()
        }
        r = api_customerManager_insert(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_customerManager_queryAuditPage(self):
        """分页查询客户审核列表"""
        payload = {
            "auditStatus": 0,
            "contact": "",
            "contactMobile": "",
            "entName": "",
            "num": 1,
            "size": 10
        }
        r = api_customerManager_queryAuditPage(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_customerManager_queryById(self):
        """【平台方】根据ID查询客户详情"""
        payload = {"id": g_d.get('id')}
        r = api_customerManager_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_customerManager_queryPage(self):
        """【平台方】分页查询客户列表"""
        payload = {
            "auditStatus": 0,
            "contact": "",
            "contactMobile": "",
            "customerType": 0,
            "entName": "",
            "num": 1,
            "size": 10
        }
        r = api_customerManager_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_customerManager_updateauditStatus(self):
        """【平台方】修改审核状态"""
        payload = {
            "auditOpinion": "通过啦",
            "auditStatus": 3,
            "id": g_d.get('id')
        }
        r = api_customerManager_update_auditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

from common.global_variable import customize_dict
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from case_api.template import api_template_uploadfile
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
from case_api.backAccount import api_backAccount_queryPage, api_backAccount_bindByProjectId
from common.do_config import api_host, restime
import requests
import json
import unittest
from common.do_excel import DoExcel
from common.do_faker import get_number
from jsonpath import jsonpath
import datetime


def api_orderLoan_import(token, payload):
    """导入"""
    url = f'{api_host}/api-scf/orderLoan/import'
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


def api_orderLoan_list(token, payload):
    """列表"""
    url = f'{api_host}/api-scf/orderLoan/list'
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


def api_orderLoan_export(token, payload):
    """下载"""
    url = f'{api_host}/api-scf/orderLoan/export'
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


def api_orderLoan_projectList(token, payload):
    """项目下拉列表"""
    url = f'{api_host}/api-scf/orderLoan/projectList'
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


def api_orderLoan_financing(token, payload):
    """融资"""
    url = f'{api_host}/api-scf/orderLoan/financing'
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


def api_orderLoan_revoke(token, payload):
    """撤回"""
    url = f'{api_host}/api-scf/orderLoan/revoke'
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


def api_orderLoan_review(token, payload):
    """审核"""
    url = f'{api_host}/api-scf/orderLoan/review'
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


def api_orderLoan_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/orderLoan/resubmit'
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


def api_orderLoan_detail(token, payload):
    """详情"""
    url = f'{api_host}/api-scf/orderLoan/detail'
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


def insert_excel_importOrderFromExcel(num):
    sellCompany = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['entName']
    excel = DoExcel('订单贷导入模板.xlsx', 'Sheet1')
    for n in range(num):
        row_value = (
            n + 1,
            get_number(10),
            f"订单名称{get_number(6)}",
            '接口自动化核心企业账号',
            sellCompany,
            '',
            '',
            '',
            '',
            '',
            '人民币',
            '',
            '',
            '',
            10000 + n,
            datetime.date.today() + datetime.timedelta(days=30),
        )
        excel.insert(row_value, 3 + n)
    file_name = excel.save()
    return file_name


g_d = {}


class OrderLoan(unittest.TestCase):
    def test_001_orderLoan_import(self):
        """【供应商】导入"""
        file_name = insert_excel_importOrderFromExcel(3)
        path = api_template_uploadfile(token_scf_platform, file_name).json()['datas']['path']
        fileId = "group1/" + path
        payload = {
            "fileId": fileId
        }
        r = api_orderLoan_import(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_orderLoan_list(self):
        """【供应商】列表"""
        payload = {
            "num": 1,
            "size": 10,
        }
        r = api_orderLoan_list(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        orderIds = jsonpath(r_json, '$..id')
        g_d['orderIds'] = orderIds
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_orderLoan_export(self):
        """【供应商】下载"""
        payload = {
            "orderIds": g_d['orderIds']
        }
        r = api_orderLoan_export(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_orderLoan_projectList(self):
        """【供应商】项目下拉列表"""
        payload = {
            "orderId": g_d['orderIds'][0]
        }
        r = api_orderLoan_projectList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        datas = r_json['datas']
        g_d['projectId'] = r_json['datas'][len(datas)-1]['id']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_orderLoan_financing(self):
        """【供应商】融资"""
        payload = {
            "num": 1,
            "size": 10,
        }
        bankCardInfo = api_backAccount_queryPage(token_scf_supplier, payload).json()["datas"]
        bankCardId = bankCardInfo[0]['id']
        bankAccountNo = bankCardInfo[0]['bankAccountNo']
        payload = {
            "id": bankCardId,
            "projectId": g_d['projectId']
        }
        r = api_backAccount_bindByProjectId(token_scf_supplier, payload)
        payload = {
            "financeAmount": 1000,
            "financingEnd": "2023-09-10",
            "financingStart": "2022-09-10",
            "id": g_d['orderIds'][0],
            "increaseTrustId": "",
            "projectId": g_d['projectId'],
            "receiveBankAccount": bankAccountNo
        }
        r = api_orderLoan_financing(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_orderLoan_revoke(self):
        """【供应商】撤回"""
        payload = {
            "auditFlowItemId": 0,
            "id": 0
        }
        r = api_orderLoan_revoke(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_orderLoan_review(self):
        """【供应商】审核"""
        payload = {
            "auditEntId": 0,
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 0,
            "busType": "",
            "creditEnhancerId": 0,
            "entId": 0,
            "id": 0,
            "projectId": 0
        }
        r = api_orderLoan_review(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_orderLoan_resubmit(self):
        """【供应商】重新提交"""
        payload = {
            "auditFlowItemId": 0,
            "financeAmount": 0,
            "financingEnd": "",
            "financingStart": "",
            "id": 0,
            "increaseTrustId": 0,
            "receiveBankAccount": ""
        }
        r = api_orderLoan_resubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_orderLoan_detail(self):
        """【供应商】详情"""
        payload = {
            "id": 0
        }
        r = api_orderLoan_detail(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

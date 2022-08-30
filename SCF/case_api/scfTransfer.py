from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_enterprise, token_scf_supplier
from common.global_variable import customize_dict
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
from common.do_faker import get_number
import requests
import unittest
import json

"""转让"""


def api_scfTransfer_audit(token, payload):
    """审核"""
    url = f'{api_host}/api-scf/scfTransfer/audit'
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


def api_scfTransfer_detail(token, payload):
    """转让详情"""
    url = f'{api_host}/api-scf/scfTransfer/detail'
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


def api_scfTransfer_listCoreSub(token, payload):
    """获取核企子公司"""
    url = f'{api_host}/api-scf/scfTransfer/listCoreSub'
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


def api_scfTransfer_listGuarantor(token, payload):
    """获取担保方"""
    url = f'{api_host}/api-scf/scfTransfer/listGuarantor'
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


def api_scfTransfer_reSubmit(token, payload):
    """转让重新提交"""
    url = f'{api_host}/api-scf/scfTransfer/reSubmit'
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


def api_scfTransfer_searchNotSupplier(token, payload):
    """转让列表-非供应商"""
    url = f'{api_host}/api-scf/scfTransfer/searchNotSupplier'
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


def api_scfTransfer_searchSupplier(token, payload):
    """转让列表-供应商"""
    url = f'{api_host}/api-scf/scfTransfer/searchSupplier'
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


def api_scfTransfer_selectReceiver(token, payload):
    """查询接收人"""
    url = f'{api_host}/api-scf/scfTransfer/selectReceiver'
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


def api_scfTransfer_sign(token, payload):
    """签收"""
    url = f'{api_host}/api-scf/scfTransfer/sign'
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


def api_scfTransfer_toAudit(token, payload):
    """跳转至审核页面"""
    url = f'{api_host}/api-scf/scfTransfer/toAudit'
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


def api_scfTransfer_toResumit(token, payload):
    """跳转至重新提交页面"""
    url = f'{api_host}/api-scf/scfTransfer/toResumit'
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


def api_scfTransfer_toSign(token, payload):
    """跳转至签收页面"""
    url = f'{api_host}/api-scf/scfTransfer/toSign'
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


def api_scfTransfer_toTransfer(token, payload):
    """跳转至转让页面.入参：金点信记录ID"""
    url = f'{api_host}/api-scf/scfTransfer/toTransfer'
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


def api_scfTransfer_transfer(token, payload):
    """保存转让信息"""
    url = f'{api_host}/api-scf/scfTransfer/transfer'
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


g_d = {}


class ScfTransfer(unittest.TestCase):
    def test_001_scfTransfer_audit(self):
        """审核"""
        payload = {
            "auditEntId": 0,
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 0,
            "busType": "",
            "entId": 0,
            "id": 0,
            "projectId": 0
        }
        r = api_scfTransfer_audit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfTransfer_detail(self):
        """转让详情"""
        payload = {
            "id": 0
        }
        r = api_scfTransfer_detail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfTransfer_listCoreSub(self):
        """获取核企子公司"""
        payload = {
        }
        r = api_scfTransfer_listCoreSub(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfTransfer_listGuarantor(self):
        """获取担保方"""
        payload = {
        }
        r = api_scfTransfer_listGuarantor(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfTransfer_reSubmit(self):
        """转让重新提交"""
        payload = {
            "bills": [],
            "creditEnhancement": "",
            "id": 0,
            "invoiceWithTax": "",
            "orderName": "",
            "orderNumber": "",
            "receiver": 0,
            "statementNumber": "",
            "transferAmount": "",
            "transferId": 0,
            "transferIntroduce": ""
        }
        r = api_scfTransfer_reSubmit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfTransfer_searchNotSupplier(self):
        """转让列表-非供应商"""
        payload = {
            "bills": [],
            "creditEnhancement": "",
            "id": 0,
            "invoiceWithTax": "",
            "orderName": "",
            "orderNumber": "",
            "receiver": 0,
            "statementNumber": "",
            "transferAmount": "",
            "transferId": 0,
            "transferIntroduce": ""
        }
        r = api_scfTransfer_searchNotSupplier(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfTransfer_searchSupplier(self):
        """转让列表-供应商"""
        payload = {
            "currentHolder": "",
            "founderEnt": "",
            "goldenLetterCode": "",
            "num": 1,
            "paymentStatus": 0,
            "size": 10
        }
        r = api_scfTransfer_searchSupplier(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_scfTransfer_selectReceiver(self):
        """查询接收人"""
        payload = {
        }
        r = api_scfTransfer_selectReceiver(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_scfTransfer_sign(self):
        """签收"""
        payload = {
            "id": 1564090769279369218
        }
        r = api_scfTransfer_sign(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_scfTransfer_toAudit(self):
        """跳转至审核页面"""
        payload = {
            "id": 0
        }
        r = api_scfTransfer_toAudit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_scfTransfer_toResumit(self):
        """跳转至重新提交页面"""
        payload = {
            "id": 0
        }
        r = api_scfTransfer_toResumit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_scfTransfer_toSign(self):
        """跳转至签收页面"""
        payload = {
            "id": 0
        }
        r = api_scfTransfer_toSign(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_013_scfTransfer_toTransfer(self):
        """跳转至转让页面.入参：金点信记录ID"""
        payload = {
            "id": 1564090769279369218
        }
        r = api_scfTransfer_toTransfer(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_014_scfTransfer_transfer(self):
        """【供应商】发起转让保存转让信息"""
        g_d["coreSub"] = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()["datas"]["id"]
        payload = {
            "bills": ["1562284267547848706"],
            "coreSub": g_d.get("coreSub"),
            "creditEnhancerId": 0,
            "id": 1564090769279369218,
            "invoiceWithTax": "1000",
            "orderName": "合同/订单名称",
            "orderNumber": "合同/订单编号",
            "receiver": 1563001484513939458,
            "statementNumber": "对账单编号",
            "transferAmount": "	转让金额",
            "transferIntroduce": "转让说明"
        }
        r = api_scfTransfer_transfer(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

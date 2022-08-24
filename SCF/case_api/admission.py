from common.global_variable import customize_dict
from common.get_token import token_scf_supplier, token_scf_financier
from common.do_config import api_host, restime
import requests
import json
import unittest


def api_admission_queryBuyerList(token, payload):
    """买方列表，即核心企业子公司"""
    url = f'{api_host}/api-scf/admission/queryBuyerList'
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


def api_admission_insert(token, payload):
    """新增"""
    url = f'{api_host}/api-scf/admission/insert'
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


def api_admission_queryByEntId(token, payload):
    """根据企业ID查询企业详情"""
    url = f'{api_host}/api-scf/admission/queryByEntId'
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


def api_admission_queryById(token, payload):
    """根据ID查询准入申请详情"""
    url = f'{api_host}/api-scf/admission/queryById'
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


def api_admission_queryConfigSet(token, payload):
    """根据项目id查询基础项配置,准入配置,流程配置"""
    url = f'{api_host}/api-scf/admission/queryConfigSet'
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


def api_admission_queryDownList(token, payload):
    """项目列表，核心企业，金融产品，金融机构下拉列表"""
    url = f'{api_host}/api-scf/admission/queryDownList'
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


def api_admission_queryPage(token, payload):
    """分页查询准入申请列表"""
    url = f'{api_host}/api-scf/admission/queryPage'
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


def api_admission_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/admission/resubmit'
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


def api_admission_queryAuditPage(token, payload):
    """分页查询准入审批列表"""
    url = f'{api_host}/api-scf/admission/queryAuditPage'
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


def api_admission_update_auditStatus(token, payload):
    """审核"""
    url = f'{api_host}/api-scf/admission/update/auditStatus'
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


class Admission(unittest.TestCase):
    def test_001_admission_queryBuyerList(self):
        """【供应商】买方列表，即核心企业子公司"""
        payload = {
            "coreEntId": 0,
            "coreEntName": "",
            "num": 0,
            "size": 0
        }
        r = api_admission_queryBuyerList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_admission_insert(self):
        """【供应商】新增"""
        payload = {
            "buyerEntId": 0,
            "buyerEntName": "",
            "coreEntId": 0,
            "coreEntName": "",
            "creditCode": "",
            "entId": 0,
            "entName": "",
            "financeId": 0,
            "financeName": "",
            "productId": 0,
            "productName": "",
            "projectId": 0,
            "projectName": ""
        }
        r = api_admission_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_admission_queryByEntId(self):
        """【供应商】根据企业ID查询企业详情"""
        payload = {
            "id": 0
        }
        r = api_admission_queryByEntId(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_admission_queryById(self):
        """【供应商】根据ID查询准入申请详情"""
        payload = {
            "id": 0
        }
        r = api_admission_queryById(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_admission_queryConfigSet(self):
        """【供应商】根据项目id查询基础项配置,准入配置,流程配置"""
        payload = {
            "id": 0
        }
        r = api_admission_queryConfigSet(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_admission_queryDownList(self):
        """【供应商】根据项目id查询基础项配置,准入配置,流程配置"""
        payload = {}
        r = api_admission_queryDownList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_admission_queryDownList(self):
        """【供应商】分页查询准入申请列表"""
        payload = {
            "num": 1,
            "size": 10
        }
        r = api_admission_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_admission_resubmit(self):
        """【供应商】重新提交"""
        payload = {
            "auditFlowItemId": 0,
            "buyerEntId": 0,
            "buyerEntName": ""
        }
        r = api_admission_resubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_admission_queryAuditPage(self):
        """【资金方】分页查询准入审批列表"""
        payload = {
            # "auditStatus": 3,   # 审核通过:3，审核拒绝:4，审核退回:5，已撤销:6
            "num": 1,
            "size": 10
        }
        r = api_admission_queryAuditPage(token_scf_financier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_admission_update_auditStatus(self):
        """【资金方】审核"""
        payload = {
            "auditEntId": 0,
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 0,
            "busType": "",
            "creditEnhancerId": 0,
            "entId": 0,
            "id": 0,
            "projectId": 0,
            "recipientId": 0
        }
        r = api_admission_update_auditStatus(token_scf_financier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)



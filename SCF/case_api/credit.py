from common.global_variable import customize_dict
from common.get_token import token_scf_supplier, token_scf_financier, token_scf_platform
from common.do_config import api_host, restime
import random
import requests
import json
import unittest
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis


def api_credit_insert(token, payload):
    """新增授信"""
    url = f'{api_host}/api-scf/credit/insert'
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


def api_credit_queryConfigSet(token, payload):
    """根据项目id查询基础项配置,授信配置,流程配置"""
    url = f'{api_host}/api-scf/credit/queryConfigSet'
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

def api_credit_update(token, payload):
    """修改授信"""
    url = f'{api_host}/api-scf/credit/update'
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


def api_credit_queryPage(token, payload):
    """分页查询授信"""
    url = f'{api_host}/api-scf/credit/queryPage'
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


def api_credit_queryAuditPage(token, payload):
    """分页查询审核授信"""
    url = f'{api_host}/api-scf/credit/queryAuditPage'
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


def api_credit_update_auditStatus(token, payload):
    """审核"""
    url = f'{api_host}/api-scf/credit/update/auditStatus'
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


def api_credit_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/credit/resubmit'
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


def api_credit_get(token, payload):
    """获取授信"""
    url = f'{api_host}/api-scf/credit/get'
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


def api_credit_getCreditAmount(token, payload):
    """获取授信额度"""
    url = f'{api_host}/api-scf/credit/getCreditAmount'
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


def api_credit_delete(token, payload):
    """删除授信"""
    url = f'{api_host}/api-scf/credit/delete'
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


class Credit(unittest.TestCase):
    def test_001_credit_insert(self):
        """【供应商】新增授信"""
        supplierDatas = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']
        creditApplyCardId = supplierDatas['creditCode']
        financierDatas = api_enterprise_queryEntArchivesDetail(token_scf_financier).json()['datas']
        creditId = financierDatas['id']
        creditName = financierDatas['entName']
        projectId = api_scfProjectBasis_listProjectBasis(token_scf_supplier).json()['datas'][0]['id']
        payload = {
            "creditApplyCardId": creditApplyCardId,
            "creditCardIdType": 1,
            "creditId": creditId,
            "creditName": creditName,
            "creditScope": 1,
            "creditType": random.randint(1, 2),
            "enterprise": "",
            "enterpriseId": 1111,
            "financialInstitutionName": "",
            "financialProductId": 1,
            "financialProductName": "",
            "projectId": projectId,
            "projectName": ""
        }
        r = api_credit_insert(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_credit_insert(self):
        """【供应商】根据项目id查询基础项配置,授信配置,流程配置"""
        id = api_scfProjectBasis_listProjectBasis(token_scf_supplier).json()['datas'][0]['id']
        payload = {
            "id": id
        }
        r = api_credit_queryConfigSet(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_credit_update(self):
        """【供应商】修改授信"""
        payload = {
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 0,
            "createBy": "",
            "createTime": "",
            "creditApplyCardId": "授信申请人证件号码",
            "creditApplyName": "授信申请人名称",
            "creditCardIdType": 1,
            "creditCode": "",
            "creditId": 1,
            "creditName": "授信方名称",
            "creditScope": 1,
            "creditType": 1,
            "enterprise": "核心企业",
            "enterpriseId": 1111,
            "financialInstitutionName": "金融机构名称",
            "financialProductId": 1,
            "financialProductName": "金融产品名称",
            "id": g_d.get('id'),
            "projectId": 1,
            "projectName": "项目名称",
            "updateBy": "",
            "updateTime": ""
        }
        r = api_credit_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_credit_queryPage(self):
        """【供应商】分页查询授信"""
        payload = {
            "auditStatus": 0,
            "createBy": 0,
            "createTime": "",
            "creditApplyName": "",
            "financialInstitutionName": "",
            "financialProductName": "",
            "id": 0,
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_credit_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_credit_queryAuditPage(self):
        """【平台方】分页查询审核授信"""
        payload = {
            "auditStatus": 0,
            "createBy": 0,
            "createTime": "",
            "creditApplyName": "",
            "financialInstitutionName": "",
            "financialProductName": "",
            "id": 0,
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_credit_queryAuditPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_credit_update_auditStatus(self):
        """【平台方】审核"""
        payload = {
            "auditEntId": 0,
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 0,
            "busType": "",
            "entId": 0,
            "id": g_d.get('id'),
            "projectId": 0
        }
        r = api_credit_update_auditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_credit_resubmit(self):
        """【供应商】重新提交"""
        payload = {
            "auditFlowItemId": 0
        }
        r = api_credit_resubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_credit_get(self):
        """【供应商】获取授信"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_credit_get(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_credit_getCreditAmount(self):
        """【供应商】获取授信额度"""
        payload = {
            "creditId": 0,
            "projectId": 0,
            "tenantId": 0
        }
        r = api_credit_getCreditAmount(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_credit_delete(self):
        """【平台方】删除授信"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_credit_delete(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

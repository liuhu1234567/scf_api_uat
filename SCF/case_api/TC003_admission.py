from common.global_variable import customize_dict
from common.get_token import token_scf_supplier, token_scf_financier, token_scf_enterprise, token_scf_platform
from common.do_config import api_host, restime
import requests
import json
import unittest
from enterprise import api_enterprise_queryEntArchivesDetail, api_admission_queryBuyerList
from TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis

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


g_d = {}


class Admission(unittest.TestCase):

    def test_001_admission_queryDownList(self):
        """【供应商】项目列表，核心企业，金融产品，金融机构下拉列表"""
        payload = {}
        r = api_admission_queryDownList(token_scf_supplier, payload)
        r_json = r.json()
        g_d['projectId'] = r_json['datas']['listProject'][0]['id']
        g_d['projectName'] = r_json['datas']['listProject'][0]['name']
        g_d['productId'] = r_json['datas']['listFinanceProduct'][0]['id']
        g_d['productName'] = r_json['datas']['listFinanceProduct'][0]['name']
        g_d['financeId'] = r_json['datas']['listBank'][0]['id']
        g_d['financeName'] = r_json['datas']['listBank'][0]['name']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_admission_queryPage(self):
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

    def test_003_admission_queryConfigSet(self):
        """【供应商】根据项目id查询基础项配置,准入配置,流程配置"""
        id = api_scfProjectBasis_listProjectBasis(token_scf_supplier).json()['datas'][0]['id']
        payload = {
            "id": id
        }
        r = api_admission_queryConfigSet(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_admission_insert(self):
        """【供应商】新增"""
        creditCode = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['creditCode']
        g_d['entId'] = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['id']
        entName = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['entName']
        coreEntId = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['id']
        coreEntName = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['entName']
        payload = {
            "coreEntName": coreEntName,
        }
        g_d['buyerEntId'] = api_admission_queryBuyerList(token_scf_supplier, payload).json()['datas'][0]['id']
        g_d['buyerEntName'] = api_admission_queryBuyerList(token_scf_supplier, payload).json()['datas'][0]['entName']
        payload = {
            "buyerEntId": g_d.get('buyerEntId'),
            "buyerEntName": g_d.get('buyerEntName'),
            "coreEntId": coreEntId,
            "coreEntName": coreEntName,
            "creditCode": creditCode,
            "entId": g_d.get('entId'),
            "entName": entName,
            "financeId": g_d.get('financeId'),
            "financeName": g_d.get('financeName'),
            "productId": g_d.get('productId'),
            "productName": g_d.get('productName'),
            "projectId": g_d.get('projectId'),
            "projectName": g_d.get('projectName')
        }
        r = api_admission_insert(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_admission_queryByEntId(self):
        """【供应商】根据企业ID查询企业详情"""
        payload = {
            "id": g_d.get('entId')
        }
        r = api_admission_queryByEntId(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_admission_queryById(self):
        """【供应商】根据ID查询准入申请详情"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_admission_queryById(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_admission_resubmit(self):
        """【供应商】重新提交"""
        payload = {
            "auditFlowItemId": 0,
            "buyerEntId": g_d.get('buyerEntId'),
            "buyerEntName": g_d.get('buyerEntName')
        }
        r = api_admission_resubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_admission_queryAuditPage(self):
        """【平台方】分页查询准入审批列表"""
        payload = {
            "auditStatus": 1,
            "entName": "",
            "financeName": "",
            "num": 1,
            "productName": "",
            "size": 10
        }
        r = api_admission_queryAuditPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_admission_update_auditStatus(self):
        """【平台方】审核"""
        payload = {
            "auditEntId": 1,
            "auditFlowItemId": 2,
            "auditOpinion": "",
            "auditStatus": 0,
            "busType": "",
            "creditEnhancerId": 0,
            "entId": 0,
            "id": g_d.get('id'),
            "projectId": 0,
            "recipientId": 0
        }
        r = api_admission_update_auditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

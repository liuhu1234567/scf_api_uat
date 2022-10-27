from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
from common.do_faker import get_number
from case_api.TC004_credit import api_credit_queryPage
from case_api.enterprise import api_enterprise_queryEntArchivesDetailNonCache
import json

"""授信结果表管理控制层"""


def api_credit_result_insert(token, payload):
    """新增授信结果"""
    url = f'{api_host}/api-scf/credit/result/insert'
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


def api_credit_result_queryPage(token, payload):
    """分页查询"""
    url = f'{api_host}/api-scf/credit/result/queryPage'
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


def api_credit_result_getCreditAmount(token, payload):
    """获取授信额度"""
    url = f'{api_host}/api-scf/credit/result/getCreditAmount'
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


def api_credit_result_get(token, payload):
    """获取"""
    url = f'{api_host}/api-scf/credit/result/get'
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


# def api_credit_result_useCreditAmount(token, payload):
#     """使用授信额度"""
#     url = f'{api_host}/api-scf/credit/result/useCreditAmount'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "2",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r


def api_credit_result_delete(token, payload):
    """删除"""
    url = f'{api_host}/api-scf/credit/result/delete'
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


def api_credit_result_enabled(token, payload):
    """授信结果启用"""
    url = f'{api_host}/api-scf/credit/result/enabled'
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


class CreditResult(unittest.TestCase):
    def test_001_credit_result_insert(self):
        """【平台方】新增授信结果"""
        payload = {
            "creditName": "",
            "creditApplyName": "",
            "financialProductName": "",
            "auditStatus": 3,
            "num": 1,
            "size": 10
        }
        creditQueryPage = api_credit_queryPage(token_scf_supplier, payload).json()['datas'][0]
        g_d['creditApplyCardId'] = creditQueryPage['creditApplyCardId']
        g_d['creditApplyName'] = creditQueryPage['creditApplyName']
        g_d['creditId'] = creditQueryPage['creditId']
        g_d['creditName'] = creditQueryPage['creditName']
        g_d['enterprise'] = creditQueryPage['enterprise']
        g_d['enterpriseId'] = creditQueryPage['enterpriseId']
        g_d['financialInstitutionId'] = creditQueryPage['financialInstitutionId']
        g_d['financialInstitutionName'] = creditQueryPage['financialInstitutionName']
        g_d['financialProductId'] = creditQueryPage['financialProductId']
        g_d['financialProductName'] = creditQueryPage['financialProductName']
        g_d['projectId'] = creditQueryPage['projectId']
        g_d['projectName'] = creditQueryPage['projectName']
        g_d['tenantId'] = api_enterprise_queryEntArchivesDetailNonCache(token_scf_supplier).json()['datas']['id']
        payload = {
            "auditAmount": 10000,
            "creditApplyCardId": g_d.get('creditApplyCardId'),
            "creditApplyName": g_d.get('creditApplyName'),
            "creditCardIdType": 1,
            "creditId": g_d.get('creditId'),
            "creditName": g_d.get('creditName'),
            "creditScope": 1,
            "creditType": 1,
            "dataUuid": f"dataUuid{get_number(10)}",
            "enterprise": g_d.get('enterprise'),
            "enterpriseId": g_d.get('enterpriseId'),
            "financialInstitutionId": g_d.get('financialInstitutionId'),
            "financialInstitutionName": g_d.get('financialInstitutionName'),
            "financialProductId": g_d.get('financialProductId'),
            "financialProductName": g_d.get('financialProductName'),
            "loanBegin": "2022-09-30 00:00:00",
            "loanEnd": "2023-09-30 00:00:00",
            "projectId": g_d.get('projectId'),
            "projectName": g_d.get('projectName'),
            "tenantId": g_d.get('tenantId'),
        }
        r = api_credit_result_insert(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_credit_result_queryPage(self):
        """【供应商】分页查询"""
        payload = {
            "num": 1,
            "size": 10,
            "productName": "",
            "financeName": "",
            "isApply": ""
        }
        r = api_credit_result_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_credit_result_getCreditAmount(self):
        """【供应商】获取授信额度"""
        payload = {
            "creditId": g_d.get('creditId'),
            "projectId": g_d.get('projectId'),
            "tenantId": g_d.get('tenantId')
        }
        r = api_credit_result_getCreditAmount(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_credit_result_get(self):
        """【供应商】获取"""
        payload = {
            "id": g_d.get('id'),
        }
        r = api_credit_result_get(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_005_credit_result_useCreditAmount(self):
    #     """【供应商】使用授信额度"""
    #     payload = {
    #         "creditId": g_d.get('creditId'),
    #         "orderId": 1585449468973563906,
    #         "projectId": g_d.get('projectId'),
    #         "tenantId": g_d.get('tenantId'),
    #         "userAmount": 0,
    #         "userAmountStastus": 0
    #     }
    #     r = api_credit_result_useCreditAmount(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_credit_result_delete(self):
        """【平台方】删除"""
        payload = {
            "auditAmount": 10000,
            "creditApplyCardId": g_d.get('creditApplyCardId'),
            "creditApplyName": g_d.get('creditApplyName'),
            "creditCardIdType": 1,
            "creditId": g_d.get('creditId'),
            "creditName": g_d.get('creditName'),
            "creditScope": 1,
            "creditType": 1,
            "dataUuid": f"dataUuid{get_number(10)}",
            "enterprise": g_d.get('enterprise'),
            "enterpriseId": g_d.get('enterpriseId'),
            "financialInstitutionId": g_d.get('financialInstitutionId'),
            "financialInstitutionName": g_d.get('financialInstitutionName'),
            "financialProductId": g_d.get('financialProductId'),
            "financialProductName": g_d.get('financialProductName'),
            "loanBegin": "2022-09-30 00:00:00",
            "loanEnd": "2023-09-30 00:00:00",
            "projectId": g_d.get('projectId'),
            "projectName": g_d.get('projectName'),
            "tenantId": g_d.get('tenantId'),
        }
        id = api_credit_result_insert(token_scf_platform, payload).json()['datas']
        payload = {
            "id": id
        }
        r = api_credit_result_delete(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_007_credit_result_enabled(self):
    #     """【供应商】授信结果启用"""
    #     payload = {
    #         "creditId": 0,
    #         "creditResultId": 0,
    #         "projectId": 0
    #     }
    #     r = api_credit_result_enabled(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

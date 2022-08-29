from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_company
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis
import requests
import unittest
import json

"""融资保理控制层"""


def api_financialFactoring_insert(token, payload):
    """新增"""
    url = f'{api_host}/api-scf/financialFactoring/insert'
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


def api_financialFactoring_queryById(token, payload):
    """根据ID查询融资保理详情"""
    url = f'{api_host}/api-scf/financialFactoring/queryById'
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


def api_financialFactoring_queryConfigSet(token, payload):
    """根据项目id查询融资流程配置"""
    url = f'{api_host}/api-scf/financialFactoring/queryConfigSet'
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


def api_financialFactoring_queryFinancialFactoringPage(token, payload):
    """查询融资保理审核列表"""
    url = f'{api_host}/api-scf/financialFactoring/queryFinancialFactoringPage'
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


def api_financialFactoring_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/financialFactoring/resubmit'
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


def api_financialFactoring_updateAuditStatus(token, payload):
    """融资保理审核"""
    url = f'{api_host}/api-scf/financialFactoring/updateAuditStatus'
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


class FinancialFactoring(unittest.TestCase):
    def test_001_financialFactoring_insert(self):
        """【供应商】新增"""
        payload = {
            "bankAccountNo": 5520418039408053,
            "creditEnhancerEntId": 1544611013257465857,
            "creditEnhancerEntName": get_company(),
            "estimatedDisbursementDate": "增信方名称",
            "financeEntId": 1544611013257465857,
            "financeEntName": "增信方名称",
            "financingAmount": 1000,
            "financingRate": "1%",
            "financingRemainAmount": 0,
            "financingServiceCharge": 0,
            "financingTerm": 100,
            "goldenLetterId": 1562714421046603778,
            "platformServiceCharge": 1562682259547254785,
            "platformServiceRate": "1%"
        }
        r = api_financialFactoring_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_financialFactoring_queryById(self):
        """根据ID查询融资保理详情"""
        payload = {
            "id": 0
        }
        r = api_financialFactoring_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_financialFactoring_queryConfigSet(self):
        """根据项目id查询融资流程配置"""
        id_one = api_scfProjectBasis_listProjectBasis(token_scf_platform).json()["datas"][0]["id"]
        payload = {
            "id": id_one
        }
        r = api_financialFactoring_queryConfigSet(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_financialFactoring_queryFinancialFactoringPage(self):
        """查询融资保理审核列表"""
        payload = {
            "auditStatus": 0,
            "creditEnhancerEntName": "",
            "financeEntName": "",
            "goldenLetterCode": "",
            "num": 0,
            "size": 0
        }
        r = api_financialFactoring_queryFinancialFactoringPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_financialFactoring_resubmit(self):
        """重新提交"""
        payload = {
            "auditFlowItemId": 0,
            "bankAccountNo": 0,
            "creditEnhancerEntId": 0,
            "creditEnhancerEntName": "",
            "estimatedDisbursementDate": "",
            "financeEntId": 0,
            "financeEntName": "",
            "financingAmount": 0,
            "financingRate": "",
            "financingRemainAmount": 0,
            "financingServiceCharge": 0,
            "financingTerm": 0,
            "goldenLetterId": 0,
            "id": 0,
            "platformServiceCharge": 0,
            "platformServiceRate": ""
        }
        r = api_financialFactoring_resubmit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_financialFactoring_updateAuditStatus(self):
        """融资保理审核"""
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
        r = api_financialFactoring_updateAuditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

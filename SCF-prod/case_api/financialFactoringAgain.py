from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_number
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis
import requests
import unittest
import json

"""再融资保理控制层"""


def api_financialFactoringAgain_insert(token, payload):
    """新增"""
    url = f'{api_host}/api-scf/financialFactoringAgain/insert'
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


def api_financialFactoringAgain_queryById(token, payload):
    """根据ID查询融资保理详情"""
    url = f'{api_host}/api-scf/financialFactoringAgain/queryById'
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


def api_financialFactoringAgain_queryConfigSet(token, payload):
    """根据项目id查询融资流程配置"""
    url = f'{api_host}/api-scf/financialFactoringAgain/queryConfigSet'
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


def api_financialFactoringAgain_queryFinancialFactoringPage(token, payload):
    """查询融资保理审核列表"""
    url = f'{api_host}/api-scf/financialFactoringAgain/queryFinancialFactoringPage'
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


def api_financialFactoringAgain_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/financialFactoringAgain/resubmit'
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


def api_financialFactoringAgain_updateAuditStatus(token, payload):
    """融资保理审核"""
    url = f'{api_host}/api-scf/financialFactoringAgain/updateAuditStatus'
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


def api_financialFactoringAgain_queryByApplicationNumber(token, payload):
    """根据再保理申请编号查询再保理详情"""
    url = f'{api_host}/api-scf/financialFactoringAgain/queryByApplicationNumber'
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


class FinancialFactoringAgain(unittest.TestCase):
    def test_001_financialFactoringAgain_insert(self):
        """新增再"""
        payload = {
            "bankAccountNo": "41234123",
            "estimatedDisbursementDate": "2022-09-29T07:39:50.154Z",
            "financeEntId": "1547048461623263234",
            "financeEntName": "泛光灯",
            "financingAmount": 1000,
            "financingRate": 0.1,
            "financingRemainAmount": 0,
            "financingServiceCharge": "1.09",
            "financingTerm": 397,
            "goldenLetterCode": "JDX20220929063",
            "platformServiceCharge": "1.00",
            "platformServiceRate": 0.1,
            "projectId": "1575389575205949442",
            "currentHolder": "接口自动化保理商账号",
            "founderEnt": "接口自动化核心企业账号",
            "goldenLetterEndDate": "2023-10-31T07:41:48.897",
            "goldenLetterMoney": 1000,
            "goldenLetterOpenDate": "2022-09-28T07:41:59.41",
            "initialHolder": "自动化供应商企业名称",
            "promisedPaymentDate": "2023-09-30T07:41:53.796"
        }
        r = api_financialFactoringAgain_insert(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_financialFactoringAgain_queryById(self):
        """根据ID查询融资保理详情"""
        payload = {
            "id": 0
        }
        r = api_financialFactoringAgain_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_financialFactoringAgain_queryConfigSet(self):
        """根据项目id查询融资流程配置"""
        # id_one = api_scfProjectBasis_listProjectBasis(token_scf_platform).json()["datas"][0]["id"]
        payload = {
            "id": 1573520796372992002
        }
        r = api_financialFactoringAgain_queryConfigSet(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_financialFactoringAgain_queryFinancialFactoringPage(self):
        """查询融资保理审核列表"""
        payload = {
            "auditStatus": 0,
            "creditEnhancerEntName": "",
            "financeEntName": "",
            "goldenLetterCode": "",
            "num": 0,
            "size": 0
        }
        r = api_financialFactoringAgain_queryFinancialFactoringPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_financialFactoringAgain_resubmit(self):
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
        r = api_financialFactoringAgain_resubmit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_financialFactoringAgain_updateAuditStatus(self):
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
        r = api_financialFactoringAgain_updateAuditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_financialFactoringAgain_queryByApplicationNumber(self):
        """根据再保理申请编号查询再保理详情"""
        payload = {
            "financeApplicationNumber": ""
        }
        r = api_financialFactoringAgain_queryByApplicationNumber(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

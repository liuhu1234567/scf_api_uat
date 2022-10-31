from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_company, get_number
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasis
from modware.bus_orderLoan import Bus_orderLoan
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


def api_financialFactoring_queryByApplicationNumber(token, payload):
    """根据融资申请编号查询融资保理详情"""
    url = f'{api_host}/api-scf/financialFactoring/queryByApplicationNumber'
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


def api_financialFactoring_checkByProjectId(token, payload):
    """根据项目id校验是否完成前面流程"""
    url = f'{api_host}/api-scf/financialFactoring/checkByProjectId'
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


def api_financialFactoring_queryByGoldLetterCode(token, payload):
    """根据金点信编号查询融资详情"""
    url = f'{api_host}/api-scf/financialFactoring/queryByGoldLetterCode'
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


def api_financialFactoring_queryPage(token, payload):
    """查询融资保理列表"""
    url = f'{api_host}/api-scf/financialFactoring/queryPage'
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


def api_financialFactoring_financialSeal(token, payload):
    """融资平台方审核签章返回地址"""
    url = f'{api_host}/api-scf/financialFactoring/financialSeal'
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


class FinancialFactoring(unittest.TestCase):
    def test_001_financialFactoring_insert(self):
        """【供应商】新增保理融资 V2.1.1修改"""
        goldenLetterCoden_nwe = Bus_orderLoan().audit_credentials()
        payload = {
            "bankAccountNo": "345690914408085",
            "estimatedDisbursementDate": "2022-09-28T07:54:46.236Z",
            "financeEntId": "1565532904946343937",
            "financeEntName": "接口自动化保理商账号",
            "financingAmount": 1000,
            "financingRate": 1,
            "financingRemainAmount": 0,
            "financingServiceCharge": "10.90",
            "financingTerm": 398,
            "goldenLetterCode": goldenLetterCoden_nwe,
            "platformServiceCharge": "10.00",
            "platformServiceRate": 1,
            "projectId": "1568063677864439810",
            "currentHolder": "自动化供应商企业名称",
            "founderEnt": "接口自动化核心企业账号",
            "goldenLetterEndDate": "2023-10-31T07:41:48.897",
            "goldenLetterMoney": 1000,
            "goldenLetterOpenDate": "2022-09-28T07:41:59.41",
            "initialHolder": "自动化供应商企业名称",
            "promisedPaymentDate": "2023-09-30T07:41:53.796",
            "bankRate": "1000",
            "bankServiceCharge": 1
        }
        g_d["projectId"] = payload["projectId"]
        g_d["goldenLetterCoden_nwe"] = goldenLetterCoden_nwe
        r = api_financialFactoring_insert(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_financialFactoring_queryById(self):
        """根据ID查询融资保理详情"""
        id_one = api_scfProjectBasis_listProjectBasis(token_scf_platform).json()["datas"][0]["id"]
        payload = {
            "id": id_one
        }
        r = api_financialFactoring_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_financialFactoring_queryFinancialFactoringPage(self):
        """查询融资保理审核列表"""
        payload = {
            "auditStatus": 0,
            "creditEnhancerEntName": "",
            "financeEntName": "",
            "goldenLetterCode": "",
            "num": 1,
            "size": 10
        }
        r = api_financialFactoring_queryFinancialFactoringPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_financialFactoring_resubmit(self):
        """重新提交"""
        payload = {
            "id": "1575307554190274562",
            "bankAccountNo": "345690914408085",
            "creditEnhancerEntId": 0,
            "creditEnhancerEntName": 0,
            "estimatedDisbursementDate": "2022-09-27T23:54:46.000Z",
            "financeEntId": "1565532904946343937",
            "financeEntName": "接口自动化保理商账号",
            "financingAmount": 1000,
            "financingRate": 1,
            "financingRemainAmount": 0,
            "financingServiceCharge": 10.9,
            "financingTerm": 398,
            "goldenLetterCode": "JDX20869520417",
            "platformServiceCharge": 10,
            "platformServiceRate": 1,
            "financingInstructions": "0",
            "currentHolder": "自动化供应商企业名称",
            "founderEnt": "接口自动化核心企业账号",
            "goldenLetterEndDate": "2023-10-31T07:41:48.897",
            "goldenLetterMoney": 1000,
            "goldenLetterOpenDate": "2022-09-28T07:41:59.41",
            "initialHolder": "自动化供应商企业名称",
            "promisedPaymentDate": "2023-09-30T07:41:53.796"
        }
        r = api_financialFactoring_resubmit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_financialFactoring_updateAuditStatus(self):
        """融资保理审核 V2.1.1修改"""
        payload = {
            "coreEntId": "1565528298128351233",
            "auditEntId": "1565532746930135041",
            "auditFlowItemId": "1575306492444160002",
            "auditStatus": 3,
            "entId": "1565532746930135041",
            "id": "1575303286704058370",
            "recipientId": "1565532746930135041",
            "financeEntId": "1565532904946343937",
            "goldenLetterId": "1575306485586472962"
        }
        r = api_financialFactoring_updateAuditStatus(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_financialFactoring_queryByApplicationNumber(self):
        """根据融资申请编号查询融资保理详情 V2.1.1修改"""
        payload = {
            "financeApplicationNumber": "75643585578"
        }
        r = api_financialFactoring_queryByApplicationNumber(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_financialFactoring_checkByProjectId(self):
        """根据项目id校验是否完成前面流程"""
        payload = {
            "id": g_d["projectId"]
        }
        r = api_financialFactoring_checkByProjectId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_009_financialFactoring_queryByGoldLetterCode(self):
        """根据金点信编号查询融资详情"""
        payload = {
            "goldenLetterCode": g_d["goldenLetterCoden_nwe"]
        }
        r = api_financialFactoring_queryByGoldLetterCode(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_010_financialFactoring_queryPage(self):
        """根据金点信编号查询融资详情"""
        payload = {
            "auditStatus": 0,
            "currentHolder": "",
            "founderEnt": "",
            "goldenLetterCode": "",
            "num": 1,
            "paymentStatus": 0,
            "size": 10
        }
        r = api_financialFactoring_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_011_financialFactoring_queryPage(self):
        """融资平台方审核签章返回地址"""
        payload = {
            "auditStatus": 3,
            "id": 1573228672130846722
        }
        r = api_financialFactoring_financialSeal(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

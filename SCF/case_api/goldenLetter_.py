from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number
import requests
import unittest
import json

"""金点信"""
def api_goldenLetter_getCreditAmount(token, payload):
    """获取授信额度"""
    url = f'{api_host}/api-scf/goldenLetter/getCreditAmount'
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


def api_goldenLetter_open_deleteBillTem(token, payload):
    """发票删除"""
    url = f'{api_host}/api-scf/goldenLetter/open/deleteBillTemp'
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


def api_goldenLetter_open_importBillExcel(token, payload):
    """开立-导入发票"""
    url = f'{api_host}/api-scf/goldenLetter/open/importBillExcel'
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


def api_goldenLetter_open_insert(token, payload):
    """开立新增"""
    url = f'{api_host}/api-scf/goldenLetter/open/insert'
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


def api_goldenLetter_open_queryPage(token, payload):
    """查询开立审核列表"""
    url = f'{api_host}/api-scf/goldenLetter/open/queryPage'
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


def api_goldenLetter_open_updateAuditStatus(token, payload):
    """开立审核"""
    url = f'{api_host}/api-scf/goldenLetter/open/updateAuditStatus'
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


def api_goldenLetter_queryBillList(token, payload):
    """开立-查询发票-临时表"""
    url = f'{api_host}/api-scf/goldenLetter/queryBillList'
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


def api_goldenLetter_queryBillListById(token, payload):
    """根据金点信ID查询发票详情"""
    url = f'{api_host}/api-scf/goldenLetter/queryBillListById'
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


def api_goldenLetter_queryByCode(token, payload):
    """根据code查询金点信详情"""
    url = f'{api_host}/api-scf/goldenLetter/queryByCode'
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


def api_goldenLetter_queryById(token, payload):
    """根据ID查询金点信详情"""
    url = f'{api_host}/api-scf/goldenLetter/queryById'
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


def api_goldenLetter_queryConfigSet(token, payload):
    """根据核心企业id查询开立基础项配置"""
    url = f'{api_host}/api-scf/goldenLetter/queryConfigSet'
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


def api_goldenLetter_queryPage(token, payload):
    """查询金点信列表"""
    url = f'{api_host}/api-scf/goldenLetter/queryPage'
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


def api_goldenLetter_querySupplierList(token, payload):
    """供应商信息"""
    url = f'{api_host}/api-scf/goldenLetter/querySupplierList'
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


def api_goldenLetter_resubmit(token, payload):
    """重新提交"""
    url = f'{api_host}/api-scf/goldenLetter/resubmit'
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


def api_goldenLetter_retrospective(token, payload):
    """金点信追溯"""
    url = f'{api_host}/api-scf/goldenLetter/retrospective'
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


class Open(unittest.TestCase):
    def test_001_goldenLetter_getCreditAmount(self):
        """获取授信额度"""
        payload = {
            "creditId": 0,
            "projectId": 0,
            "tenantId": 0
        }
        r = api_goldenLetter_getCreditAmount(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_goldenLetter_open_deleteBillTemp(self):
        """发票删除"""
        payload = {
        }
        r = api_goldenLetter_open_deleteBillTem(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_goldenLetter_open_importBillExcel(self):
        """开立-导入发票"""
        payload = {
            "fileId": ""
        }
        r = api_goldenLetter_open_importBillExcel(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_goldenLetter_open_insert(self):
        """开立-导入发票"""
        payload = {
            "bills": [],
            "coreEntId": 0,
            "coreEntName": "",
            "createBy": 0,
            "createTime": "",
            "creditEnhancerId": 0,
            "creditEnhancerName": "",
            "currentHolder": "",
            "currentHolderId": 0,
            "deleted": 0,
            "founderEnt": "",
            "founderEntId": 0,
            "goldenLetterCode": "",
            "goldenLetterEndDate": "",
            "goldenLetterMoney": 0,
            "goldenLetterOpenDate": "",
            "initialHolder": "",
            "initialHolderId": 0,
            "invoiceAmountProportion": "",
            "invoiceWithTax": 0,
            "openApplicationNumber": "",
            "orderName": "",
            "orderNumber": "",
            "promisedPaymentDate": "",
            "recipient": "",
            "recipientId": 0,
            "remainingAvailableQuota": 0,
            "remainingOpenableInvoice": 0,
            "statementNumber": "",
            "totalIssuerQuota": 0,
            "updateBy": 0,
            "updateTime": "",
            "usedQuota": 0
        }
        r = api_goldenLetter_open_insert(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_open_queryPage(self):
        """查询开立审核列表"""
        payload = {
            "auditStatus": 0,
            "founderEnt": "",
            "goldenLetterCode": "",
            "num": 0,
            "recipient": "",
            "size": 0
        }
        r = api_goldenLetter_open_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_goldenLetter_open_updateAuditStatus(self):
        """开立审核"""
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
        r = api_goldenLetter_open_updateAuditStatus(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_goldenLetter_queryBillList(self):
        """开立-查询发票-临时表"""
        payload = {
            "coreEntName": "欣旺达",
            "date": "2022-07",
            "division": "电池事业部",
            "recipient": "AAA公司"
        }
        r = api_goldenLetter_queryBillList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_goldenLetter_queryBillListById(self):
        """根据金点信ID查询发票详情"""
        payload = {
            "id": 0
        }
        r = api_goldenLetter_queryBillListById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_goldenLetter_queryByCode(self):
        """根据code查询金点信详情"""
        payload = {
            "goldenLetterCode": "",
            "num": 0,
            "size": 0
        }
        r = api_goldenLetter_queryByCode(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_goldenLetter_queryById(self):
        """根据ID查询金点信详情"""
        payload = {
            "id": 0
        }
        r = api_goldenLetter_queryById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_goldenLetter_queryConfigSet(self):
        """根据核心企业id查询开立基础项配置"""
        payload = {
            "id": 0
        }
        r = api_goldenLetter_queryConfigSet(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_goldenLetter_queryPage(self):
        """查询金点信列表"""
        payload = {
            "auditStatus": 0,
            "currentHolder": "",
            "founderEnt": "",
            "goldenLetterCode": "",
            "num": 0,
            "paymentStatus": 0,
            "size": 0
        }
        r = api_goldenLetter_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_013_goldenLetter_querySupplierList(self):
        """供应商信息"""
        payload = {
        }
        r = api_goldenLetter_querySupplierList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_014_goldenLetter_resubmit(self):
        """重新提交"""
        payload = {
            "auditFlowItemId": 0,
            "bills": [],
            "coreEntId": 0,
            "coreEntName": "",
            "creditEnhancerId": 0,
            "creditEnhancerName": "",
            "currentHolder": "",
            "currentHolderId": 0,
            "founderEnt": "",
            "founderEntId": 0,
            "goldenLetterCode": "",
            "goldenLetterEndDate": "",
            "goldenLetterMoney": 0,
            "goldenLetterOpenDate": "",
            "id": 0,
            "initialHolder": "",
            "initialHolderId": 0,
            "invoiceAmountProportion": "",
            "invoiceWithTax": 0,
            "openApplicationNumber": "",
            "orderName": "",
            "orderNumber": "",
            "promisedPaymentDate": "",
            "recipient": "",
            "recipientId": 0,
            "remainingAvailableQuota": 0,
            "remainingOpenableInvoice": 0,
            "statementNumber": "",
            "totalIssuerQuota": 0,
            "usedQuota": 0
        }
        r = api_goldenLetter_resubmit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_015_goldenLetter_retrospective(self):
        """金点信追溯"""
        payload = {
            "goldenLetterId": 0
        }
        r = api_goldenLetter_retrospective(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

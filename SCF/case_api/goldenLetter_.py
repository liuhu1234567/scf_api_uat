from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_enterprise,token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_company
from case_api.template import api_template_uploadfile
import requests
import unittest
import json
import datetime

"""金点信"""


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
        "Authorization": token,
        "x-userid-header": "1562325610995245058"
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


class GoldenLetter(unittest.TestCase):
    def test_001_goldenLetter_open_deleteBillTemp(self):
        """发票删除"""
        payload = {
        }
        r = api_goldenLetter_open_deleteBillTem(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_goldenLetter_open_importBillExcel(self):
        """开立-导入发票"""
        path = api_template_uploadfile(token_scf_platform,'导入发票模板.xlsx').json()["datas"]["url"]
        payload = {
            "fileId": path
        }
        r = api_goldenLetter_open_importBillExcel(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_goldenLetter_open_insert(self):
        """开立新增"""
        payload = {
            "bills": ["1562284267547848706", "1562284267556237314"],
            "coreEntId": 1562325610781274113,
            "coreEntName": "核心企业",
            "creditEnhancerId": 1544611013257465857,
            "creditEnhancerName": "西咸新区沣东新城一",
            "founderEnt": "核心企业",
            "founderEntId": 1549224468155265025,
            "goldenLetterCode": "",
            "goldenLetterEndDate": "2024-07-09T14:00:00",
            "goldenLetterMoney": 1000,
            "goldenLetterOpenDate": "2023-07-09T10:00:00",
            "invoiceAmountProportion": "100%",
            "invoiceWithTax": 1000,
            "openApplicationNumber": "",
            "orderName": "合同/订单名称",
            "orderNumber": "合同/订单编号",
            "promisedPaymentDate": "2023-07-09T10:00:00",
            "recipient": "泰麒麟科技有限公司",
            "recipientId": 1544611079456165889,
            "remainingAvailableQuota": 0,
            "remainingOpenableInvoice": 0,
            "statementNumber": "对账单编号",
            "totalIssuerQuota": 1000,
            "usedQuota": 1000
        }
        r = api_goldenLetter_open_insert(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_open_queryPage(self):
        """查询开立审核列表"""
        payload = {
            "auditStatus": 0,
            "founderEnt": "",
            "goldenLetterCode": "",
            "num": 1,
            "recipient": "",
            "size": 10
        }
        r = api_goldenLetter_open_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_goldenLetter_open_updateAuditStatus(self):
        """开立审核"""
        payload = {
            "auditEntId": 0,
            "auditFlowItemId": 0,
            "auditOpinion": "",
            "auditStatus": 3,
            "busType": "",
            "creditEnhancerId": 0,
            "entId": 0,
            "id": 0,
            "projectId": 0,
            "recipientId": 0
        }
        r = api_goldenLetter_open_updateAuditStatus(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_goldenLetter_queryBillList(self):
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

    def test_007_goldenLetter_queryBillListById(self):
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

    def test_008_goldenLetter_queryByCode(self):
        """根据code查询金点信详情"""
        payload = {
            "goldenLetterCode": "",
            "num": 1,
            "size": 10
        }
        r = api_goldenLetter_queryByCode(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_09_goldenLetter_queryById(self):
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

    def test_010_goldenLetter_queryConfigSet(self):
        """根据核心企业id查询开立基础项配置"""
        payload = {
            "id": 1562325610781274113
        }
        r = api_goldenLetter_queryConfigSet(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_goldenLetter_queryPage(self):
        """查询金点信列表"""
        payload = {
            "auditStatus": 0,
            "currentHolder": "",
            "founderEnt": "核心企业",
            "goldenLetterCode": "",
            "num": 1,
            "paymentStatus": 0,
            "size": 10
        }
        r = api_goldenLetter_queryPage(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_goldenLetter_resubmit(self):
        """重新提交"""
        payload = {
            "auditFlowItemId": 1562325610781274113,
            "bills": ["1562284267547848706", "1562284267556237314"],
            "coreEntId": 1562325610781274113,
            "coreEntName": "核心企业",
            "creditEnhancerId": 0,
            "creditEnhancerName": get_company(),
            "currentHolder": "",
            "currentHolderId": 0,
            "founderEnt": get_company(),
            "founderEntId": 0,
            "goldenLetterCode": "金电信编号",
            "goldenLetterEndDate": "2018-07-09T14:00:00",
            "goldenLetterMoney": 0,
            "goldenLetterOpenDate": "2018-07-09T10:00:00",
            "id": 0,
            "initialHolder": "",
            "initialHolderId": 0,
            "invoiceAmountProportion": "发票开立金额比例",
            "invoiceWithTax": 0,
            "openApplicationNumber": "开立申请编号",
            "orderName": "合同/订单名称",
            "orderNumber": "合同/订单编号",
            "promisedPaymentDate": "2018-07-09T14:00:00",
            "recipient": get_company(),
            "recipientId": 0,
            "remainingAvailableQuota": 0,
            "remainingOpenableInvoice": 0,
            "statementNumber": "对账单编号",
            "totalIssuerQuota": 0,
            "usedQuota": 0
        }
        r = api_goldenLetter_resubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_013_goldenLetter_retrospective(self):
        """金点信追溯"""
        payload = {
            "goldenLetterId": 1562325610781274113
        }
        r = api_goldenLetter_retrospective(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

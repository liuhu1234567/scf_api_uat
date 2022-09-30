from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from case_api.enterprise import api_enterprise_queryEntArchivesDetail
from common.do_faker import get_number
import requests
import unittest
import json
from modware.bus_orderLoan import Bus_orderLoan
from case_api.goldenLetter_ import api_goldenLetter_open_queryPage

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
    """转让列表"""
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


def api_scfTransfer_getLetterCode(token, payload):
    """获取金点信编号"""
    url = f'{api_host}/api-scf/scfTransfer/getLetterCode'
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


def api_scfTransfer_listPaymentStatusEnum(token, payload):
    """获取兑付状态"""
    url = f'{api_host}/api-scf/scfTransfer/listPaymentStatusEnum'
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


def api_scfTransfer_listScfAuditStatusEnum(token, payload):
    """获取审批状态"""
    url = f'{api_host}/api-scf/scfTransfer/listScfAuditStatusEnum'
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


def api_scfTransfer_pullByCoreId(token, payload):
    """根据核心ID-授信配置-表单"""
    url = f'{api_host}/api-scf/scfTransfer/pullByCoreId'
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


def api_scfTransfer_queryConfigSet(token, payload):
    """根据核心企业id查询转让基础项配置"""
    url = f'{api_host}/api-scf/scfTransfer/queryConfigSet'
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


def api_scfTransfer_signProtocol(token, payload):
    """转让协议签署"""
    url = f'{api_host}/api-scf/scfTransfer/signProtocol'
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


def api_scfTransfer_transferSeal(token, payload):
    """转让平台方审核签章返回地址"""
    url = f'{api_host}/api-scf/scfTransfer/transferSeal'
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

    def test_001_scfTransfer_transfer(self):
        """【供应商】发起转让保存转让信息"""
        g_d["goldenLetterCoden_nwe"] = Bus_orderLoan().audit_credentials()
        payload = {
            "auditStatus": 1,
            "founderEnt": "",
            "goldenLetterCode": g_d["goldenLetterCoden_nwe"],
            "num": 1,
            "recipient": "",
            "size": 10
        }
        r = api_goldenLetter_open_queryPage(token_scf_enterprise, payload)
        r_json = r.json()
        g_d["coreSub"] = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()["datas"]["id"]
        payload = {
            "bills": [
                "1575323707260284929"
            ],
            "coreSub": "",
            "creditEnhancerId": "",
            "id": r_json["datas"][0]["id"],
            "invoiceWithTax": 0,
            "orderName": 0,
            "orderNumber": 0,
            "receiver": "1565532746930135041",
            "statementNumber": "91440300279446850J",
            "transferAmount": "1000",
            "founderEnt": "接口自动化核心企业账号"
        }
        r = api_scfTransfer_transfer(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
        g_d["id_new"] = r_json["datas"]

    def test_002_scfTransfer_toAudit(self):
        """跳转至审核页面"""
        payload = {
            "id": g_d["id_new"]
        }
        r = api_scfTransfer_toAudit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        # self.assertEqual(200, r_json['resp_code'])
        # self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_scfTransfer_audit(self):
        """审核"""
        payload = {"auditOpinion": "0",
                   "auditStatus": 5,
                   "id": g_d["id_new"]}
        r = api_scfTransfer_audit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_scfTransfer_detail(self):
        """转让详情"""
        searchSupplier_payload = {
            "founderEnt": "",
            "goldenLetterCode": "",
            "currentHolder": "",
            "paymentStatus": "",
            "num": 1,
            "size": 10
        }
        id = api_scfTransfer_searchSupplier(token_scf_platform, searchSupplier_payload).json()['datas'][0]['id']
        payload = {
            "id": id
        }
        r = api_scfTransfer_detail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
        g_d["goldenLetterCode"] = r_json["datas"][0]["goldenLetterCode"]

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
        g_d["id_resubmit"] = r_json["datas"][0]["id"]

    def test_008_scfTransfer_reSubmit(self):
        """转让重新提交"""
        payload = {
            "bills": [
                "1575684533347487746"
            ],
            "coreSub": "",
            "founderEnt": "接口自动化核心企业账号",
            "creditEnhancerId": "",
            "id": "1575684533322321922",
            "invoiceWithTax": 0,
            "orderName": "0",
            "orderNumber": "0",
            "receiver": "1565532746930135041",
            "statementNumber": "91440300279446850J",
            "transferAmount": 1000,
            "transferIntroduce": ""
        }

        r = api_scfTransfer_reSubmit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

        payload = {"auditOpinion": "0",
                   "auditStatus": 3,
                   "id": g_d["id_resubmit"]}
        r = api_scfTransfer_audit(token_scf_supplier, payload)
        r_json = r.json()

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_010_scfTransfer_selectReceiver(self):
        """查询接收人"""
        payload = {
        }
        r = api_scfTransfer_selectReceiver(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_011_scfTransfer_toResumit(self):
        """跳转至重新提交页面"""
        payload = {
            "id": g_d["id_new"]
        }
        r = api_scfTransfer_toResumit(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_012_scfTransfer_toSign(self):
        """跳转至签收页面"""
        payload = {
            "id": g_d["id_new"]
        }
        r = api_scfTransfer_toSign(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

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
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_014_scfTransfer_listCoreSub(self):
        """获取核企子公司"""
        payload = {
        }
        r = api_scfTransfer_listCoreSub(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_015_scfTransfer_getLetterCode(self):
        """获取金点信编号"""
        payload = {
        }
        r = api_scfTransfer_getLetterCode(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_016_scfTransfer_listPaymentStatusEnum(self):
        """获取兑付状态"""
        payload = {
        }
        r = api_scfTransfer_listPaymentStatusEnum(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_017_scfTransfer_listScfAuditStatusEnum(self):
        """获取审批状态"""
        payload = {
        }
        r = api_scfTransfer_listScfAuditStatusEnum(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_018_scfTransfer_pullByCoreId(self):
        """根据核心ID-授信配置-表单"""
        payload = {
            "id": g_d["coreSub"]
        }
        r = api_scfTransfer_pullByCoreId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_019_scfTransfer_queryConfigSet(self):
        """根据核心企业id查询转让基础项配置"""
        payload = {
            "id": g_d["coreSub"]
        }
        r = api_scfTransfer_queryConfigSet(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
    """还未开发完成"""
    # def test_020_scfTransfer_signProtocol(self):
    #     """转让协议签署"""
    #     payload = {
    #         "id": 1566672651710578689
    #     }
    #     r = api_scfTransfer_signProtocol(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_021_scfTransfer_transferSeal(self):
        """转让平台方审核签章返回地址"""
        payload = {
            "auditStatus": 3,
            "id": g_d["id_new"]
        }
        r = api_scfTransfer_transferSeal(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

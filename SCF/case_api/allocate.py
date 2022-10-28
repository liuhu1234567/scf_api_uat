from common.global_variable import customize_dict
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.do_config import api_host, restime
import requests
import json
import unittest
from case_api.enterprise import api_enterprise_queryEntArchivesDetail


def api_allocate_insert(token, payload):
    """新增额度"""
    url = f'{api_host}/api-scf/allocate/insert'
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


def api_allocate_update(token, payload):
    """修改额度"""
    url = f'{api_host}/api-scf/allocate/update'
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


def api_allocate_commit(token, payload):
    """审批状态：1.已提交，2.重新提交，3.驳回, 4.通过，5.变更中, 6.变更驳回, 7.已变更"""
    url = f'{api_host}/api-scf/allocate/commit'
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


def api_allocate_queryPage(token, payload):
    """分页查询额度"""
    url = f'{api_host}/api-scf/allocate/queryPage'
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


def api_allocate_queryAuditPage(token, payload):
    """分页查询额度-审查"""
    url = f'{api_host}/api-scf/allocate/queryAuditPage'
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


def api_allocate_get(token, payload):
    """获取额度"""
    url = f'{api_host}/api-scf/allocate/get'
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


# def api_allocate_delete(token, payload):
#     """删除额度"""
#     url = f'{api_host}/api-scf/allocate/delete'
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


def api_allocate_queryList(token, payload):
    """分页查询额度-List"""
    url = f'{api_host}/api-scf/allocate/queryList'
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


def api_allocate_checkAddProject(token, payload):
    """检查可新增单一项目还是不限项目"""
    url = f'{api_host}/api-scf/allocate/checkAddProject'
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


def api_allocate_getTotalAmount(token, payload):
    """获额度分配的总额-核心企业或子公司"""
    url = f'{api_host}/api-scf/allocate/getTotalAmount'
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


def api_allocate_queryPageAllocate(token, payload):
    """分页查询额度-List-已经分配"""
    url = f'{api_host}/api-scf/allocate/queryPageAllocate'
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


def api_allocate_useAllocateAmount(token, payload):
    """使用额度管理额度"""
    url = f'{api_host}/api-scf/allocate/useAllocateAmount'
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


class Allocate(unittest.TestCase):
    def test_001_allocate_insert(self):
        """【核心企业】新增额度"""
        corDatas = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']
        coreCertificateCardId = corDatas['creditCode']
        g_d['coreEntId'] = corDatas['id']
        g_d['coreEntName'] = corDatas['entName']
        payload = {
            "auditAmount": 100,
            "coinType": 1,
            "coreCertificateCardId": coreCertificateCardId,
            "coreCertificateType": 1,
            "coreCreditScope": 1,
            "coreId": g_d.get('coreEntId'),
            "coreName": g_d.get('coreEntName'),
            "creditId": 1,
            "creditName": "授信方名称",
            "creditType": 1,
            "financialInstitutionName": "金融机构名称",
            "financialProductId": 1,
            "financialProductName": "金融产品名称",
            "loanBegin": "2022-08-09 00:11:11",
            "loanEnd": "2022-08-10 00:11:11",
            "loanRatio": 1.98,
            "projectId": 1,
            "projectName": "项目名称",
            "remainAmount": 1,
            "userAmount": 10
        }
        r = api_allocate_insert(token_scf_enterprise, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_allocate_update(self):
        """【核心企业】修改额度"""
        payload = {
            "auditAmount": 100,
            "coinType": 1,
            "coreCertificateCardId": "S3834953480283",
            "coreCertificateType": 1,
            "coreCreditScope": 1,
            "coreId": g_d.get('coreEntId'),
            "coreName": "核心企业名称",
            "creditId": 1,
            "creditName": "授信方名称",
            "creditType": 1,
            "financialInstitutionName": "金融机构名称",
            "financialProductId": 1,
            "financialProductName": "金融产品名称",
            "id": g_d.get('id'),
            "loanBegin": "2022-08-09 00:11:11",
            "loanEnd": "2022-08-10 00:11:11",
            "loanRatio": 0.98,
            "projectId": 1,
            "projectName": "项目名称",
            "remainAmount": 1,
            "userAmount": 10
        }
        r = api_allocate_update(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_allocate_commit(self):
        """【核心企业】审批状态：1.已提交，2.重新提交，3.驳回, 4.通过，5.变更中, 6.变更驳回, 7.已变更"""
        payload = {
            "auditOpinion": "",
            "auditStatus": 1,
            "id": g_d.get('id')
        }
        r = api_allocate_commit(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_allocate_queryPage(self):
        """【核心企业】分页查询额度"""
        payload = {
            "coreName": "核心企业名称",
            "createBy": 0,
            "createTime": "",
            "creditName": "授信方名称",
            "creditStatus": 1,
            "id": 0,
            "num": 0,
            "projectName": "项目名称",
            "size": 0,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_allocate_queryPage(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_allocate_queryAuditPage(self):
        """【核心企业】分页查询额度-审查"""
        payload = {
            "coreName": "核心企业名称",
            "createBy": 0,
            "createTime": "",
            "creditName": "授信方名称",
            "creditStatus": 1,
            "id": 0,
            "num": 0,
            "projectName": "项目名称",
            "size": 0,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_allocate_queryAuditPage(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_allocate_get(self):
        """【核心企业】获取额度"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_allocate_get(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_007_allocate_delete(self):
    #     """【核心企业】删除额度"""
    #     payload = {
    #         "id": g_d.get('id')
    #     }
    #     r = api_allocate_delete(token_scf_enterprise, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_allocate_queryAuditPage(self):
        """【核心企业】分页查询额度-List"""
        payload = {
            "coreId": "",
            "coreName": "",
            "creditId": 1,
            "creditName": "授信方名称",
            "creditStatus": 1,
            "projectId": 1,
            "projectName": "项目名称",
            "tenantId": 0
        }
        r = api_allocate_queryList(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_009_allocate_checkAddProject(self):
        """【核心企业】检查可新增单一项目还是不限项目"""
        payload = {
            "coreId": 0,
            "creditId": 0,
            "projectType": 0
        }
        r = api_allocate_checkAddProject(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_010_allocate_getTotalAmount(self):
        """【核心企业】获额度分配的总额-核心企业或子公司"""
        payload = {
            "id": g_d.get('coreEntId')
        }
        r = api_allocate_getTotalAmount(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_011_allocate_getTotalAmount(self):
        """【核心企业】分页查询额度-List-已经分配"""
        payload = {
            "entName": "",
            "creditName": "",
            "projectName": "",
            "auditStatus": -1,
            "num": 1,
            "size": 10
        }
        r = api_allocate_queryPageAllocate(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_012_allocate_useAllocateAmount(self):
        """【核心企业】分页查询额度-List-已经分配"""
        payload = {
            "coreEntName": "",
            "creditName": "",
            "projectId": 0,
            "userAmount": 0,
            "userAmountStastus": 0
        }
        r = api_allocate_useAllocateAmount(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_enterprise, token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number
import json
import requests
import unittest
from enterprise import api_enterprise_queryEntArchivesDetail


def api_scfProjectBasis_listProjectBasis(token):
    """【平台方】查询项目列表"""
    url = f'{api_host}/api-scf/scfProjectBasis/listProjectBasis'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfProjectBasis_getBusinessTypes(token):
    """【平台方】获取业务类型"""
    url = f'{api_host}/api-scf/scfProjectBasis/getBusinessTypes'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "2",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfProjectBasis_listProjectBasisByType(token, payload):
    """【平台方】通过业务类型查询项目列表"""
    url = f'{api_host}/api-scf/scfProjectBasis/listProjectBasisByType'
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


def api_scfProjectBasis_listCore(token, payload):
    """【平台方】查询核心企业"""
    url = f'{api_host}/api-scf/scfProjectBasis/listCore'
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


def api_scfProjectBasis_listFinanceProduct(token, payload):
    """【平台方】查询金融产品列表"""
    url = f'{api_host}/api-scf/scfProjectBasis/listFinanceProduct'
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


def api_scfProjectBasis_getUseScope(token):
    """【平台方】查询授信使用范围枚举值"""
    url = f'{api_host}/api-scf/scfProjectBasis/getUseScope'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfProjectBasis_getPushMaterial(token):
    """【平台方】查询推送的节点材料枚举值"""
    url = f'{api_host}/api-scf/scfProjectBasis/getPushMaterial'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfProjectBasis_signType(token):
    """【平台方】获取签署方式"""
    url = f'{api_host}/api-scf/scfProjectBasis/signType'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_scfProjectBasis_insertAllDetail(token, payload):
    """【平台方】新增项目"""
    url = f'{api_host}/api-scf/scfProjectBasis/insertAllDetail'
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


def api_scfProjectBasis_listEnterprise(token, payload):
    """【平台方】查询融资企业"""
    url = f'{api_host}/api-scf/scfProjectBasis/listEnterprise'
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


def api_scfProjectBasis_search(token, payload):
    """【平台方】项目配置搜索"""
    url = f'{api_host}/api-scf/scfProjectBasis/search'
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


def api_scfProjectBasis_enable(token, payload):
    """【平台方】项目配置启用-停用"""
    url = f'{api_host}/api-scf/scfProjectBasis/enable'
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


def api_scfProjectBasis_deliver(token, payload):
    """【平台方】产品配置-再保理配置"""
    url = f'{api_host}/api-scf/scfProjectBasis/deliver'
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


def api_scfProjectBasis_filterList(token, payload):
    """【平台方】过滤数据表的项目列表"""
    url = f'{api_host}/api-scf/scfProjectBasis/filterList'
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


def api_scfProjectBasis_selectFlow(token, payload):
    """【平台方】查询流程模板"""
    url = f'{api_host}/api-scf/scfProjectBasis/selectFlow'
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


def api_scfProjectBasis_getFlowTemplateDetail(token, payload):
    """【平台方】查询流程模板详情"""
    url = f'{api_host}/api-scf/scfProjectBasis/getFlowTemplateDetail'
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


def api_scfProjectBasis_queryProjectBasicInfo(token, payload):
    """【平台方】通过项目ID查询相关信息"""
    url = f'{api_host}/api-scf/scfProjectBasis/queryProjectBasicInfo'
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


def api_scfProjectBasis_editAllDetail(token, payload):
    """【平台方】跳转至编辑项目页面"""
    url = f'{api_host}/api-scf/scfProjectBasis/editAllDetail'
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


def api_scfProjectBasis_delete(token, payload):
    """【平台方】项目配置删除"""
    url = f'{api_host}/api-scf/scfProjectBasis/delete'
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


class ScfProjectBasis(unittest.TestCase):
    def test_001_scfProjectBasis_listProjectBasis(self):
        """【平台方】查询项目列表"""
        r = api_scfProjectBasis_listProjectBasis(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfProjectBasis_getBusinessTypes(self):
        """【平台方】获取业务类型"""
        r = api_scfProjectBasis_getBusinessTypes(token_scf_platform)
        r_json = r.json()
        g_d['businessType'] = r_json['datas'][0]['value']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfProjectBasis_listProjectBasisByType(self):
        """【平台方】通过业务类型查询项目列表"""
        payload = {
            "businessType": g_d.get('businessType')
        }
        r = api_scfProjectBasis_listProjectBasisByType(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfProjectBasis_listCore(self):
        """【平台方】查询核心企业"""
        payload = {
            "coreName": ""
        }
        r = api_scfProjectBasis_listCore(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfProjectBasis_listFinanceProduct(self):
        """【平台方】查询金融产品列表"""
        payload = {
            "name": ""
        }
        r = api_scfProjectBasis_listFinanceProduct(token_scf_platform, payload)
        r_json = r.json()
        g_d['scfFinanceProductId'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfProjectBasis_getUseScope(self):
        """【平台方】查询授信使用范围枚举值"""
        r = api_scfProjectBasis_getUseScope(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_scfProjectBasis_getPushMaterial(self):
        """【平台方】查询推送的节点材料枚举值"""
        r = api_scfProjectBasis_getPushMaterial(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_scfProjectBasis_signType(self):
        """【平台方】获取签署方式"""
        r = api_scfProjectBasis_signType(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_009_scfProjectBasis_insertAllDetail(self):
        """【平台方】新增项目"""
        g_d['coreEnterpriseId'] = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['id']
        g_d['bankId'] = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['id']
        payload = {
            "scfProjectBasisReq": {
                "id": "",
                "bankId": g_d.get('bankId'),
                "businessType": "3",
                "enterpriseId": g_d.get('coreEnterpriseId'),
                "name": f"项目名称{get_number(6)}",
                "open": False,
                "refactor": False,
                "scfFinanceProductId": g_d.get('scfFinanceProductId'),
                "enter": True,
                "grants": True,
                "transfer": False,
                "finance": True,
                "isCoreGrant": True,
                "bankName": "",
                "flowName": [
                    "2",
                    "3",
                    "6"
                ],
                "financeName": "",
                "enable": True
            },
            "scfProjectEnterReq": {
                "isTemplate": False,
                "flowId": "",
                "filePath": "",
                "grantFlowItemId": "",
                "link": "",
                "scfProjectFlowEnterReq": {
                    "name": f"准入流程名称{get_number(6)}",
                    "step": 2,
                    "flowItems": [
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "3",
                            "customerTypeName": "供应商",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 1,
                            "subs": []
                        },
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "11",
                            "customerTypeName": "平台方",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 2,
                            "subs": []
                        }
                    ]
                }
            },
            "scfProjectGrantReq": {
                "isTemplate": False,
                "flowId": "",
                "isPush": False,
                "useScope": 1,
                "scfProjectFlowReq": {
                    "name": f"授信流程名称{get_number(6)}",
                    "step": 2,
                    "flowItems": [
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "3",
                            "customerTypeName": "供应商",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 1,
                            "subs": []
                        },
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "11",
                            "customerTypeName": "平台方",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 2,
                            "subs": []
                        }
                    ]
                }
            },
            "scfProjectFinanceReq": {
                "isTemplate": False,
                "flowId": "",
                "isHistory": False,
                "isPush": False,
                "pushMaterial": 0,
                "serviceRate": "1.01",
                "financeRate": "2.02",
                "scfProjectFlowReq": {
                    "name": f"融资流程名称{get_number(6)}",
                    "step": 2,
                    "flowItems": [
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "3",
                            "customerTypeName": "供应商",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 1,
                            "subs": []
                        },
                        {
                            "id": "",
                            "flowId": "",
                            "customerType": "11",
                            "customerTypeName": "平台方",
                            "isExternal": False,
                            "isProtocol": False,
                            "isPush": False,
                            "reportId": "",
                            "num": 2,
                            "subs": []
                        }
                    ]
                }
            }
        }
        r = api_scfProjectBasis_insertAllDetail(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_scfProjectBasis_listEnterprise(self):
        """【平台方】查询融资企业"""
        payload = {
            "enable": True,
            "id": 0,
            "name": ""
        }
        r = api_scfProjectBasis_listEnterprise(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_011_scfProjectBasis_search(self):
        """【平台方】产品配置列表-搜索"""
        payload = {
            "enable": True,
            "enterpriseName": "",
            "name": "",
            "num": 1,
            "size": 10
        }
        r = api_scfProjectBasis_search(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_012_scfProjectBasis_enable(self):
        """【平台方】项目配置启用-停用"""
        payload = {
            "enable": 1,
            "id": g_d.get('id')
        }
        r = api_scfProjectBasis_enable(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_013_scfProjectBasis_deliver(self):
        """【平台方】项目配置分配"""
        enterpriseId = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['id']
        payload = {
            "basisId": g_d.get('id'),
            "enterpriseId": enterpriseId
        }
        r = api_scfProjectBasis_deliver(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_014_scfProjectBasis_filterList(self):
        """【平台方】过滤数据表的项目列表"""
        payload = {
            "kind": 0
        }
        r = api_scfProjectBasis_filterList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_015_scfProjectBasis_selectFlow(self):
        """【平台方】查询流程模板"""
        payload = {
            "projectEnum": 2
        }
        r = api_scfProjectBasis_selectFlow(token_scf_platform, payload)
        r_json = r.json()
        g_d['flowid'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_016_scfProjectBasis_getFlowTemplateDetail(self):
        """【平台方】查询流程模板详情"""
        payload = {
            "id": g_d.get('flowid')
        }
        r = api_scfProjectBasis_getFlowTemplateDetail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_017_scfProjectBasis_queryProjectBasicInfo(self):
        """【平台方】通过项目ID查询相关信息"""
        payload = {
            "projectId": g_d.get('id')
        }
        r = api_scfProjectBasis_queryProjectBasicInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_018_scfProjectBasis_editAllDetail(self):
        """【平台方】跳转至编辑项目页面"""
        payload = {
            "id": g_d.get('id')
        }
        r = api_scfProjectBasis_editAllDetail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_019_scfProjectBasis_delete(self):
        """【平台方】项目配置删除"""
        payload = {
            "scfProjectBasisReq": {
                "bankId": g_d.get('bankId'),
                "businessType": g_d.get('businessType'),
                "enter": False,
                "enterpriseId": g_d.get('coreEnterpriseId'),
                "finance": False,
                "grants": False,
                "isCoreGrant": False,
                "name": f"项目名称{get_number(6)}",
                "refactor": False,
                "scfFinanceProductId": g_d.get('scfFinanceProductId')
            }
        }
        id = api_scfProjectBasis_insertAllDetail(token_scf_platform, payload).json()['datas']
        payload = {
            "id": id
        }
        r = api_scfProjectBasis_delete(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

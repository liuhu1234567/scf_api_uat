from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
import json
from common.do_faker import get_number
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_search

"""数据配置管理"""


def api_config_dataTable_allSelect(token):
    """数据表页面下拉列表集合"""
    url = f'{api_host}/api-scf-data/config/dataTable/allSelect'
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


def api_config_dataTable_list_all(token, payload):
    """放款-不分页获取全部数据"""
    url = f'{api_host}/api-scf-data/config/dataTable/list/all'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_config_dataTable_templateData_save(token, payload):
    """模板对应的数据表-新增"""
    url = f'{api_host}/api-scf-data/config/dataTable/templateData/save'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_config_dataTable_templateData_update(token, payload):
    """模板对应的数据表-修改"""
    url = f'{api_host}/api-scf-data/config/dataTable/templateData/update'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_config_dataTable_queryProjectInfo(token, payload):
    """所属项目查询核心企业"""
    url = f'{api_host}/api-scf-data/config/dataTable/queryProjectInfo'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_config_dataTable_customerList(token):
    """可查看的客户类型"""
    url = f'{api_host}/api-scf-data/config/dataTable/customerList'
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


# def api_config_dataTable_getList(token):
#     """数据表列表"""
#     url = f'{api_host}/api-scf-data/config/dataTable/getList'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers)
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'接口响应为：{r.text}')
#     return r


def api_config_dataTable_detail(token, payload):
    """数据表详情"""
    url = f'{api_host}/api-scf-data/config/dataTable/detail'
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


def api_config_dataTable_fieldTable(token, payload):
    """根据模板ID查询模板"""
    url = f'{api_host}/api-scf-data/config/dataTable/fieldTable'
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


def api_config_dataTable_list(token, payload):
    """查询数据表列表"""
    url = f'{api_host}/api-scf-data/config/dataTable/list'
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


def api_config_dataTable_save(token, payload):
    """新增数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/save'
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


def api_config_dataTable_templateList_all(token):
    """数据表模板下拉列表"""
    url = f'{api_host}/api-scf-data/config/dataTable/templateList/all'
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


def api_config_dataTable_update(token, payload):
    """修改数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/update'
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


# def api_config_dataTable_filterItemId(token, payload):
#     """服务接口 - 获取过滤模板类型的项目ID集合"""
#     url = f'{api_host}/api-scf-data/config/dataTable/filterItemId'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r


def api_config_dataTable_findDataTable(token, payload):
    """服务接口 - 获取单个数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/findDataTable'
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


def api_config_dataTable_getOne(token, payload):
    """服务接口 - 获取单个数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/getOne'
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


# def api_config_dataTable_lending_getTotalAmt(token, payload):
#     """服务接口-放款获取合作商放款金额"""
#     url = f'{api_host}/api-scf-data/config/dataTable/lending/getTotalAmt'
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "x-appid-header": "1",
#         "Authorization": token
#     }
#     r = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(f'请求地址：{url}')
#     print(f'请求头：{headers}')
#     print(f'请求参数：{payload}')
#     print(f'接口响应为：{r.text}')
#     return r


def api_config_dataTable_onlyViewDateTable(token, payload):
    """服务-获取数据表数据 - 仅仅针对只查看的数据表"""
    url = f'{api_host}/api-scf-data/config/dataTable/onlyViewDateTable'
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


def api_config_dataTable_templateData_download(token, payload):
    """服务接口 - 放款数据下载"""
    url = f'{api_host}/api-scf-data/config/dataTable/templateData/download'
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


class ConfigDataTable(unittest.TestCase):
    def test_001_config_dataTable_customerList(self):
        """可查看的客户类型"""
        r = api_config_dataTable_customerList(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_config_dataTable_detail(self):
        """数据表详情"""
        payload = {
            "id": 1566717067710705666
        }
        r = api_config_dataTable_detail(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_config_dataTable_fieldTable(self):
        """根据模板ID查询模板"""
        payload = {
            "templateId": 1
        }
        r = api_config_dataTable_fieldTable(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_config_dataTable_list(self):
        """查询数据表列表"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "institutionName": "",
            "num": 0,
            "productName": "",
            "size": 0,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_config_dataTable_list(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_config_dataTable_templateList_all(self):
        """数据表模板下拉列表"""
        r = api_config_dataTable_templateList_all(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_config_dataTable_save(self):
        """新增数据表"""
        payload = {
            "fieldList": [
                {
                    "id": 1,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 1
                },
                {
                    "id": 2,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 2
                },
                {
                    "id": 3,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 3
                },
                {
                    "id": 4,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 4
                },
                {
                    "id": 5,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 5
                },
                {
                    "id": 6,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 6
                },
                {
                    "id": 7,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 7
                },
                {
                    "id": 8,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 8
                },
                {
                    "id": 9,
                    "isEdit": 1,
                    "isSearch": 1,
                    "isShow": 1,
                    "sort": 9
                }
            ],
            "itemId": 0,
            "name": f"数据表{get_number(6)}",
            "templateId": 1,
            "tenantId": 0,
            "tenantType": "3,4,5",
            "type": 1
        }
        r = api_config_dataTable_save(token_scf_platform, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_config_dataTable_update(self):
        """修改数据表"""
        payload = {"id": "1566717067710705666", "name": "自动化专用勿动" + get_number(4), "type": 2, "tenantType": "1",
                   "templateId": "1",
                   "itemId": "1566714084775821314", "productName": "名称54", "institutionName": "创汇传媒有限公司",
                   "tenantName": "接口自动化核心企业账号", "tenantId": "1565528298128351233", "fieldList": [
                {"id": "1", "fieldName": "ind_entp_ctf_num", "desc": "统一社会信用代码", "sort": 0, "isShow": 0, "isSearch": 0,
                 "isEdit": 0, "haveSearch": 1},
                {"id": "2", "fieldName": "ind_entp_nm", "desc": "借款企业名称", "sort": 1, "isShow": 0, "isSearch": 0,
                 "isEdit": 0, "haveSearch": 1},
                {"id": "3", "fieldName": "coop_months", "desc": "合作时长（月）", "sort": 2, "isShow": 0, "isSearch": 0,
                 "isEdit": 0, "haveSearch": 1},
                {"id": "4", "fieldName": "last_order_total_num", "desc": "近12个月订单总笔数", "sort": 3, "isShow": 0,
                 "isSearch": 0, "isEdit": 0, "haveSearch": 1},
                {"id": "5", "fieldName": "last_order_total_amt", "desc": "近12个月订单总金额（元）", "sort": 4, "isShow": 0,
                 "isSearch": 0, "isEdit": 0, "haveSearch": 0},
                {"id": "6", "fieldName": "last_order_max_amt", "desc": "近12个月最大订购金额（元）", "sort": 5, "isShow": 0,
                 "isSearch": 0, "isEdit": 0, "haveSearch": 0},
                {"id": "7", "fieldName": "vendor_compl_rate", "desc": "供应商履约完成率[*%]", "sort": 6, "isShow": 0,
                 "isSearch": 0, "isEdit": 0, "haveSearch": 1},
                {"id": "8", "fieldName": "vendor_delivery_freq", "desc": "供应商供货频次", "sort": 7, "isShow": 0,
                 "isSearch": 0, "isEdit": 0, "haveSearch": 1},
                {"id": "9", "fieldName": "coop_cr_lmt", "desc": "核心企业建议贷款额度（元）", "sort": 8, "isShow": 0, "isSearch": 0,
                 "isEdit": 0, "haveSearch": 0}]}
        r = api_config_dataTable_update(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_config_dataTable_allSelect(self):
        """数据表页面下拉列表集合"""
        r = api_config_dataTable_allSelect(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_009_config_dataTable_getList(self):
    #     """数据表列表"""
    #     r = api_config_dataTable_getList(token_scf_platform)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_010_config_dataTable_list_all(self):
    #     """放款-不分页获取全部数据"""
    #     payload = {
    #         "ctfNum": "",
    #         "ctfTp": "",
    #         "lndEntpCtfNum": "",
    #         "repyAccList": [],
    #         "tableId": 0
    #     }
    #     r = api_config_dataTable_list_all(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_011_config_dataTable_templateData_save(self):
    #     """模板对应的数据表-新增"""
    #     payload = {
    #         "data": [
    #             {}
    #         ],
    #         "tableId": 0
    #     }
    #     r = api_config_dataTable_templateData_save(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_012_config_dataTable_templateData_update(self):
    #     """模板对应的数据表-修改"""
    #     payload = {
    #         "data": {},
    #         "tableId": 0
    #     }
    #     r = api_config_dataTable_templateData_update(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_013_config_dataTable_filterItemId(self):
    #     """服务接口 - 获取过滤模板类型的项目ID集合"""
    #     payload = {
    #         "kind": 0
    #     }
    #     r = api_config_dataTable_filterItemId(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_014_config_dataTable_findDataTable(self):
    #     """服务间接口-确定数据表"""
    #     payload = {
    #         "bankId": 0,
    #         "coreId": 0,
    #         "productId": 0,
    #         "projectId": 0
    #     }
    #     r = api_config_dataTable_findDataTable(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_015_config_dataTable_getOne(self):
    #     """服务接口 - 获取单个数据表"""
    #     payload = {
    #         "tableId": 0
    #     }
    #     r = api_config_dataTable_getOne(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_016_config_dataTable_lending_getTotalAmt(self):
    #     """服务接口-放款获取合作商放款金额"""
    #     payload = {
    #         "kind": 0,
    #         "lendingList": [
    #             {
    #                 "bankId": 0,
    #                 "creditCode": ""
    #             }
    #         ]
    #     }
    #     r = api_config_dataTable_lending_getTotalAmt(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_017_config_dataTable_onlyViewDateTable(self):
    #     """服务-获取数据表数据 - 仅仅针对只查看的数据表"""
    #     payload = {
    #         "ctfNum": "",
    #         "ctfTp": "",
    #         "lndEntpCtfNum": "",
    #         "repyAccList": [],
    #         "tableId": 0
    #     }
    #     r = api_config_dataTable_onlyViewDateTable(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_018_config_dataTable_templateData_download(self):
    #     """服务接口 - 放款数据下载"""
    #     payload = {
    #         "dataTableId": 0,
    #         "lndEntpCtfNum": "",
    #         "repyAccList": []
    #     }
    #     r = api_config_dataTable_templateData_download(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_019_config_dataTable_allSelect(self):
        """【平台方】所属项目查询核心企业"""
        payload = {
            "name": "",
            "enable": "",
            "enterpriseName": "",
            "num": 1,
            "size": 10
        }
        id = api_scfProjectBasis_search(token_scf_platform, payload).json()['datas'][0]['id']
        payload = {
            "itemId": id
        }
        r = api_config_dataTable_queryProjectInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

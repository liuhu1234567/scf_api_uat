from common.do_config import api_host, restime
from common.do_faker import get_number
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from case_api.config_dataTable import api_config_dataTable_save,api_config_dataTable_list
import requests
import unittest
import json

"财务数据/准入历史"


def api_template_api_accessHistory_list(token, payload):
    """准入历史数据列表"""
    url = f'{api_host}/api-scf-data/template/api/accessHistory/list'
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


def api_template_api_accessHistory_update(token, payload):
    """准入历史数据修改"""
    url = f'{api_host}/api-scf-data/template/api/accessHistory/update'
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


def api_template_api_accessHistory_delete(token, payload):
    """准入历史数据删除"""
    url = f'{api_host}/api-scf-data/template/api/accessHistory/delete'
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


def api_template_api_zxLending_delete(token, payload):
    """中信放款数据删除"""
    url = f'{api_host}/api-scf-data/template/api/zxLending/delete'
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


def api_template_api_zxLending_list(token, payload):
    """中信放款数据列表"""
    url = f'{api_host}/api-scf-data/template/api/zxLending/list'
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


def api_template_api_zxLending_update(token, payload):
    """中信放款数据修改"""
    url = f'{api_host}/api-scf-data/template/api/zxLending/update'
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


class TemplateApi(unittest.TestCase):
    def test_001_template_api_accessHistory_list(self):
        """准入历史数据列表"""
        payload = {
            "coopCrLmt": 0,
            "coopMonths": 0,
            "createBy": 0,
            "createTime": "",
            "id": "",
            "indEntpCtfNum": "",
            "indEntpNm": "",
            "lastOrderMaxAmt": 0,
            "lastOrderTotalAmt": 0,
            "lastOrderTotalNum": 0,
            "num": 1,
            "size": 10,
            "tableId": 1562277848618438658,
            "updateBy": 0,
            "updateTime": "",
            "vendorComplRate": "",
            "vendorDeliveryFreq": 0
        }
        r = api_template_api_accessHistory_list(token_scf_supplier, payload)
        r_json = r.json()
        # g_d['id'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_template_api_accessHistory_update(self):
        """准入历史数据修改"""
        payload = {
            "coopCrLmt": 0,
            "coopMonths": 0,
            "createBy": 0,
            "createTime": "",
            "id": g_d.get('id'),
            "indEntpCtfNum": "",
            "indEntpNm": "",
            "lastOrderMaxAmt": 0,
            "lastOrderTotalAmt": 0,
            "lastOrderTotalNum": 0,
            "num": 1,
            "size": 10,
            "tableId": 1562277848618438658,
            "updateBy": 0,
            "updateTime": "",
            "vendorComplRate": "",
            "vendorDeliveryFreq": 0
        }
        r = api_template_api_accessHistory_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_template_api_accessHistory_delete(self):
        """准入历史数据删除"""
        payload = {
            "id": g_d.get('id'),
            "tableId": 1562277848618438658
        }
        r = api_template_api_accessHistory_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    # def test_004_template_api_zxLending_delete(self):
    #     """中信放款数据删除"""
    #     # api_config_dataTable_save(token_scf_supplier,payload = {
    #     #     "fieldList": [
    #     #         {
    #     #             "id": 1,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 1
    #     #         },
    #     #         {
    #     #             "id": 2,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 2
    #     #         },
    #     #         {
    #     #             "id": 3,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 3
    #     #         },
    #     #         {
    #     #             "id": 4,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 4
    #     #         },
    #     #         {
    #     #             "id": 5,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 5
    #     #         },
    #     #         {
    #     #             "id": 6,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 6
    #     #         },
    #     #         {
    #     #             "id": 7,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 7
    #     #         },
    #     #         {
    #     #             "id": 8,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 8
    #     #         },
    #     #         {
    #     #             "id": 9,
    #     #             "isEdit": 1,
    #     #             "isSearch": 1,
    #     #             "isShow": 1,
    #     #             "sort": 9
    #     #         }
    #     #     ],
    #     #     "itemId": 0,
    #     #     "name": f"数据表{get_number(6)}",
    #     #     "templateId": 1,
    #     #     "tenantId": 0,
    #     #     "tenantType": "3,4,5",
    #     #     "type": 1
    #     # })
    #     re = api_config_dataTable_list(token_scf_supplier,payload={
    #         "createBy": 0,
    #         "createTime": "",
    #         "id": 0,
    #         "institutionName": "",
    #         "num": 1,
    #         "productName": "",
    #         "size": 10,
    #         "updateBy": 0,
    #         "updateTime": ""
    #     }).json()
    #     id, tableId = re['datas'][0]['templateId'], re['datas'][0]['id']
    #     payload = {
    #         "id": 2,
    #         "tableId": 1567846917649477633
    #     }
    #     r = api_template_api_zxLending_delete(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime)

    def test_005_template_api_zxLending_list(self):
        """中信放款数据列表"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "ctfNum": "",
            "ctfTp": "",
            "ctrId": "",
            "fncGistList": "",
            "id": 0,
            "iouNum": "",
            "lndEntpCtfNum": "",
            "num": 0,
            "orderNum": "",
            "pyAmt": 0,
            "pyDt": "",
            "pyStat": "",
            "repyAcc": "",
            "repyAccNm": "",
            "repyAccNumDepBnkNm": "",
            "repyDt": "",
            "size": 0,
            "tableId": 1562277848618438658,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_template_api_zxLending_list(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_template_api_zxLending_update(self):
        """中信放款数据修改"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "ctfNum": "",
            "ctfTp": "",
            "ctrId": "",
            "fncGistList": "",
            "id": 0,
            "iouNum": "",
            "lndEntpCtfNum": "",
            "num": 0,
            "orderNum": "",
            "pyAmt": 0,
            "pyDt": "",
            "pyStat": "",
            "repyAcc": "",
            "repyAccNm": "",
            "repyAccNumDepBnkNm": "",
            "repyDt": "",
            "size": 0,
            "tableId": 1567802060780351489,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_template_api_zxLending_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

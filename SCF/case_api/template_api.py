from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json


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


def api_template_api_financing_list(token, payload):
    """融资依据数据列表"""
    url = f'{api_host}/api-scf-data/template/api/financing/list'
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


def api_template_api_financing_update(token, payload):
    """准入历史数据修改"""
    url = f'{api_host}/api-scf-data/template/api/financing/update'
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


def api_template_api_financing_delete(token, payload):
    """融资依据数据删除"""
    url = f'{api_host}/api-scf-data/template/api/financing/delete'
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
            # "coopCrLmt": 0,
            # "coopMonths": 0,
            # "createBy": 0,
            # "createTime": "",
            # "id": "",
            # "indEntpCtfNum": "",
            # "indEntpNm": "",
            # "lastOrderMaxAmt": 0,
            # "lastOrderTotalAmt": 0,
            # "lastOrderTotalNum": 0,
            "num": 1,
            "size": 10,
            "tableId": 1549312997482921986,
            # "updateBy": 0,
            # "updateTime": "",
            # "vendorComplRate": "",
            # "vendorDeliveryFreq": 0
        }
        r = api_template_api_accessHistory_list(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas'][0]['id']
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
            "tableId": 1549312997482921986,
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
            "tableId": 1549312997482921986
        }
        r = api_template_api_accessHistory_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    # def test_template_api_financing_list(self):
    #     """融资依据数据列表"""
    #     payload = {
    #         "createBy": 0,
    #         "createTime": "",
    #         "currency": "",
    #         "id": 0,
    #         "indEntpCtfNum": "",
    #         "indEntpNm": "",
    #         "num": 1,
    #         "orderAmt": 0,
    #         "orderName": "",
    #         "orderNum": "",
    #         "orderOtherName": "",
    #         "orderPyDate": "",
    #         "orderSignDate": "",
    #         "repyAcc": "",
    #         "reserve": "",
    #         "size": 10,
    #         "tableId": 1549312997482921986,
    #         "updateBy": 0,
    #         "updateTime": ""
    #     }
    #     r = api_template_api_financing_list(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime)
    #
    # def test_template_api_financing_update(self):
    #     """准入历史数据修改"""
    #     payload = {
    #         "createBy": 0,
    #         "createTime": "",
    #         "currency": "",
    #         "id": 0,
    #         "indEntpCtfNum": "",
    #         "indEntpNm": "",
    #         "num": 0,
    #         "orderAmt": 0,
    #         "orderName": "",
    #         "orderNum": "",
    #         "orderOtherName": "",
    #         "orderPyDate": "",
    #         "orderSignDate": "",
    #         "repyAcc": "",
    #         "reserve": "",
    #         "size": 0,
    #         "tableId": 1549312997482921986,
    #         "updateBy": 0,
    #         "updateTime": ""
    #     }
    #     r = api_template_api_financing_update(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime)
    #
    # def test_template_api_financing_delete(self):
    #     """融资依据数据删除"""
    #     payload = {
    #         "id": 9103,
    #         "tableId": 1549312997482921986
    #     }
    #     r = api_template_api_financing_delete(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime)

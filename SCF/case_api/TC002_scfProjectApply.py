from common.global_variable import customize_dict
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_config import api_host, restime
import requests
import json
import unittest
from jsonpath import jsonpath
from case_api.scfFinanceProduct import api_scfFinanceProduct_projectDeliverSearch


def api_scfProjectApply_isCertificate(token, payload):
    """验证当前用户所在的企业是否已认证"""
    url = f'{api_host}/api-scf/scfProjectApply/isCertificate'
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


def api_scfProjectApply_listRepayment(token, payload):
    """获取还款方式"""
    url = f'{api_host}/api-scf/scfProjectApply/listRepayment'
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


def api_scfProjectApply_toApply(token, payload):
    """跳转至 ”申请融资“ 页面"""
    url = f'{api_host}/api-scf/scfProjectApply/toApply'
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


def api_scfProjectApply_apply(token, payload):
    """申请融资"""
    url = f'{api_host}/api-scf/scfProjectApply/apply'
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


def api_scfProjectApply_viewApply(token, payload):
    """查看融资申请信息"""
    url = f'{api_host}/api-scf/scfProjectApply/viewApply'
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


class ScfProjectApply(unittest.TestCase):
    def test_001_scfProjectApply_isCertificate(self):
        """【供应商】验证当前用户所在的企业是否已认证"""
        payload = {}
        r = api_scfProjectApply_isCertificate(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_scfProjectApply_listRepayment(self):
        """【供应商】获取还款方式"""
        payload = {}
        r = api_scfProjectApply_listRepayment(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        repayName = ['到期一次还本付息', '等额本息', '等额本金', '按期还本付息', '先息后本']
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertEqual(repayName, jsonpath(r_json, '$..name'))
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_scfProjectApply_toApply(self):
        """【供应商】跳转至 ”申请融资“ 页面"""
        payload = {
            "enable": True,
            "entName": "",
            "enterpriseId": 0,
            "financeName": "",
            "isApply": False,
            "num": 1,
            "productName": "",
            "projectName": "",
            "size": 10
        }
        g_d['projectDeliverId'] = \
        api_scfFinanceProduct_projectDeliverSearch(token_scf_supplier, payload).json()['datas'][0]['id']
        payload = {
            "projectDeliverId": g_d.get('projectDeliverId')
        }
        r = api_scfProjectApply_toApply(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_scfProjectApply_apply(self):
        """【供应商】申请融资"""
        payload = {
            "projectDeliverId": g_d.get('projectDeliverId')
        }
        r = api_scfProjectApply_apply(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_scfProjectApply_viewApply(self):
        """【供应商】查看融资申请信息"""
        payload = {
            "id": g_d.get('projectDeliverId')
        }
        r = api_scfProjectApply_viewApply(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

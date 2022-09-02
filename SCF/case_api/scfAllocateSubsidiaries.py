from common.global_variable import customize_dict
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.do_config import api_host, restime
import requests
import json
import unittest


def api_scfAllocateSubsidiaries_queryAll(token):
    """查询"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/queryAll'
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


def api_scfAllocateSubsidiaries_queryList(token):
    """获取子公司分配额度信息"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/queryList'
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


def api_scfAllocateSubsidiaries_insert(token, payload):
    """新增"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/insert'
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


def api_scfAllocateSubsidiaries_batch(token, payload):
    """批量"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/batch'
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


def api_scfAllocateSubsidiaries_update(token, payload):
    """编辑"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/update'
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


def api_scfAllocateSubsidiaries_queryPage(token, payload):
    """分页查询"""
    url = f'{api_host}/api-scf/scfAllocateSubsidiaries/queryPage'
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

class ScfAllocateSubsidiaries(unittest.TestCase):
    def test_001_scfAllocateSubsidiaries_queryAll(self):
        """【核心企业】查询"""
        r = api_scfAllocateSubsidiaries_queryAll(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_scfAllocateSubsidiaries_ueryList(self):
        """【核心企业】获取子公司分配额度信息"""
        r = api_scfAllocateSubsidiaries_queryList(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_scfAllocateSubsidiaries_insert(self):
        """【核心企业】新增"""
        payload = {
            "allocateAmount": 100000,
            "creditCode": "X2342342X",
            "subsidiariesName": "中国恭敬公司"
        }
        r = api_scfAllocateSubsidiaries_insert(token_scf_enterprise, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_004_scfAllocateSubsidiaries_batch(self):
        """【核心企业】批量"""
        payload = [
            {
                "allocateAmount": 111,
                "creditCode": "X2342342X",
                "subsidiariesName": "中国恭敬公司"
            }
        ]
        r = api_scfAllocateSubsidiaries_batch(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_scfAllocateSubsidiaries_update(self):
        """【核心企业】编辑"""
        payload = {
            "allocateAmount": 111,
            "applyAmount": 1,
            "creditCode": "X2342342X",
            "id": 0,
            "subsidiariesName": "中国恭敬公司"
        }
        r = api_scfAllocateSubsidiaries_update(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_006_scfAllocateSubsidiaries_update(self):
        """【核心企业】分页查询"""
        payload = {
            "allocateAmount": 0,
            "coreId": 0,
            "createBy": 0,
            "createTime": "",
            "creditCode": "",
            "id": 0,
            "num": 0,
            "size": 0,
            "updateBy": 0,
            "updateTime": "",
            "userAmount": 0
        }
        r = api_scfAllocateSubsidiaries_queryPage(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)



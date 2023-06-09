from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from case_api.otherApi import api_otherApi_queryProjectList
from common.do_faker import get_number, get_card_number
import requests
import unittest
import json


def api_backAccount_insert(token, payload):
    """【平台方】新增银行账户"""
    url = f'{api_host}/api-scf/backAccount/insert'
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


def api_backAccount_queryPage(token, payload):
    """【平台方】分页查询银行账户"""
    url = f'{api_host}/api-scf/backAccount/queryPage'
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


def api_backAccount_update(token, payload):
    """【平台方】修改银行账户"""
    url = f'{api_host}/api-scf/backAccount/update'
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


def api_backAccount_delete(token, payload):
    """【平台方】删除银行账户"""
    url = f'{api_host}/api-scf/backAccount/delete'
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


def api_backAccount_bindByProjectId(token, payload):
    """绑定项目-银行卡"""
    url = f'{api_host}/api-scf/backAccount/bindByProjectId'
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


def api_backAccount_validCardID(token, payload):
    """获取认证过的银行卡信息"""
    url = f'{api_host}/api-scf/backAccount/validCardID'
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


def api_backAccount_queryBindById(token, payload):
    """查询已绑定项目-银行卡"""
    url = f'{api_host}/api-scf/backAccount/queryBindById'
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


def api_backAccount_queryBankAccountList(token, payload):
    """根据项目id查询代扣银行账户列表"""
    url = f'{api_host}/api-scf/backAccount/queryBankAccountList'
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


def api_backAccount_queryListByProjectId(token, payload):
    """根据项目id查询银行账户列表"""
    url = f'{api_host}/api-scf/backAccount/queryListByProjectId'
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


def api_backAccount_queryListFelationByProjectId(token, payload):
    """根据项目id查询银行关联账户列表"""
    url = f'{api_host}/api-scf/backAccount/queryListFelationByProjectId'
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


class BackAccount(unittest.TestCase):
    def test_001_backAccount_insert(self):
        """【平台方】新增银行账户"""
        number = get_number(10)
        card_number = get_card_number()
        payload = {
            "bankAccountDebutNo": number,
            "bankAccountName": f"账户名称{number}",
            "bankAccountNo": card_number,
            "bankAccountSite": "深圳市兴东路点链支行",
            "bankAccountType": 2
        }
        r = api_backAccount_insert(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_backAccount_queryPage(self):
        """【平台方】分页查询银行账户"""
        payload = {
            "bankAccountName": "",
            "bankAccountNo": "",
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_backAccount_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_backAccount_update(self):
        """【平台方】修改银行账户"""
        number = get_number(10)
        card_number = get_card_number()
        payload = {
            "bankAccountDebutNo": number,
            "bankAccountName": f"账户名称{number}",
            "bankAccountNo": card_number,
            "bankAccountSite": "深圳市兴东路点链支行",
            "bankAccountType": 0,
            "id": g_d.get('id')
        }
        r = api_backAccount_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_004_backAccount_delete(self):
        """【平台方】删除银行账户"""
        payload = {"id": g_d.get('id')}
        r = api_backAccount_delete(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_backAccount_bindByProjectId(self):
        """绑定项目-银行卡 V2.1.1修改"""
        payload_new = {
            "id": "1567401221412044802",
            "scfBankAccountBindProjectReqList": [
                {
                    "projectId": "1582635711985631234",
                    "projectName": "项目名称762149"
                }
            ]
        }
        r = api_backAccount_bindByProjectId(token_scf_supplier, payload_new)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_backAccount_validCardID(self):
        """获取认证过的银行卡信息"""
        payload = {
        }
        r = api_backAccount_validCardID(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_backAccount_queryBindById(self):
        """查询已绑定项目-银行卡 V2.1.1修改"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_backAccount_queryBindById(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_backAccount_queryBankAccountList(self):
        """根据项目id查询代扣银行账户列表 V2.1.1新增"""
        payload = {
            "projectId": 0
        }
        r = api_backAccount_queryBankAccountList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_009_backAccount_queryListByProjectId(self):
        """根据项目id查询代扣银行账户列表"""
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 1,
            "size": 10,
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_backAccount_queryListByProjectId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_010_backAccount_queryListFelationByProjectId(self):
        """根据项目id查询银行关联账户列表 V2.1.1新增"""
        payload = {
            "createBy": "",
            "createTime": "",
            "id": "",
            "num": 1,
            "size": 10,
            "updateBy": "",
            "updateTime": ""
        }
        r = api_backAccount_queryListFelationByProjectId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

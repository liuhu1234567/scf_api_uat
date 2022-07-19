from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
import requests
import unittest
import json
from common.do_faker import get_name, get_phone, get_email, get_sfz, get_number, get_company, get_card_number


def api_enterprise_check_key(token, payload):
    """校验用户选择的ukey否正确"""
    url = f'{api_host}/api-scf/enterprise/check/key'
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


def api_enterprise_get_pdf_hash(token, payload):
    """经办人或者审核人确认获取pdfhash值"""
    url = f'{api_host}/api-scf/enterprise/get/pdf/hash'
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


def api_enterprise_queryById(token, payload):
    """【供应商/经销商】根据ID查询企业档案详情"""
    url = f'{api_host}/api-scf/enterprise/queryById'
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


def api_enterprise_queryByUserId(token):
    """企业档案详情-当前用户"""
    url = f'{api_host}/api-scf/enterprise/queryByUserId'
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


def api_enterprise_queryPage(token, payload):
    """【供应商/经销商】分页查询企业档案列表"""
    url = f'{api_host}/api-scf/enterprise/queryPage'
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


def api_enterprise_step1(token, payload):
    """【供应商/经销商】企业认证步骤1-完善企业工商信息"""
    url = f'{api_host}/api-scf/enterprise/step1'
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


def api_enterprise_step2(token, payload):
    """【供应商/经销商】企业认证步骤2-开通电子签章"""
    url = f'{api_host}/api-scf/enterprise/step2'
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


def api_enterprise_step3(token, payload):
    """【供应商/经销商】企业认证步骤3-签署授权书及平台协议"""
    url = f'{api_host}/api-scf/enterprise/step3'
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


def api_enterprise_update_save(token, payload):
    """修改企业档案-保存"""
    url = f'{api_host}/api-scf/enterprise/update/save'
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


def api_enterprise_update_submit(token, payload):
    """修改企业档案-提交"""
    url = f'{api_host}/api-scf/enterprise/update/submit'
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


def api_enterprise_updateCustomerType(token, payload):
    """企业初次登入页面关联客户状态"""
    url = f'{api_host}/api-scf/enterprise/updateCustomerType'
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


class Enterprise(unittest.TestCase):
    def test_001_enterprise_check_key(self):
        """校验用户选择的ukey否正确"""
        payload = {"id": ""}
        r = api_enterprise_check_key(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_enterprise_get_pdf_hash(self):
        """经办人或者审核人确认获取pdf hash值"""
        payload = {
            "certContent": "",
            "commitPayDate": "",
            "id": "",
            "img": "",
            "openAmount": "",
            "openCube": "",
            "pdfHash": "",
            "pdfHashId": "",
            "saleCompany": "",
            "type": 0
        }
        r = api_enterprise_get_pdf_hash(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_enterprise_queryByUserId(self):
        """企业档案详情-当前用户"""
        r = api_enterprise_queryByUserId(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_enterprise_queryPage(self):
        """【供应商/经销商】分页查询企业档案列表"""
        payload = {"num": "1", "size": "10"}
        r = api_enterprise_queryPage(token_scf_supplier, payload)
        r_json = r.json()
        g_d['id'] = r_json['datas'][0]['id']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_003_enterprise_queryById(self):
        """【供应商/经销商】根据ID查询企业档案详情"""
        payload = {"id": g_d.get('id')}
        r = api_enterprise_queryById(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_101_enterprise_step1(self):
        """【供应商/经销商】企业认证步骤1-完善企业工商信息"""
        name = get_name()
        sfz = get_sfz()
        email = get_email()
        phone = get_phone()
        number = get_number(8)
        company_name = get_company()
        payload = {
            "businessLicense": "",
            "confirmImage": "",
            "contact": name,
            "contactCardId": sfz,
            "contactCardIdImage": "",
            "contactCardType": 0,
            "contactEmail": email,
            "contactMobile": phone,
            "contactPosition": "",
            "creditCode": number,
            "detailedAddress": "深圳",
            "entName": company_name,
            "entScale": 0,
            "entType": 0,
            "industry": 0,
            "legalCardId": sfz,
            "legalCardIdImage": "",
            "legalCardType": 0,
            "legalName": name,
            "legalPhone": phone,
            "legalPosition": "",
            "region": "",
            "registeredAddress": "深圳",
            "telephone": ""
        }
        r = api_enterprise_step1(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_102_enterprise_step2(self):
        """【供应商/经销商】企业认证步骤2-开通电子签章"""
        number = get_number(6)
        card_number = get_card_number()
        payload = {
            "accountTitle": f"账户{number}",
            "bankAccount": card_number,
            "bankDepositNo": number,
            "bankOutlet": "深圳宝安某一个银行",
            "validMoney": "1000"
        }
        r = api_enterprise_step2(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_103_enterprise_step3(self):
        """【供应商/经销商】企业认证步骤3-签署授权书及平台协议"""
        payload = {
            "confirmLicense": "",
            "ruleLicense": "",
            "serviceLicense": ""
        }
        r = api_enterprise_step3(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_104_enterprise_update_save(self):
        """修改企业档案-保存"""
        name = get_name()
        sfz = get_sfz()
        email = get_email()
        phone = get_phone()
        number = get_number(8)
        company_name = get_company()
        payload = {
            "contact": name,
            "contactCardId": sfz,
            "contactCardType": 0,
            "contactEmail": email,
            "contactMobile": phone,
            "contactPosition": "",
            "creditCode": number,
            "detailedAddress": "深圳",
            "entName": company_name,
            "entScale": 0,
            "entType": 0,
            "id": 0,
            "industry": 0,
            "legalCardId": sfz,
            "legalCardType": 0,
            "legalName": name,
            "legalPhone": phone,
            "legalPosition": "",
            "region": "深圳",
            "registeredAddress": "",
            "telephone": ""
        }
        r = api_enterprise_update_save(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_105_enterprise_update_submit(self):
        """修改企业档案-提交"""
        name = get_name()
        sfz = get_sfz()
        email = get_email()
        phone = get_phone()
        number = get_number(8)
        company_name = get_company()
        payload = {
            "contact": name,
            "contactCardId": sfz,
            "contactCardType": 0,
            "contactEmail": email,
            "contactMobile": phone,
            "contactPosition": "",
            "creditCode": number,
            "detailedAddress": "深圳",
            "entName": company_name,
            "entScale": 0,
            "entType": 0,
            "id": 0,
            "industry": 0,
            "legalCardId": sfz,
            "legalCardType": 0,
            "legalName": name,
            "legalPhone": phone,
            "legalPosition": "",
            "region": "深圳",
            "registeredAddress": "",
            "telephone": ""
        }
        r = api_enterprise_update_submit(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_enterprise_updateCustomerType(self):
        """企业初次登入页面关联客户状态"""
        payload = {
            "channel": 0,
            "coreEnterprise": "",
            "customerType": 0,
            "id": ""
        }
        r = api_enterprise_updateCustomerType(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)
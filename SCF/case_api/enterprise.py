from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
import requests
import unittest
import json
from common.do_faker import get_name, get_phone, get_email, get_sfz, get_number, get_company, get_card_number
from case_api.customerManager import api_customerManager_queryAuditPage


def api_enterprise_check_key(token, payload):
    """校验用户选择的ukey否正确"""
    url = f'{api_host}/api-scf/enterprise/check/key'
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


def api_enterprise_pdf_hash(token, payload):
    """经办人或者审核人确认获取pdfhash值"""
    url = f'{api_host}/api-scf/enterprise/pdf/hash'
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


def api_enterprise_step4(token):
    """企业认证步骤4"""
    url = f'{api_host}/api-scf/enterprise/step4'
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


def api_enterprise_pdf_show(token, payload):
    """展示签名信息"""
    url = f'{api_host}/api-scf/enterprise/pdf/show'
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


def api_enterprise_step2_valid(token, payload):
    """企业认证步骤2-检测银行卡"""
    url = f'{api_host}/api-scf/enterprise/step2/valid'
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


def api_enterprise_queryEntArchivesDetail(token):
    """企业档案详情-当前用户"""
    url = f'{api_host}/api-scf/enterprise/queryEntArchivesDetail'
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


def api_enterprise_queryEntArchivesDetailNonCache(token):
    """企业档案详情-当前用户(非缓存)"""
    url = f'{api_host}/api-scf/enterprise/queryEntArchivesDetailNonCache'
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


def api_enterprise_pdf_document(token):
    """平台服务协议"""
    url = f'{api_host}/api-scf/enterprise/pdf/document'
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


def api_enterprise_queryBankList(token):
    """银行信息"""
    url = f'{api_host}/api-scf/enterprise/queryBankList'
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


def api_enterprise_queryByEntName(token, payload):
    """根据企业名称查询企业档案详情"""
    url = f'{api_host}/api-scf/enterprise/queryByEntName'
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


def api_enterprise_queryFunderList(token):
    """资金方信息"""
    url = f'{api_host}/api-scf/enterprise/queryFunderList'
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


def api_enterprise_queryGuarantorList(token):
    """担保方列表信息"""
    url = f'{api_host}/api-scf/enterprise/queryGuarantorList'
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


def api_enterprise_querySupplierList(token):
    """供应商信息"""
    url = f'{api_host}/api-scf/enterprise/querySupplierList'
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


def api_enterprise_queryBuyerList(token, payload):
    """买方列表，即核心企业子公司"""
    url = f'{api_host}/api-scf/enterprise/queryBuyerList'
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


def api_enterprise_pdf_node_document(token, payload):
    """平台服务协议-节点合同"""
    url = f'{api_host}/api-scf/enterprise/pdf/node/document'
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

    # def test_002_enterprise_get_pdf_hash(self):
    #     """经办人或者审核人确认获取pdf hash值,需要使用Ukey访问"""
    #     payload = {
    #         "certContent": "",
    #         "fileId": "",
    #         "keyWord": ""
    #     }
    #     r = api_enterprise_pdf_hash(token_scf_supplier, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime)

    def test_003_enterprise_queryPage(self):
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

    def test_004_enterprise_queryById(self):
        """【供应商/经销商】根据ID查询企业档案详情"""
        payload = {"id": g_d.get('id')}
        r = api_enterprise_queryById(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_005_enterprise_step1(self):
        """【供应商/经销商】企业认证步骤1-完善企业工商信息"""
        name = get_name()
        g_d["name"] = name
        sfz = get_sfz()
        email = get_email()
        phone = get_phone()
        number = get_number(10)
        number_two = get_number(7)
        g_d["creditCode"] = f'{number}{number_two}H'
        company_name = get_company()
        payload = {
            "businessLicense": "",
            "confirmIage": "",
            "contact": name,
            "contactCardId": sfz,
            "contactCardIdImage": "",
            "contactCardType": 0,
            "contactEmail": email,
            "contactMobile": phone,
            "contactPosition": "",
            "creditCode": g_d.get("creditCode"),
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
            "region": "深圳",
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

    def test_006_enterprise_step2_valid(self):
        """企业认证步骤2-检测银行卡"""
        payload = {
            "bankAccountDebutNo": "深圳市天富包装制品有限公司",
            "bankAccountName": f"账户{get_number(6)}",
            "bankAccountNo": get_card_number(),
            "bankAccountSite": "恒生银行中国有限公司深圳分行"
        }
        r = api_enterprise_step2_valid(token_scf_supplier, payload)
        r_json = r.json()
        g_d['originalTxSn'] = r_json['datas']
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_007_enterprise_step2(self):
        """【供应商/经销商】企业认证步骤2-开通电子签章"""
        number = get_number(6)
        payload = {
            "bankAccountDebutNo": "深圳市天富包装制品有限公司",
            "bankAccountName": f"账户{get_number(6)}",
            "bankAccountNo": get_card_number(),
            "bankAccountSite": "恒生银行中国有限公司深圳分行",
            "originalTxSn": g_d.get('originalTxSn'),
            "validMoney": "1"
        }
        r = api_enterprise_step2(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_008_enterprise_step3(self):
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

    def test_009_enterprise_step4(self):
        """【供应商/经销商】企业认证步骤4"""
        r = api_enterprise_step4(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_010_enterprise_update_save(self):
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

    def test_011_enterprise_update_submit(self):
        """修改企业档案-提交"""
        name = get_name()
        sfz = get_sfz()
        email = get_email()
        phone = get_phone()
        number = get_number(10)
        number_two = get_number(7)
        company_name = get_company()
        payload = {
            "contact": g_d.get("name"),
            "contactCardId": sfz,
            "contactCardType": 0,
            "contactEmail": email,
            "contactMobile": phone,
            "contactPosition": "",
            "creditCode": g_d.get("creditCode"),
            "detailedAddress": "深圳",
            "entName": company_name,
            "entScale": 0,
            "entType": 0,
            "id": g_d.get("id"),
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

    def test_012_enterprise_updateCustomerType(self):
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

    def test_013_enterprise_pdf_show(self):
        """展示签名信息"""
        payload = {
            "certContent": "",
            "fileId": "",
            "hashId": "",
            "keyWord": ""
        }
        r = api_enterprise_pdf_show(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_014_enterprise_queryEntArchivesDetail(self):
        """【供应商】企业档案详情-当前用户"""
        r = api_enterprise_queryEntArchivesDetail(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_015_enterprise_queryEntArchivesDetail(self):
        """【供应商】企业档案详情-当前用户(非缓存)"""
        r = api_enterprise_queryEntArchivesDetailNonCache(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_016_enterprise_pdf_document(self):
        """【供应商】平台服务协议"""
        r = api_enterprise_pdf_document(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_017_enterprise_queryBankList(self):
        """【供应商】银行信息"""
        r = api_enterprise_queryBankList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_018_enterprise_queryByEntName(self):
        """【供应商】根据企业名称查询企业档案详情"""
        payload = {
            "entName": "",
            "contact": "",
            "contactMobile": "",
            "auditStatus": 3,
            "num": 1,
            "size": 10
        }
        entName = api_customerManager_queryAuditPage(token_scf_platform, payload).json()["datas"][3]["entName"]
        payload = {
            "entName": entName
        }
        r = api_enterprise_queryByEntName(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_019_enterprise_queryFunderList(self):
        """【供应商】资金方信息"""
        r = api_enterprise_queryFunderList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_020_enterprise_queryGuarantorList(self):
        """【供应商】担保方列表信息"""
        r = api_enterprise_queryGuarantorList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_021_enterprise_querySupplierList(self):
        """【供应商】供应商信息"""
        r = api_enterprise_querySupplierList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_022_enterprise_queryBuyerList(self):
        """【核心企业】买方列表，即核心企业子公司"""
        coreEntName = api_enterprise_queryEntArchivesDetail(token_scf_enterprise).json()['datas']['entName']
        payload = {
            "coreEntName": coreEntName,
        }
        r = api_enterprise_queryBuyerList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_023_enterprise_pdf_node_document(self):
        """【供应商】买方列表，即核心企业子公司"""
        payload = {}
        r = api_enterprise_pdf_node_document(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

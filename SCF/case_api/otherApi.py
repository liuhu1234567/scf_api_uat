from common.do_config import api_host, restime
from common.get_token import token_scf_platform, token_scf_supplier, token_scf_financier, token_scf_factor, \
    token_scf_subsidiaries, token_scf_enterprise
from common.global_variable import customize_dict
from config.all_path import get_file_path
from case_api.TC001_scfProjectBasis import api_scfProjectBasis_listProjectBasisByType
import requests
import unittest
import json
from case_api.enterprise import api_enterprise_queryEntArchivesDetail

"""公共接口"""


def api_otherApi_initDropdownListInfo(token, payload):
    """枚举下拉列表信息集"""
    url = f'{api_host}/api-scf/otherApi/initDropdownListInfo'
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


# def api_otherApi_queryById(token, payload):
#     """根据传入的ID集返回名称详情"""
#     url = f'{api_host}/api-scf/otherApi/queryById'
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


def api_otherApi_queryDownList(token, payload):
    """项目列表，核心企业，金融产品，金融机构下拉列表"""
    url = f'{api_host}/api-scf/otherApi/queryDownList'
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


# def api_otherApi_queryProjectInfo(token, payload):
#     """服务-查询项目相关信息"""
#     url = f'{api_host}/api-scf/otherApi/queryProjectInfo'
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


def api_template_upload_file(token, file_name):
    """上传文件"""
    url = f'{api_host}/api-scf/template/upload/file'
    headers = {
        "x-appid-header": "2",
        "Authorization": token
    }
    png_path = get_file_path(file_name)
    with open(png_path, 'rb') as f:
        file_b = f.read()
    files = {
        'file': (file_name, file_b, "png")
    }
    r = requests.post(url, headers=headers, files=files)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


def api_otherApi_queryProjectList(token):
    """项目下拉列表"""
    url = f'{api_host}/api-scf/otherApi/queryProjectList'
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


def api_admission_queryDownList(token, payload):
    """准入-项目列表，核心企业，金融产品，金融机构下拉列表"""
    url = f'{api_host}/api-scf/admission/queryDownList'
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


def api_admission_queryCreditDownList(token):
    """授信项目列表"""
    url = f'{api_host}/api-scf/admission/queryCreditDownList'
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


def api_auditFlow_queryByFlowItemId(token, payload):
    """查询流程详情"""
    url = f'{api_host}/api-scf/auditFlow/queryByFlowItemId'
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


def api_blockchain_info(token, payload):
    """查询区块链信息"""
    url = f'{api_host}/api-scf/blockchain/info'
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


def api_downLoadExcel(token, payload):
    """根据名称下载excel模板"""
    url = f'{api_host}/api-scf/downLoadExcel'
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


def api_enterprise_pdf_listAddCreditDocument(token):
    """额度新增显示文件树"""
    url = f'{api_host}/api-scf/enterprise/pdf/listAddCreditDocument'
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


def api_enterprise_pdf_listUpdateCreditDocument(token):
    """额度变更显示文件树"""
    url = f'{api_host}/api-scf/enterprise/pdf/listUpdateCreditDocument'
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


def api_enterprise_pdf_node_document(token):
    """平台服务协议-节点合同"""
    url = f'{api_host}/api-scf/enterprise/pdf/node/document'
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


def api_otherApi_queryDownListSpanCredit(token):
    """项目列表-授信专用"""
    url = f'{api_host}/api-scf/otherApi/queryDownListSpanCredit'
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


def api_otherApi_queryDownListSpanCreditCore(token):
    """项目列表-授信中核心企业专用"""
    url = f'{api_host}/api-scf/otherApi/queryDownListSpanCreditCore'
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


def api_otherApi_queryProjectByIdList(token, payload):
    """按企业ID查询项目下拉列表"""
    url = f'{api_host}/api-scf/otherApi/queryProjectByIdList'
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


def api_anxinsign_downloading(token, payload):
    """安心签章-下载合同"""
    url = f'{api_host}/api-scf/anxinsign/downloading'
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

def api_enterprise_pdf_document(token, payload):
    """平台服务协议"""
    url = f'{api_host}/api-scf/enterprise/pdf/document'
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


class OtherApi(unittest.TestCase):
    def test_001_otherApi_initDropdownListInfo(self):
        """【平台方】枚举下拉列表信息集"""
        payload = {
        }
        r = api_otherApi_initDropdownListInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_002_otherApi_queryById(self):
    #     """【平台方】根据传入的ID集返回名称详情"""
    #     payload = [
    #         {
    #             "institutionId": 0,
    #             "itemId": 0,
    #             "productId": 0,
    #             "templateId": 0,
    #             "tenantId": 0
    #         }
    #     ]
    #     r = api_otherApi_queryById(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_otherApi_queryDownList(self):
        """【平台方】项目列表，核心企业，金融产品，金融机构下拉列表"""
        payload = {
        }
        r = api_otherApi_queryDownList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_004_otherApi_queryProjectInfo(self):
    #     """【平台方】服务-查询项目相关信息"""
    #     payload = {
    #         "businessType": ""
    #     }
    #     itemId = api_scfProjectBasis_listProjectBasisByType(token_scf_platform, payload).json()["datas"][0]["id"]
    #     payload = {
    #         "itemId": itemId
    #     }
    #     r = api_otherApi_queryProjectInfo(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_template_upload_file(self):
        """【平台方】上传文件"""
        r = api_template_upload_file(token_scf_platform, "test.png")
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_otherApi_queryProjectList(self):
        """【供应商】项目下拉列表"""
        r = api_otherApi_queryProjectList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_007_admission_queryDownList(self):
        """【供应商】准入-项目列表，核心企业，金融产品，金融机构下拉列表"""
        g_d['entId'] = api_enterprise_queryEntArchivesDetail(token_scf_supplier).json()['datas']['id']
        payload = {
            "entId": g_d.get('entId')
        }
        r = api_admission_queryDownList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_008_admission_queryCreditDownList(self):
        """【供应商】授信项目列表"""
        r = api_admission_queryCreditDownList(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_009_auditFlow_queryByFlowItemId(self):
        """【平台方】查询流程详情"""
        payload = {
            "flowItemId": 0
        }
        r = api_auditFlow_queryByFlowItemId(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_010_blockchain_info(self):
        """【核心企业】查询区块链信息"""
        payload = {
            "busId": "JDX20375982046",
            "busType": 2
        }
        r = api_blockchain_info(token_scf_enterprise, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_011_downLoadExcel(self):
        """【平台方】根据名称下载excel模板"""
        payload = {
            "name": "批量分配模板.xlsx"
        }
        r = api_downLoadExcel(token_scf_platform, payload)
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r.status_code)
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_012_enterprise_pdf_listAddCreditDocument(self):
        """【核心企业】额度新增显示文件树"""
        r = api_enterprise_pdf_listAddCreditDocument(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_013_enterprise_pdf_listUpdateCreditDocument(self):
        """【核心企业】额度变更显示文件树"""
        r = api_enterprise_pdf_listUpdateCreditDocument(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_014_enterprise_pdf_node_document(self):
        """【供应商】平台服务协议-节点合同"""
        r = api_enterprise_pdf_node_document(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_015_otherApi_queryDownListSpanCredit(self):
        """【供应商】项目列表-授信专用"""
        r = api_otherApi_queryDownListSpanCredit(token_scf_supplier)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_016_otherApi_queryDownListSpanCreditCore(self):
        """【核心企业】项目列表-授信中核心企业专用"""
        r = api_otherApi_queryDownListSpanCreditCore(token_scf_enterprise)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_017_otherApi_queryProjectByIdList(self):
        """【供应商】按企业ID查询项目下拉列表"""
        payload = {
            "coreEntId": 0,
            "coreEntName": ""
        }
        r = api_otherApi_queryProjectByIdList(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_018_anxinsign_downloading(self):
        """【平台方】安心签章-下载合同"""
        payload = {
            "id": ""
        }
        r = api_anxinsign_downloading(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_019_enterprise_pdf_document(self):
        """【平台方】平台服务协议"""
        payload = {}
        r = api_enterprise_pdf_document(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')
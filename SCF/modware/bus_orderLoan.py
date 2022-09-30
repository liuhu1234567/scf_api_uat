from common.get_token import *
from common.do_faker import *
from common.do_config import api_host
from functools import wraps
from case_api.goldenLetter_ import api_goldenLetter_open_insert, api_goldenLetter_open_updateAuditStatus, \
    api_goldenLetter_open_queryPage
import json
import requests


# def add_scfFinanceProduct(func, *args, **kwargs):
#     def wrapper( *args, **kwargs):
#         """【平台方】新增金融产品"""
#         payload = {"name":"自动化金融产品" + get_number(4),
#                    "financeId":"1547048461623263234",
#                    "amountMin":1,
#                    "amountMax":1000,
#                    "rateMin":0,
#                    "rateMax":5,
#                    "loop":True,
#                    "single":True,
#                    "pay":True,
#                    "repaymentType":1,
#                    "availableBegin":"2022-09-27 19:32:43",
#                    "availableEnd":"2033-09-25 19:32:50",
#                    "loanBegin":"2022-09-27 19:33:02",
#                    "loanEnd":"2031-09-28 19:33:09"}
#         url = f'{api_host}/api-scf/scfFinanceProduct/insert'
#         headers = {
#             "Content-Type": "application/json;charset=UTF-8",
#             "x-appid-header": "2",
#             "Authorization": token_scf_platform
#         }
#         r = requests.post(url, headers=headers, data=json.dumps(payload))
#         r_json = r.json()
#         scfFinanceProductId = r_json['datas']
#         print(f'流程步骤: 【平台方】新增金融产品,返回金融产品scfFinanceProductId:{scfFinanceProductId}')
#         print(f'接口响应为：{r_json}')
#         func(scfFinanceProductId= scfFinanceProductId)
#         return scfFinanceProductId
#     return wrapper
#
# @add_scfFinanceProduct
# def add_scfProjectBasis(func, scfFinanceProductId, *args, **kwargs):
#     def wrapper(scfFinanceProductId, *args, **kwargs):
#         """【平台方】新增项目"""
#         payload = {
#             "scfProjectBasisReq":
#                 {"id":"",
#                  "bankId":"1547048461623263234",
#                  "businessType":2,
#                  "enterpriseId":"1565528298128351233",
#                  "name":"自动化项目" + get_number(4),
#                  "open":False,
#                  "refactor":False,
#                  "scfFinanceProductId":scfFinanceProductId,
#                  "enter":False,
#                  "grants":False,
#                  "transfer":False,
#                  "finance":True,
#                  "isCoreGrant":True,
#                  "bankName":"泛光灯",
#                  "flowName":["6"]},
#             "scfProjectEnterReq":
#                 {"isTemplate":False,
#                  "flowId":"",
#                  "filePath":"",
#                  "grantFlowItemId":"",
#                  "link":"",
#                  "scfProjectFlowEnterReq":
#                      {"name":"",
#                       "step":0,
#                       "flowItems":[]}},
#             "scfProjectGrantReq":
#                 {"isTemplate":False,
#                  "flowId":"",
#                  "isPush":False,
#                  "useScope":1,
#                  "scfProjectFlowReq":
#                      {"name":"",
#                       "step":0,
#                       "flowItems":[]}},
#             "scfProjectFinanceReq":
#                 {"isTemplate":False,
#                  "flowId":"",
#                  "isHistory":True,
#                  "isPush":True,
#                  "pushMaterial":0,
#                  "serviceRate":1,
#                  "financeRate":1,
#                  "scfProjectFlowReq":
#                      {"name":"自动化流程" + get_number(4),
#                       "step":1,
#                       "flowItems":
#                           [{"customerType":"11",
#                             "isExternal":False,
#                             "reportId":"","isPush":False,
#                             "isProtocol":False,"subs":[],
#                             "customerTypeName":"平台方"}]}},
#             "scfProjectRefactorReq":
#                 {"flowId":"",
#                  "isTemplate":False,
#                  "isHistory":False,
#                  "isPush":False,
#                  "pushMaterial":0,
#                  "serviceRate":0,
#                  "financeRate":0,
#                  "scfProjectFlowReq":{"name":"","step":0,"flowItems":[]}}}
#         url = f'{api_host}/api-scf/scfProjectBasis/insertAllDetail'
#         headers = {
#             "Content-Type": "application/json;charset=UTF-8",
#             "x-appid-header": "2",
#             "Authorization": token_scf_platform
#         }
#         r = requests.post(url, headers=headers, data=json.dumps(payload))
#         r_json = r.json()
#         scfProjectBasisId = r_json['datas']
#         print(f'流程步骤: 【平台方】新增金融产品,返回项目scfProjectBasisId:{scfProjectBasisId}')
#         print(f'接口响应为：{r_json}')
#         func(scfProjectBasisId = scfProjectBasisId)
#         return scfProjectBasisId
#     return wrapper

class Bus_orderLoan():
    def __init__(self):
        self.g_d = {}

    def add_scfFinanceProduct(self):
        """【平台方】新增金融产品，生成金融产品Id"""
        payload = {"name": "自动化金融产品" + get_number(6),
                   "financeId": "1547048461623263234",
                   "amountMin": 1,
                   "amountMax": 1000,
                   "rateMin": 0,
                   "rateMax": 5,
                   "loop": True,
                   "single": True,
                   "pay": True,
                   "repaymentType": 1,
                   "availableBegin": "2022-09-27 19:32:43",
                   "availableEnd": "2033-09-25 19:32:50",
                   "loanBegin": "2022-09-27 19:33:02",
                   "loanEnd": "2031-09-28 19:33:09"}
        url = f'{api_host}/api-scf/scfFinanceProduct/insert'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "2",
            "Authorization": token_scf_platform
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        ProductId = r_json['datas']
        print(f'流程步骤: 【平台方】新增金融产品,返回金融产品ProductId:{ProductId}')
        print(f'请求参数: {payload}')
        print(f'接口响应为：{r_json}')
        self.g_d['ProductId'] = ProductId
        return ProductId

    def add_scfProjectBasis(self):
        """【平台方】新增项目,生成项目Id"""
        ProductId = self.add_scfFinanceProduct()
        payload = {
            "scfProjectBasisReq":
                {"id": "",
                 "bankId": "1547048461623263234",
                 "businessType": 2,
                 "enterpriseId": "1565528298128351233",
                 "name": "自动化项目" + get_number(6),
                 "open": False,
                 "refactor": False,
                 "scfFinanceProductId": ProductId,
                 "enter": False,
                 "grants": False,
                 "transfer": False,
                 "finance": True,
                 "isCoreGrant": True,
                 "bankName": "泛光灯",
                 "flowName": ["6"]},
            "scfProjectEnterReq":
                {"isTemplate": False,
                 "flowId": "",
                 "filePath": "",
                 "grantFlowItemId": "",
                 "link": "",
                 "scfProjectFlowEnterReq":
                     {"name": "",
                      "step": 0,
                      "flowItems": []}},
            "scfProjectGrantReq":
                {"isTemplate": False,
                 "flowId": "",
                 "isPush": False,
                 "useScope": 1,
                 "scfProjectFlowReq":
                     {"name": "",
                      "step": 0,
                      "flowItems": []}},
            "scfProjectFinanceReq":
                {"isTemplate": False,
                 "flowId": "",
                 "isHistory": True,
                 "isPush": True,
                 "pushMaterial": 0,
                 "serviceRate": 1,
                 "financeRate": 1,
                 "scfProjectFlowReq":
                     {"name": "自动化流程" + get_number(6),
                      "step": 1,
                      "flowItems":
                          [{"customerType": "11",
                            "isExternal": False,
                            "reportId": "", "isPush": False,
                            "isProtocol": False, "subs": [],
                            "customerTypeName": "平台方"}]}},
            "scfProjectRefactorReq":
                {"flowId": "",
                 "isTemplate": False,
                 "isHistory": False,
                 "isPush": False,
                 "pushMaterial": 0,
                 "serviceRate": 0,
                 "financeRate": 0,
                 "scfProjectFlowReq": {"name": "", "step": 0, "flowItems": []}}}
        url = f'{api_host}/api-scf/scfProjectBasis/insertAllDetail'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "2",
            "Authorization": token_scf_platform
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        projectId = r_json['datas']
        print(f'流程步骤: 【平台方】新增项目,返回项目projectId:{projectId}')
        print(f'请求参数: {payload}')
        print(f'接口响应为：{r_json}')
        self.g_d['projectId'] = projectId
        return projectId

    def allot_deliver(self):
        """【平台方】项目分配给供应商"""
        projectId = self.add_scfProjectBasis()
        url = f'{api_host}/api-scf/scfProjectBasis/deliver'
        payload = {
            "basisId": projectId,
            "enterpriseId": "1565532746930135041"
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_platform
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        print(f'流程步骤: 【平台方】项目分配给供应商')
        print(f'请求参数: {payload}')
        print(f'接口响应为：{r_json}')
        return r_json

    def by_projectId(self):
        """【供应商】根据项目Id绑定银行卡"""
        self.allot_deliver()
        projectId = self.g_d['projectId']
        url = f'{api_host}/api-scf/backAccount/bindByProjectId'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_supplier
        }
        payload = {
            "id": "1575006661570007042",
            "projectId": projectId}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        print(f'流程步骤: 【供应商】根据项目Id绑定银行卡')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        return r_json

    def open_credentials(self):
        """【核心企业】金点信开立"""
        self.g_d["goldenLetterCoden_nwe"] = "JDX20" + get_number(9)
        payload = {
            "goldenLetterCode": self.g_d["goldenLetterCoden_nwe"],
            "bills": [
                "1575028102419984386"
            ],
            "coreEntId": "1565528298128351233",
            "coreEntName": "接口自动化核心企业账号",
            "founderEnt": "接口自动化核心企业账号",
            "founderEntId": "1565528298128351233",
            "recipient": "自动化供应商企业名称",
            "recipientId": "1565532746930135041",
            "goldenLetterOpenDate": "2022-09-28T07:41:59.410Z",
            "goldenLetterEndDate": "2023-10-31T07:41:48.897Z",
            "promisedPaymentDate": "2023-09-30T07:41:53.796Z",
            "totalIssuerQuota": 2006250947,
            "usedQuota": 153272365,
            "goldenLetterMoney": 1000,
            "remainingAvailableQuota": 1852977582,
            "statementNumber": "91440300279446850J",
            "invoiceWithTax": 1000,
            "invoiceAmountProportion": "100%",
            "remainingOpenableInvoice": 0
        }
        r = api_goldenLetter_open_insert(token_scf_enterprise, payload)
        r_json = r.json()
        print(f'流程步骤: 【核心企业】金点信开立')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        return self.g_d["goldenLetterCoden_nwe"]

    def audit_credentials(self):
        "【核心企业】金点信开立审核"
        goldenLetterCoden_nwe = self.open_credentials()
        payload = {
            "auditStatus": 1,
            "founderEnt": "",
            "goldenLetterCode": goldenLetterCoden_nwe,
            "num": 1,
            "recipient": "",
            "size": 10
        }
        r = api_goldenLetter_open_queryPage(token_scf_enterprise, payload)
        r_json = r.json()

        payload = {
            "coreEntId": "1565528298128351233",
            "auditEntId": "1565528298128351233",
            "auditFlowItemId": "1575028590750216193",
            "auditOpinion": "",
            "auditStatus": 3,
            "creditEnhancerId": 0,
            "settlementId": "",
            "settlementName": "",
            "entId": "1565528298128351233",
            "id": r_json["datas"][0]["id"],
            "recipientId": "1565532746930135041"
        }

        r = api_goldenLetter_open_updateAuditStatus(token_scf_enterprise, payload)
        r_json = r.json()
        print(f'流程步骤: 【核心企业】金点信开立审核')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        return goldenLetterCoden_nwe

    def open_financing(self):
        goldenLetterCoden_nwe = self.audit_credentials()
        url = f'{api_host}/api-scf/financialFactoring/insert'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_supplier
        }
        payload = {
            "bankAccountNo": "4587006089066",
            "estimatedDisbursementDate": "2022-10-31T06:13:57.363Z",
            "financeEntId": "1565532904946343937",
            "financeEntName": "接口自动化保理商账号",
            "financingAmount": 1000,
            "financingRate": 0.1,
            "financingRemainAmount": 0,
            "financingServiceCharge": "1.00",
            "financingTerm": 365,
            "goldenLetterCode": goldenLetterCoden_nwe,
            "platformServiceCharge": "1.00",
            "platformServiceRate": 0.1,
            "projectId": "1575367552681390082",
            "currentHolder": "自动化供应商企业名称",
            "founderEnt": "接口自动化核心企业账号",
            "goldenLetterEndDate": "2023-10-31T07:41:48.897",
            "goldenLetterMoney": 1000,
            "goldenLetterOpenDate": "2022-09-28T07:41:59.41",
            "initialHolder": "自动化供应商企业名称",
            "promisedPaymentDate": "2023-09-30T07:41:53.796"
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        print(f'流程步骤: 【供应商】保理融资')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        return goldenLetterCoden_nwe

    def audit_financing(self):
        """融资审核"""
        goldenLetterCoden_nwe = self.open_financing()
        url = f'{api_host}/api-scf/financialFactoring/queryFinancialFactoringPage'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_platform
        }
        payload = {
            "goldenLetterCode": goldenLetterCoden_nwe,
            "currentHolder": "",
            "founderEnt": "",
            "paymentStatus": "",
            "num": 1,
            "size": 10
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        """流程步骤: 【供应商】查询金点信列表"""


        url = f'{api_host}/api-scf/goldenLetter/queryPage'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_supplier
        }
        payload = {
            "goldenLetterCode": goldenLetterCoden_nwe,
            "currentHolder": "",
            "founderEnt": "",
            "paymentStatus": "",
            "num": 1,
            "size": 10
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        rr_json = r.json()

        url = f'{api_host}/api-scf/financialFactoring/queryByApplicationNumber'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_supplier
        }
        payload = {"financeApplicationNumber": r_json["datas"][0]["financeApplicationNumber"]}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        rrr_json = r.json()

        url = f'{api_host}/api-scf/financialFactoring/updateAuditStatus'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_platform
        }

        payload = {
            "coreEntId": "1565528298128351233",
            "auditEntId": "1544610594103889922",
            "auditFlowItemId": rrr_json["datas"]["auditFlowItemId"],
            "auditStatus": 3,
            "creditEnhancerId": 0,
            "entId": "1565528298128351233",
            "id": r_json["datas"][0]["id"],
            "recipientId": "1565532746930135041",
            "financeEntId": "1565532904946343937",
            "goldenLetterId": rr_json["datas"][0]["id"]
        }

        r = requests.post(url, headers=headers, data=json.dumps(payload))
        rs_json = r.json()
        print(f'流程步骤: 【平台方】保理融资审核')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{rs_json}')
        self.g_d["id_one"] = r_json["datas"][0]["id"]
        return self.g_d["id_one"]

    def break_financing(self):
        id_one = self.audit_financing()
        url = f'{api_host}/api-scf/financialFactoring/financialSeal'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "1",
            "Authorization": token_scf_platform
        }

        payload = {
            "auditStatus": 3,
            "id": id_one
        }

        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        print(f'流程步骤: 【平台方】保理融资审核拆分金点信')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        self.g_d["goldenLetterCode"] = r_json["datas"][0]["goldenLetterCode"]
        return self.g_d["goldenLetterCode"]


if __name__ == '__main__':
    s = Bus_orderLoan()
    b = s.break_financing()
    print(b)

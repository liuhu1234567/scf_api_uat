from common.get_token import *
from common.do_faker import *
from common.do_config import api_host
from functools import wraps
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

class bus_orderLoan():
    def __init__(self):
        self.g_d = {}

    def add_scfFinanceProduct(self):
        """【平台方】新增金融产品，生成金融产品Id"""
        payload = {"name":"自动化金融产品" + get_number(6),
                   "financeId":"1547048461623263234",
                   "amountMin":1,
                   "amountMax":1000,
                   "rateMin":0,
                   "rateMax":5,
                   "loop":True,
                   "single":True,
                   "pay":True,
                   "repaymentType":1,
                   "availableBegin":"2022-09-27 19:32:43",
                   "availableEnd":"2033-09-25 19:32:50",
                   "loanBegin":"2022-09-27 19:33:02",
                   "loanEnd":"2031-09-28 19:33:09"}
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
            "id":"1575006661570007042",
            "projectId": projectId}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r_json = r.json()
        print(f'流程步骤: 【供应商】根据项目Id绑定银行卡')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r_json}')
        return r_json


if __name__ == '__main__':
    s = bus_orderLoan()
    b = s.out()
    g_d = s.g_d
    print(b)
    print(g_d)
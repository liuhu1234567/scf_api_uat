from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest


def api_template_findTemplates(token, payload):
    """【平台方】查询模板"""
    url = f'{api_host}/api-scf/template/findTemplates'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "x-appid-header": "1",
        "Authorization": token
    }
    r = requests.post(url, headers=headers, data=payload)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


class TemplateFindTemplates(unittest.TestCase):
    def test_template_findTemplates(self):
        """【平台方】查询模板"""
        contact = get_name()
        entName = get_company()
        contactMobile = get_phone()
        contactEmail = get_email()
        creditCode = get_number(10)
        payload = {
            "createBy": 0,
            "createTime": "",
            "id": 0,
            "num": 1,
            "size": 20,
            "templateCode": "",
            "templateGroup": "",
            "templateName": "",
            "templateUrl": "",
            "updateBy": 0,
            "updateTime": ""
        }
        r = api_template_findTemplates(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now


        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

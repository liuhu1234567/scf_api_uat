from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name
from case_api.supplier.role_insert import api_role_insert
import requests
import unittest
import json


def api_role_update(token, payload):
    """【供应商/经销商】编辑角色"""
    url = f'{api_host}/api-scf/role/update'
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


class RoleUpdate(unittest.TestCase):
    def test_role_update(self):
        """【供应商/经销商】编辑角色"""
        rolename = get_name()
        descnum = get_number(10)
        payload_one = {
            "roleName": f"{rolename}",
            "roleDesc": f"{descnum}"
        }
        roleid = api_role_insert(token_scf_supplier, payload_one).json()["resp_msg"]
        payload = {
            "id": roleid,
            "roleName": f"修改后的{rolename}",
            "roleDesc": f"修改后的{descnum}"
        }
        r = api_role_update(token_scf_supplier, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

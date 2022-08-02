from common.do_config import api_host, restime
from common.get_token import token_scf_platform
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email ,get_sfz
import requests
import unittest
import json

def api_user_tree_insertInfo(token, payload):
    """【平台方】新增树形结构,文件"""
    url = f'{api_host}/api-scf/tree/insertInfo'
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

def api_user_auth_tree_queryTree(token, payload):
    """【平台方】查询菜单树"""
    url = f'{api_host}/api-scf/tree/queryTree'
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

def api_user_query_tree_queryTreeFileInfoRespList(token, payload):
    """【平台方】查询树形菜单叶子节点数据"""
    url = f'{api_host}/api-scf/tree/queryTreeFileInfoRespList'
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

class User(unittest.TestCase):
    def test_001_tree_insertInfo(self):
        """【平台方】新增树形结构,文件"""
        rolename = get_name()
        descnum = get_number(10)
        sfz = get_sfz()
        email = get_email()
        payload = {
              "beOmit": True,
              "contentType": "",
              "entId": 0,
              "isImg": True,
              "name": "",
              "path": "",
              "size": 0,
              "source": "",
              "treeId": 0,
              "url": ""
            }
        r = api_user_tree_insertInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

    def test_002_user_auth_user_role(self):
        """【平台方】查询菜单树"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "type": 1
        }
        r = api_user_auth_tree_queryTree(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)


    def test_003_user_query_tree_queryTreeFileInfoRespList(self):
        """【平台方】查询树形菜单叶子节点数据"""
        rolename = get_name()
        descnum = get_number(10)
        payload = {
            "entId": 1,
            "treeIdList": ['1']
        }
        r = api_user_query_tree_queryTreeFileInfoRespList(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

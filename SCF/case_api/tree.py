from common.do_config import api_host, restime
from common.get_token import token_scf_platform,token_scf_supplier,token_scf_financier,token_scf_factor,token_scf_subsidiaries,token_scf_enterprise
from common.global_variable import customize_dict
from common.do_faker import get_number
import requests
import unittest
import json


def api_tree_insertInfo(token, payload):
    """【平台方】新增树形结构,文件"""
    url = f'{api_host}/api-scf/tree/insertInfo'
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


def api_tree_queryTreeData(token, payload):
    """【平台方】查询菜单树及数据"""
    url = f'{api_host}/api-scf/tree/queryTreeData'
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


def api_tree_dropdownList(token):
    """【平台方】菜单分类枚举信息"""
    url = f'{api_host}/api-scf/tree/dropdownList'
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


def api_tree_imageByType(token, payload):
    """【平台方】指定类型获取影像文件"""
    url = f'{api_host}/api-scf/tree/imageByType'
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


def api_tree_imageByTypes(token, payload):
    """【平台方】指定类型获取影像文件-批量"""
    url = f'{api_host}/api-scf/tree/imagesByTypes'
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


def api_tree_deleteInfo(token, payload):
    """【平台方】删除"""
    url = f'{api_host}/api-scf/tree/deleteInfo'
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


class Tree(unittest.TestCase):
    def test_001_tree_insertInfo(self):
        """【平台方】新增树形结构,文件"""
        payload = {
            "beOmit": True,
            "contentType": "",
            "entId": 0,
            "goldenLetterId": 0,
            "isImg": True,
            "name": "头像.png",
            "orderNo": "",
            "path": f"path{get_number(6)}",
            "size": 0,
            "source": "",
            "treeId": 1,
            "url": f"url{get_number(6)}"
        }
        r = api_tree_insertInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_002_tree_queryTreeData(self):
        """【平台方】查询菜单树"""
        payload = {
            "entId": 0,
            "goldenLetterId": 0,
            "orderNo": "",
            "type": 0
        }
        r = api_tree_queryTreeData(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_003_tree_dropdownList(self):
        """【平台方】菜单分类枚举信息"""
        r = api_tree_dropdownList(token_scf_platform)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    # def test_004_tree_imageByType(self):
    #     """【平台方】指定类型获取影像文件"""
    #     payload = {
    #         "id": 0
    #     }
    #     r = api_tree_imageByType(token_scf_platform, payload)
    #     r_json = r.json()
    #     restime_now = r.elapsed.total_seconds()
    #     customize_dict['restime_now'] = restime_now
    #     self.assertEqual(200, r_json['resp_code'])
    #     self.assertEqual('SUCCESS', r_json['resp_msg'])
    #     self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_005_tree_imageByTypes(self):
        """【平台方】指定类型获取影像文件-批量"""
        payload = {
            "ids": []
        }
        r = api_tree_imageByTypes(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

    def test_006_tree_deleteInfo(self):
        """【平台方】删除"""
        payload = {
            "beOmit": True,
            "id": 0
        }
        r = api_tree_deleteInfo(token_scf_platform, payload)
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now
        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime, 'Test api timeout')

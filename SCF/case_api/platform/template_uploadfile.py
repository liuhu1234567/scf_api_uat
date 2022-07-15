from common.do_config import api_host, restime
from common.get_token import token_scf_supplier
from common.global_variable import customize_dict
from common.do_faker import get_number, get_name, get_company, get_phone, get_email
import requests
import unittest
from config.all_path import get_file_path



def api_template_uploadfile(token, file_name):
    """【平台方】上传文件"""
    url = f'{api_host}/api-scf/template/upload/file'
    headers = {
        "Content-Type": "application/json",
        "x-appid-header": "1",
        "Authorization": token
    }
    png_path = get_file_path(file_name)
    with open(png_path, 'rb') as f:
        file_b = f.read()
    files = {
        'uploadFile': (file_name, file_b)
    }
    r = requests.request("POST", url, headers=headers, files=files)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'接口响应为：{r.text}')
    return r


class TemplateUploadfile(unittest.TestCase):
    def test_template_uploadfile(self):
        """【平台方】上传文件"""
        r = api_template_uploadfile(token_scf_supplier, 'test.png')
        r_json = r.json()
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(200, r_json['resp_code'])
        self.assertEqual('SUCCESS', r_json['resp_msg'])
        self.assertLessEqual(restime_now, restime)

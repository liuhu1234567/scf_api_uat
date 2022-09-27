from common.get_token import *
from common.do_config import api_host
import json
import requests

def api_scfFinanceProduct_insert( payload):
    def wrapper():
        """【平台方】新增金融产品"""
        url = f'{api_host}/api-scf/scfFinanceProduct/insert'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "x-appid-header": "2",
            "Authorization": token_scf_supplier
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f'请求地址：{url}')
        print(f'请求头：{headers}')
        print(f'请求参数：{payload}')
        print(f'接口响应为：{r.text}')
        return r

if __name__ == '__main__':
    print('1')
    t = token_scf_supplier
    # print(t)
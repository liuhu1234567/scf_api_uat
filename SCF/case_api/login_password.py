import unittest
import requests
import json
from common.do_config import api_host, restime
from common.global_variable import customize_dict
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


# def encrypt(password):
#     """AES加密"""
#     # key为16的倍数
#     key = "6578904783439suw"
#     # 加密字符串长同样需要16倍数
#     aes = AES.new(key.encode(), AES.MODE_ECB)
#     padding_text = pad(password.encode(), AES.block_size, style='pkcs7')
#     encrypted_text = aes.encrypt(padding_text)
#     r = base64.b64encode(encrypted_text).decode()
#     return r


def encrypt(pwd):
    """RSA加密"""
    public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKSItqTh99pxpM9iRuqtFy/f81g3hTXCdGMPjWGgMTziNMxK60BmzOqw24bjXQQ+pgKQhSsPhxT4QsgaG0QbDE8CAwEAAQ=="
    key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    encrypt_text = cipher.encrypt(pwd.encode())
    r = base64.b64encode(encrypt_text).decode()
    return r


def api_login_password(payload):
    """用户名密码登录"""
    url = 'https://uat-gateway.dianliantech.com/api-uaa/login/password'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'请求地址：{url}')
    print(f'请求头：{headers}')
    print(f'请求参数：{payload}')
    print(f'接口响应为：{r.text}')
    return r


class LoginPassword(unittest.TestCase):

    def test_login_password(self):
        """账号正确，密码正确"""
        password = encrypt("Ss123456")
        # payload = {
        #     "username": "ZVXS17585245519",
        #     "password": password,
        #     "code": 1234,
        #     "remember": True,
        #     "grant_type": "password",
        #     "clientId": "webApp",
        #     "clientSecret": "webApp",
        #     "type": 1
        # }
        payload = {
            "username": "ML4W17585245519",
            "password": password,
            "code": "是",
            "grant_type": "password",
            "clientId": "webApp",
            "clientSecret": "webApp",
            "key": "",
            "type": 1}
        r = api_login_password(payload)
        r_json = r.json()
        print(r_json)
        restime_now = r.elapsed.total_seconds()
        customize_dict['restime_now'] = restime_now

        self.assertEqual(r_json['resp_code'], 200)
        self.assertEqual(r_json['resp_msg'], "SUCCESS")
        self.assertLessEqual(restime_now, restime, 'Test api timeout')


if __name__ == '__main__':
    unittest.main()
    # print(encrypt('Aa1234567'))

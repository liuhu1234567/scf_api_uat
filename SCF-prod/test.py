import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
import uuid
import requests
import json


def encrypt(pwd):
    """RSA加密"""
    public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKSItqTh99pxpM9iRuqtFy/f81g3hTXCdGMPjWGgMTziNMxK60BmzOqw24bjXQQ+pgKQhSsPhxT4QsgaG0QbDE8CAwEAAQ=="
    key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    encrypt_text = cipher.encrypt(pwd.encode())
    r = base64.b64encode(encrypt_text).decode()
    return r

if __name__ == '__main__':
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    password = encrypt("Aa12345678")
    payload = {
        "username": "dlkjBa00008",
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    url = 'https://gateway.dianliantech.com/api-uaa/login/password'
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    r = r.json()
    print(r)
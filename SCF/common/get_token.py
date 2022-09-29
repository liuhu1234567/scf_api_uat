from case_api.login_password import api_login_password, encrypt
from common.do_config import scf_financier, scf_enterprise, scf_supplier, scf_platform, scf_factor, scf_subsidiaries
import uuid

def get_scf_financier():
    """获取资金方账号token"""
    password = encrypt(scf_financier['password'])
    data = {
        "username": scf_financier['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    print(r_json)
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token


def get_scf_enterprise():
    """获取核心企业账号token"""
    password = encrypt(scf_enterprise['password'])
    data = {
        "username": scf_enterprise['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token


def get_scf_supplier():
    """获取供应商/经销商账号token"""
    password = encrypt(scf_supplier['password'])
    data = {
        "username": scf_supplier['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token


def get_scf_platform():
    """获取平台方账号token"""
    password = encrypt(scf_platform['password'])
    data = {
        "username": scf_platform['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token


def get_scf_subsidiaries():
    """获取核企子公司账号token"""
    password = encrypt(scf_subsidiaries['password'])
    data = {
        "username": scf_subsidiaries['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token


def get_scf_factor():
    """获取保理商账号token"""
    password = encrypt(scf_factor['password'])
    data = {
        "username": scf_factor['username'],
        "password": password,
        "code": "ths9tgwwlx",
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "key": str(uuid.uuid4()),
        "type": 1}
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    # token = {'token_type': r_json['datas']['token_type'], 'access_token': r_json['datas']['access_token']}
    return token

token_scf_financier = get_scf_financier()
token_scf_enterprise = get_scf_enterprise()
token_scf_supplier = get_scf_supplier()
token_scf_platform = get_scf_platform()
token_scf_factor = get_scf_factor()
token_scf_subsidiaries = get_scf_subsidiaries()

if __name__ == '__main__':
    # print(token_scf_financier)
    # print(token_scf_enterprise)
    print(token_scf_supplier)
    # print(token_scf_platform)
    # print(token_scf_factor)
    # print(token_scf_subsidiaries)

from case_api.login_password import api_login_password, encrypt
from common.do_config import scf_financier, scf_enterprise, scf_supplier, scf_platform,scf_supplier_Receive


def get_scf_financier():
    """获取资金方账号token"""
    password = encrypt(scf_financier['password'])
    data = {
        "username": scf_financier['username'],
        "password": password,
        "code": 1234,
        "remember": True,
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "type": 1
    }
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    return token


def get_scf_enterprise():
    """获取核心企业/核心子公司账号token"""
    password = encrypt(scf_enterprise['password'])
    data = {
        "username": scf_enterprise['username'],
        "password": password,
        "code": 1234,
        "remember": True,
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "type": 1
    }
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    return token


def get_scf_supplier():
    """获取供应商/经销商账号token"""
    password = encrypt(scf_supplier['password'])
    data = {
        "username": scf_supplier['username'],
        "password": password,
        "code": 1234,
        "remember": True,
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "type": 1
    }
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    return token


def get_scf_platform():
    """获取平台方账号token"""
    password = encrypt(scf_platform['password'])
    data = {
        "username": scf_platform['username'],
        "password": password,
        "code": 1234,
        "remember": True,
        "grant_type": "password",
        "clientId": "webApp",
        "clientSecret": "webApp",
        "type": 1
    }
    r_json = api_login_password(data).json()
    token = f"{r_json['datas']['token_type']} {r_json['datas']['access_token']}"
    return token


token_scf_financier = get_scf_financier()
token_scf_enterprise = get_scf_enterprise()
token_scf_supplier = get_scf_supplier()
token_scf_platform = get_scf_platform()

if __name__ == '__main__':
    print(token_scf_financier)
    print(token_scf_enterprise)
    print(token_scf_supplier)
    print(token_scf_platform)

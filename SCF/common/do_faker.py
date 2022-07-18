from faker import Faker
import random
import string

fake = Faker('zh_cn')


def get_sfz():
    """获取随机身份证"""
    return fake.ssn()


def get_number(n):
    """获取指定位数的随机数"""
    l = string.digits
    r = random.sample(l, n)
    return ''.join(r)


def get_phone():
    """获取随机手机号"""
    return fake.phone_number()


def get_entCode(n):
    """获取指定位数的随机小写字母"""
    l = string.ascii_lowercase
    r = random.sample(l, n)
    return ''.join(r)


def get_email():
    """获取随机邮箱"""
    return fake.email()


def get_name():
    """获取随机姓名"""
    return fake.name()


def get_license():
    return fake.license_plate()


def get_company():
    return fake.company()


def get_card_number():
    """获取随机信用卡号"""
    return fake.credit_card_number(card_type=None)


def get_date():
    return fake.date(pattern="%Y-%m-%d")


def get_url():
    """获取随机url"""
    return fake.url()


if __name__ == '__main__':
    r = get_card_number()
    print(r)
    print(type(r))

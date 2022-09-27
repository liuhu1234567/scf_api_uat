import random
import datetime
import time
from case_api.login_password import encrypt
from faker import Faker
from jsonpath import jsonpath
import json
# fake = Faker('zh_cn')
# def get_company():
#     """获取随机公司名称"""
#     return fake.company()
#
# li = []
# for i in range(10000):
#     c = fake.word() + fake.word() + fake.company()
#     # c = fake.company() + fake.pystr()
#     li.append(c)
#
# sum = 0
# li2 = []
# for j in li:
#     if li.count(j) > 1 and j not in li2:
#         li2.append(j)
#         sum += 1
# print(sum)
# print(li)
# # c = fake.company_suffix()
# # print(c)
#
# def get_company():
#     a = "0123456789"
#     b = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     str_list = [random.choice(a + b) for i in range(6)]
#     random_str = ''.join(str_list)
#     return random_str + fake.company()
# start = datetime.datetime.now()
# time.sleep(1)
# now = datetime.datetime.now()
# e = (now - start).total_seconds()
#
# s = str(now)
# print(type(e))
# print('%.2f'%e)
print(encrypt('Aa1234567'))
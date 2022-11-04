from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''准入申请'''


class Access(Home):
    input1_element = (By.XPATH, "//input[@value='1']")  # 企业名称搜索框
    input2_element = (By.XPATH, "//input[@value='2']")  # 金融产品名称搜索框
    input3_element = (By.XPATH, "//input[@value='3']")  # 金融机构名称搜索框
    input4_element = (By.XPATH, "//span[contains(.,'全部')]")  # 状态搜索框
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 状态下拉框数据
    preview_element = (By.XPATH, "//span[contains(.,'预览')]")  # 预览
    return_element = (By.XPATH, "//span[contains(.,'返回')]")  # 返回

    def input1_input(self):
        print('已分配客户名称搜索框')
        self.send_keys(self.input1_element, 1)

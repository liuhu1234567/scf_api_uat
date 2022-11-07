from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''融资客户列表'''


class CustomerAudit(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 已分配客户名称搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 项目名称搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 金融产品名称搜索框
    input4_element = (By.XPATH, "//span[contains(.,'全部')]")  # 状态搜索框
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 状态下拉框数据

    def input1_input(self):
        print('已分配客户名称搜索框')
        self.send_keys(self.input1_element, 1)

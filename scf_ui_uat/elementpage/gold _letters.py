from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''金点信列表'''


class GoldLetters(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 金点信编号搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 开立人搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 当前持单人搜索框
    input4_element = (By.ID, "rc_select_36")  # 兑付状态
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 兑付状态下拉框
    preview_element = (By.XPATH, "//li[contains(.,'详情')]")  # 详情
    trace_element = (By.XPATH, "//li[contains(.,'追溯')]")  # 追溯
    trace_preview_element = (By.XPATH, "//span[contains(.,'返 回')]")  # 返回

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)

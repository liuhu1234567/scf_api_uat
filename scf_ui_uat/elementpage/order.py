from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''订单融资'''


class Order(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 订单编号搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 订单名称搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 买方企业名称搜索框
    input4_element = (By.XPATH, "//span[contains(.,'全部')]")  # 审核状态
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 审核状态下拉框
    preview_element = (By.XPATH, "//span[contains(.,'预览')]")  # 预览
    preview_return_element = (By.XPATH, "//button[contains(.,'返 回')]")  # 返回
    import_element = (By.XPATH, "//span[contains(.,'导 入')]")  # 导入
    upload_element = (By.XPATH, "//span[contains(.,'导 入')]")  # 上传文件
    import_confirm_element = (By.XPATH, "//span[contains(.,'确 定')]")  # 确认
    download_element = (By.XPATH, "//span[contains(.,'下 载')]")  # 下载
    download_template_element = (By.XPATH, "//span[contains(.,'下载模板')]")  # 下载模板

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)

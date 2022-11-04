from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''产品列表'''


class Product(Home):
    product_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[3]/div')  # 金融产品管理_平台
    product_list_element = (
        By.LINK_TEXT, '产品列表')  # 产品列表
    product_add_element = (
        By.CSS_SELECTOR, '[class="ant-dl-default-btn ant-dl-default-btn-default ProductList--button--ZScxjL1"]')  # 产品新增
    name_element = (By.ID, 'name')  # 产品名称
    financeId_element = (By.ID, 'financeId')  # 金融机构名称
    content_element = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div')  # 金融机构名称下拉框数据
    amountMin_element = (By.ID, 'amountMin')
    amountMax_element = (By.ID, 'amountMax')
    rateMin_element = (By.ID, 'rateMin')
    rateMax_element = (By.ID, 'rateMax')
    loop_element = (By.ID, 'loop')
    content_one_element = (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    content_two_element = (By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    content_three_element = (By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    content_four_element = (By.XPATH, '/html/body/div[8]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    single_element = (By.ID, 'single')
    selection_element = (By.ID, 'pay')
    repaymentType_element = (By.ID, 'repaymentType')
    ue2ldsD_element = (By.CSS_SELECTOR, "li:nth-child(2) > .Add--tableHeaderOperateIcon--ue2ldsD")
    available_element = (By.ID, 'available')
    day_element = (
        By.CSS_SELECTOR,
        "tr:nth-child(4) > .ant-dl-default-picker-cell:nth-child(4) > .ant-dl-default-picker-cell-inner")
    time_element = (By.CSS_SELECTOR, ".ant-dl-default-btn-primary > span")
    day_one_element = (
        By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[4]/div')
    time_one_element = (By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div[2]/ul/li/button/span')
    loan_element = (By.ID, 'loan')
    liimg_element = (By.XPATH, '//li/img')  # 返回
    change_element = (By.XPATH, "//span[contains(.,'修改')]")  # 修改
    disable_element = (By.XPATH, "//span[contains(.,'禁用')]")  # 禁用
    delete_element = (By.XPATH, "//span[contains(.,'删除')]")  # 删除
    preview_element = (By.XPATH, "//span[contains(.,'预览')]")  # 预览
    determine_element = (By.XPATH, "//span[contains(.,'确定')]")  # 确定
    input1_element = (By.XPATH, '//input')  # 金融产品名称搜索
    input2_element = (By.XPATH, '//li[2]/input')  # 金融产品名称搜索
    input3_element = (By.XPATH, "//span[contains(.,'全部')]")  # 状态搜索
    input4_element = (By.XPATH, '//div[2]/div/div/div/div[2]/div')  # 状态搜索>启用
    input5_element = (By.XPATH, '//div/div/div[3]/div')  # 状态搜索>启用





    def product_add_clike(self):
        print('点击产品新增')
        self.clike(self.product_add_element)

    def name_input(self, name):
        print('输入产品名称')
        self.send_keys(self.name_element, name)

    def financeId_input(self):
        print('下拉选择金融机构名称')
        self.clike(self.financeId_element)
        self.clike(self.content_element)

    def amountMin_input(self, name):
        print('填写额度区间')
        self.send_keys(self.amountMin_element, name)

    def amountMax_input(self, name):
        print('填写额度区间')
        self.send_keys(self.amountMax_element, name)

    def rateMin_input(self, name):
        print('填写利率区间')
        self.send_keys(self.rateMin_element, name)

    def rateMax_input(self, name):
        print('填写利率区间')
        self.send_keys(self.rateMax_element, name)

    def loop_input(self):
        print('下拉选择是否循环额度')
        self.clike(self.loop_element)
        self.clike(self.content_one_element)

    def single_input(self):
        print('下拉选择是否单笔额度')
        self.clike(self.single_element)
        self.clike(self.content_two_element)

    def selection_input(self):
        print('下拉选择是否受托支付')
        self.clike(self.selection_element)
        self.clike(self.content_three_element)

    def repaymentType_input(self):
        print('下拉选择是否受托支付')
        self.clike(self.repaymentType_element)
        self.clike(self.content_four_element)

    def ue2ldsD_input(self):
        print('点击提交')
        self.clike(self.ue2ldsD_element)

    def available_input(self):
        print('输入产品有效期')
        self.clike(self.available_element)
        self.clike(self.day_element)
        self.clike(self.time_element)
        self.clike(self.day_element)
        self.clike(self.time_element)

    def loan_input(self):
        print('输入贷款期限')
        self.clike(self.loan_element)
        self.clike(self.day_one_element)
        self.clike(self.time_one_element)
        self.clike(self.day_one_element)
        self.clike(self.time_one_element)

# name = 'ui自动化产品名称' + get_number(6)
# Product_name = 'ui自动化金融机构名称' + get_number(6)
# obj = Product()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.product_clike()
# obj.product_list_clike()
# obj.product_add_clike()
# obj.name_input(name)
# obj.financeId_input()
# obj.amountMin_input('0.1')
# obj.amountMax_input('0.2')
# obj.rateMin_input('1')
# obj.rateMax_input('10')
# obj.loop_input()
# obj.single_input()
# obj.selection_input()
# obj.repaymentType_input()
# obj.available_input()
# obj.loan_input()
# obj.ue2ldsD_input()

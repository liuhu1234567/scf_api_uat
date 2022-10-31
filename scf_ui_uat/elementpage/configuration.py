from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number


class Configuration(Home):
    project_add_element = (By.LINK_TEXT, '+新增')
    project_name_element = (By.ID, 'name')
    enterpriseId_element = (By.ID, 'enterpriseId')
    enterpriseId_one_element = (
        By.CSS_SELECTOR, '.ant-dl-default-select-item-option-active > .ant-dl-default-select-item-option-content')
    businessType_element = (By.ID, 'businessType')
    businessType_one_element = (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]/div')
    scfFinanceProductId_element = (By.ID, 'scfFinanceProductId')
    scfFinanceProductId_one_element = (By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    value_element = (By.XPATH, '// input[ @ value = "6"]')
    isCoreGrant_element = (By.ID, 'isCoreGrant')
    isCoreGrant_one_element = (By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    page_element = (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/form/a')
    create_element = (By.XPATH, '//*[@id="rc-tabs-0-panel-6"]/div/form/div[2]/div[2]/button/span')
    process_element = (By.CSS_SELECTOR, '.ant-dl-default-col-7 #name')
    number_element = (By.ID, 'step')
    number_one_element = (By.XPATH, '/html/body/div[9]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    customerType0_element = (By.ID, 'customerType0')
    customerType0_one_element = (By.XPATH, "/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[7]/div")
    cconfirm_element = (By.XPATH, "//span[contains(.,'确 定')]")
    isPush_element = (By.ID, 'isPush')
    isPush_one_element = (By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]')
    isHistory_element = (By.ID, 'isHistory')
    isHistory_oen_element = (By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div[1]/div/div/div[1]')
    pushMaterial_element = (By.ID, 'pushMaterial')
    pushMaterial_oen_element = (By.XPATH, '/html/body/div[12]/div/div/div/div[2]/div[1]/div/div/div[1]/div')
    financeRate_element = (By.ID, 'financeRate')
    serviceRate_element = (By.ID, 'serviceRate')
    submit_element = (By.LINK_TEXT, '提交')
    distribution_element = (By.XPATH,
                            '//*[@id="ice-container"]/div/section/div/main/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[9]/ul/li[1]/span')
    customer_element = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/ul/li/div/div/span[2]')
    customer_one_element = (By.CSS_SELECTOR, '.ant-dl-default-select-item-option-content')
    determine_element = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/button[2]')

    def project_add_clike(self):
        print('新增项目配置')
        self.clike(self.project_add_element)

    def project_name_clike(self, name):
        print('新增项目名称')
        self.send_keys(self.project_name_element, name)

    def enterpriseId_clike(self):
        print('填写核心企业')
        self.clike(self.enterpriseId_element)
        self.clike(self.enterpriseId_one_element)

    def businessType_clike(self):
        print('填写业务类型')
        self.clike(self.businessType_element)
        self.clike(self.businessType_one_element)

    def scfFinanceProductId_clike(self):
        print('填写金融产品名称')
        self.clike(self.scfFinanceProductId_element)
        self.clike(self.scfFinanceProductId_one_element)

    def value_clike(self):
        print('勾选需配置的流程')
        self.clike(self.value_element)

    def isCoreGrant_clike(self):
        print('填写是否占用核心企业授信额度')
        self.clike(self.isCoreGrant_element)
        self.clike(self.isCoreGrant_one_element)

    def page_clike(self):
        print('点击下一页')
        self.clike(self.page_element)

    def create_clike(self):
        print('点击创建流程')
        self.clike(self.create_element)

    def process_clike(self, name):
        print('输入流程名称')
        self.send_keys(self.process_element, name)

    def number_clike(self):
        print('填写节点数')
        self.clike(self.number_element)
        self.clike(self.number_one_element)

    def customerType0_clike(self):
        print('填写节点名称“平台方”')
        self.clike(self.customerType0_element)
        self.get_script(self.customerType0_one_element)
        sleep(0.5)
        self.clike(self.customerType0_one_element)

    def cconfirm_clike(self):
        print('填写节点确认')
        self.clike(self.cconfirm_element)

    def isPush_clike(self):
        print('是否推送申请人主体信息材料')
        self.clike(self.isPush_element)
        self.clike(self.isPush_one_element)

    def isHistory_clike(self):
        print('是否推送历史转让材料')
        self.clike(self.isHistory_element)
        self.clike(self.isHistory_oen_element)

    def pushMaterial_clike(self):
        print('需推送的节点材料')
        self.clike(self.pushMaterial_element)
        self.clike(self.pushMaterial_oen_element)

    def financeRat_input(self):
        print('融资费率')
        self.send_keys(self.financeRate_element, '0.1')

    def serviceRate_input(self):
        print('平台服务费率')
        self.send_keys(self.serviceRate_element, '0.1')

    def submit_clike(self):
        print('点击提交')
        self.clike(self.submit_element)

    def distribution_clike(self):
        print('点击分配')
        self.clike(self.distribution_element)

    def customer_input(self):
        print('填写融资客户名称')
        self.clike(self.customer_element)
        self.clike(self.customer_one_element)

    def determine_clike(self):
        print('点击确认')
        self.clike(self.determine_element)

# project_name = 'ui自动化项目名称' + get_number(6)
# process_name = 'ui自动化流程名称' + get_number(6)
# obj = Configuration()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.configuration_clike()
# obj.project_clike()
# obj.project_add_clike()
# obj.project_name_clike(project_name)
# obj.enterpriseId_clike()
# obj.businessType_clike()
# obj.scfFinanceProductId_clike()
# obj.isCoreGrant_clike()
# obj.value_clike()
# obj.page_clike()
# obj.create_clike()
# obj.process_clike(process_name)
# obj.number_clike()
# obj.customerType0_clike()
# obj.cconfirm_clike()
# obj.isPush_clike()
# obj.isHistory_clike()
# obj.pushMaterial_clike()
# obj.financeRat_input()
# obj.serviceRate_input()
# obj.submit_clike()

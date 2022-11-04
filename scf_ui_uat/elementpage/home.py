from elementpage.loginPage import loginPage
from common.do_selenium import *
from selenium.webdriver.common.by import By


class Home(loginPage):
    product_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[3]/div')  # 金融产品管理_平台
    product_list_element = (
        By.LINK_TEXT, '产品列表')
    iframe_element = (By.ID, 'main-content')
    enterprise_element = (
    By.CSS_SELECTOR, '.ant-dl-default-menu-submenu-open > .ant-dl-default-menu-submenu-title')  # 企业中心_平台
    archives_element = (By.LINK_TEXT, '企业档案')
    certification_element = (By.LINK_TEXT, '企业认证')
    bank_element = (By.LINK_TEXT, '银行账户管理')
    configuration_element = (By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[10]/div')  # 配置管理_核心企业
    project_element = (By.LINK_TEXT, '产品配置')
    customer_element = (
    By.XPATH, "//div[@id='ice-container']/div/section/aside/div/div[2]/ul/li[2]/div/span/span/span")  # 客户管理_平台
    customer_list_element = (By.LINK_TEXT, '客户列表')
    customer_review_element = (By.LINK_TEXT, '客户审批')
    production_element = (By.LINK_TEXT, '产品申请')
    product_supplier_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[2]/div/span/span/span')  # 客户管理-供应商
    gold_element = (By.LINK_TEXT, '金点信配置')
    table_element = (By.LINK_TEXT, '数据表配置')
    field_element = (By.LINK_TEXT, '全量字段表模板')
    management_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[9]/div/span/span/span')  # 数据管理_平台
    procurement_element = (By.LINK_TEXT, '采购数据')
    Financial_element = (By.LINK_TEXT, '财务数据')
    system_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[11]/div/span/span/span')  # 系统管理_平台
    user_element = (By.LINK_TEXT, '用户管理')
    role_element = (By.LINK_TEXT, '角色管理')
    credit_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[5]/div/span/span/span')  # 授信管理_平台
    apply_for_element = (By.LINK_TEXT, '授信申请')
    review_element = (By.LINK_TEXT, '授信审批')
    results_element = (By.LINK_TEXT, '授信结果')
    lines_element = (By.LINK_TEXT, '额度管理')
    lines_credit_element = (By.LINK_TEXT, '额度审批')
    access_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[4]/div/span/span/span')  # 准入管理_平台
    access_apply_element = (By.LINK_TEXT, '准入申请')
    access_review_element = (By.LINK_TEXT, '准入审批')

    def iframe_add(self):
        self.get_iframe(self.iframe_element)

    def product_clike(self):
        print('点击金融产品管理')
        self.clike(self.product_element)

    def product_supplier_clike(self):
        print('点击金融产品管理_供应商')
        self.clike(self.product_supplier_element)

    def product_list_clike(self):
        print('点击产品列表')
        self.clike(self.product_list_element)

    def archives_clike(self):
        print('企业档案')
        self.clike(self.archives_element)

    def certification_clike(self):
        print('企业认证')
        self.clike(self.certification_element)

    def bank_clike(self):
        print('银行账户管理')
        self.clike(self.bank_element)

    def enterprise_clike(self):
        print('企业中心')
        self.clike(self.enterprise_element)

    def configuration_clike(self):
        print('配置管理')
        self.clike(self.configuration_element)

    def project_clike(self):
        print('项目配置')
        self.clike(self.project_element)

    def customer_clike(self):
        print('客户管理')
        self.clike(self.customer_element)

    def customer_list_clike(self):
        print('客户列表')
        self.clike(self.customer_list_element)

    def customer_review_clike(self):
        print('客户审批')
        self.clike(self.customer_review_element)

    def production_clike(self):
        print('产品申请')
        self.clike(self.production_element)

    def gold_clike(self):
        print('金点信配置')
        self.clike(self.gold_element)

    def table_clike(self):
        print('数据表配置')
        self.clike(self.table_element)

    def field_clike(self):
        print('全量字段表模板')
        self.clike(self.field_element)

    def management_clike(self):
        print('数据管理')
        self.clike(self.management_element)

    def procurement_clike(self):
        print('采购数据')
        self.clike(self.procurement_element)

# obj = Home()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.customer_clike()
# obj.customer_list_clike()
# obj.customer_clike()
# obj.customer_review_clike()
# obj.product_clike()
# obj.product_list_clike()

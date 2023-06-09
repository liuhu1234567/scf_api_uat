from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''数据表配置'''


class DataTable(Home):
    table_add_element = (By.LINK_TEXT, '+新增')  # 新增按钮
    table_name_element = (By.ID, 'name')  # 数据表名称
    data_type_element = (By.ID, 'type')  # 数据类型
    value_type_element = (
        By.CSS_SELECTOR,
        '.ant-dl-default-select-item-option-active > .ant-dl-default-select-item-option-content')  # 数据类型下拉数据
    customer_type_element = (
        By.XPATH,
        '//*[@id="ice-container"]/div/section/div/main/div/div/form/div[2]/div[1]/div/div[2]/div/div/div/div/div')  # 可查看客户类型
    customer_value_element = (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div')  # 可查看客户类型下拉数据
    templateId_element = (By.ID, 'templateId')  # 数据表模板
    templateId_value_element = (By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div')  # 数据表模板下拉数据
    itemId_element = (By.ID, 'itemId')  # 所属项目
    itemId_value_element = (By.XPATH, '/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[1]/div')  # 所属项目下拉数据
    according_element = (
        By.XPATH,
        './/*[@id="ice-container"]/div/section/div/main/div/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[2]/td[3]/button')  # 是否显示
    confirm_table_element = (
        By.CSS_SELECTOR, 'li:nth-child(2) > .addDataTable--tableHeaderOperateIcon--uwHxNVO')  # 确认
    return_data_element = (By.XPATH, 'li:nth-child(1) > .addDataTable--tableHeaderOperateIcon--uwHxNVO')  # 返回
    view_element = (By.XPATH, "//span[contains(.,'查看')]")  # 列表数据查看
    change_element = (By.XPATH, "//span[contains(.,'修改')]")  # 列表数据修改

    def table_add_clike(self):
        print('新增数据表配置')
        self.clike(self.table_add_element)

    def table_name_input(self, name):
        print('数据表名称')
        self.send_keys(self.table_name_element, name)

    def value_type_clike(self):
        print('数据类型')
        self.clike(self.data_type_element)
        # self.get_text(self.data_type_element)
        self.clike(self.value_type_element)

    def customer_type_clike(self):
        print('可查看客户类型')
        self.clike(self.customer_type_element)
        self.clike(self.customer_value_element)

    def templateId_clike(self):
        print('数据表模板')
        self.clike(self.templateId_element)
        self.clike(self.templateId_value_element)

    def itemId_clike(self):
        print('所属项目')
        self.clike(self.itemId_element)
        self.clike(self.itemId_value_element)

    def according_clike(self):
        print('是否显示')
        self.clike(self.according_element)

    def confirm_table_clike(self):
        print('确认')
        self.clike(self.confirm_table_element)

# table_name = 'ui自动化数据表名称' + get_number(6)
# obj = DataTable()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.configuration_clike()
# obj.table_clike()
# obj.table_add_clike()
# obj.table_name_input(table_name)
# obj.value_type_clike()
# obj.customer_type_clike()
# obj.templateId_clike()
# obj.itemId_clike()
# obj.according_clike()
# obj.confirm_table_clike()

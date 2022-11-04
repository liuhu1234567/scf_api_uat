from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number
from config.all_path import get_file_path

'''采购数据'''


class TableProcurement(Home):
    contains_element = (By.XPATH, "//span[contains(.,'批量导入')]")  # 导入文件
    upload_element = (By.CSS_SELECTOR, '.Import--icon--B50GKYx')  # 上传文件
    table_determine_element = (
        By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/button')  # 确认
    management_element = (
        By.XPATH, '//*[@id="ice-container"]/div/section/aside/div/div[2]/ul/li[9]/div/span/span/span')  # 数据管理_平台
    procurement_element = (By.LINK_TEXT, '采购数据')  # 采购数据
    new_element = (By.XPATH, "//button[contains(.,'新增')]")  # 新增
    new_new_element = (By.XPATH, "//span/div/span")  # 新增>新增
    new_return_element = (By.XPATH, "//div/span[2]")  # 新增>返回
    editor_element = (By.LINK_TEXT, "编辑")  # 修改
    save_element = (By.LINK_TEXT, "保存")  # 保存
    cancel_element = (By.LINK_TEXT, "取消")  # 取消
    editor_determine_element = (By.XPATH, "//span[contains(.,'确 定')]")  # 取消>确定
    delete_element = (By.LINK_TEXT, "删除")  # 删除
    download_element = (By.XPATH, "//button[contains(.,'下 载')]")  # 下载
    input_element = (By.XPATH, "//input")  # 借款企业名称搜索框

    def contains_clike(self):
        print('点击批量上传')
        self.clike(self.contains_element)

    def upload_clike(self):
        print('点击上传文件')
        self.clike(self.upload_element)

    def table_determine_input(self):
        print('点击确认')
        self.clike(self.table_determine_element)

# png_path = get_file_path('caigou.xlsx')
# table_name = 'ui自动化数据表名称' + get_number(6)
# obj = TableProcurement()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.management_clike()
# obj.procurement_clike()
# obj.contains_clike()
# obj.upload_clike()
# obj.uploadWinFile(png_path)
# obj.table_determine_input()

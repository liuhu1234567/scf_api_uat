from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''授信结果'''


class Lines(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 授信申请人名称搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 授信方名称搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 金融产品名称搜索框
    preview_element = (By.XPATH, "//li[contains(.,'详情')]")  # 详情
    delete_element = (By.XPATH, "//li[contains(.,'删除')]")  # 删除
    credit_return_element = (By.XPATH, "//span[contains(.,'返 回')]")  # 返回
    credit_add_element = (By.XPATH, '//div/div/div/ul/li')  # 新增
    add_return_element = (By.XPATH, "//span[contains(.,'返 回')]")  # 返回
    add_confirm_element = (By.XPATH, "//span[contains(.,'确 认')]")  # 确认
    creditApplyName_element = (By.ID, "creditApplyName")  # 授信申请人名称
    creditApplyName1_element = (By.XPATH, "//div[7]/div/div/div/div[2]/div/div/div/div")  # 授信申请人名称下拉框
    creditType_element = (By.ID, "creditType")  # 授信类型
    creditType1_element = (By.XPATH, "//div[8]/div/div/div/div[2]/div/div/div/div/div")  # 授信类型下拉框
    creditCardIdType_element = (By.ID, "creditCardIdType")  # 授信申请人证件类型
    creditCardIdType1_element = (By.XPATH, "//div[9]/div/div/div/div[2]/div/div/div/div/div")  # 授信申请人证件类型下拉框
    projectName_element = (By.ID, "projectName")  # 项目名称
    projectName1_element = (By.XPATH, "//div[11]/div/div/div/div[2]/div/div/div/div/div")  # 项目名称下拉框
    auditAmount_element = (By.ID, "auditAmount")  # 批复额度
    loanRatio_element = (By.ID, "loanRatio")  # 贷款利率
    coinType_element = (By.ID, "coinType")  # 币种
    coinType1_element = (By.XPATH, "//div[12]/div/div/div/div[2]/div/div/div/div/div")  # 币种下拉框
    loanBegin_element = (By.ID, "loanBegin")  # 额度开始日 额度到期日
    loanEnd_element = (By.ID, "loanEnd")  # 额度到期日
    loanBegin1_element = (By.LINK_TEXT, "今天")  # 额度到期日
    bankAccountName_element = (By.ID, "bankAccountName")  # 还款账户名称
    bankAccountNo_element = (By.ID, "bankAccountNo")  # 还款账户账号
    bbankAccountSite_element = (By.ID, "bankAccountSite")  # 还款账户账开户行名称

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)

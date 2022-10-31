from common.do_selenium import *
from selenium import webdriver



driver = webdriver.Chrome('/SCF-test/scf_api_uat/config/chromedriver.exe')
driver.get("http://www.baidu.com")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from common.do_path import get_abspath
from time import sleep
from selenium.webdriver import ActionChains


class BasePage(object):
    sleep_time = 0.5

    def __init__(self):
        print(get_abspath('files', 'chromedriver.exe'))
        print('初始化driver设置')
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置防止被检测为selenium
        self.driver = webdriver.Chrome(service=Service(get_abspath('config', 'chromedriver.exe')), chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open(self, url):
        print(f'打开：{url}')
        self.driver.get(url)
        sleep(self.sleep_time)

    def send_keys(self, element, text):
        print(f'向{element}元素输入：{text}')
        self.driver.find_element(element[0], element[1]).send_keys(text)
        sleep(self.sleep_time)

    def clike(self, element):
        print(f'点击{element}元素')
        self.driver.find_element(element[0], element[1]).click()
        sleep(self.sleep_time)

    def exit(self):
        print('退出浏览器')
        self.driver.close()
        self.driver.quit()

    def save_img(self):
        sleep(1)
        base64 = self.driver.get_screenshot_as_base64()
        print(f'<img src="data:image/png;base64, {base64}" width="1000px">')

    def get_text(self, element):
        print(f'获取{element}元素中的文本')
        text = self.driver.find_element(element[0], element[1]).text
        return text

    def get_attribute(self, element, name):
        print(f'获取{element}元素的{name}属性')
        value = self.driver.find_element(element[0], element[1]).get_attribute(name)
        return value

    def get_url(self):
        return self.driver.current_url

    def execute_script(self, js, *args):
        print(f'执行js：{js}，参数：{args}')
        r = self.driver.execute_script(js, *args)
        return r

    def action_login(self, element, xoffset):
        print(f'拖动{element}元素，{xoffset}')
        source = self.driver.find_element(element[0], element[1])
        action = ActionChains(self.driver)
        action.click_and_hold(source)
        action.move_by_offset(xoffset, 0)
        action.pause(1)
        action.release()
        action.perform()
        sleep(self.sleep_time)

    def test(self):
        self.driver.find_element().screenshot_as_png()
        self.driver.find_element().screenshot_as_base64()
        self.driver.get_screenshot_as_base64()
        self.driver.get_screenshot_as_png()
        self.driver.get_screenshot_as_file()
        self.driver.save_screenshot()

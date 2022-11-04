from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import pyautogui
import logger
from common.do_path import get_abspath
from time import sleep
from selenium.webdriver import ActionChains


class BasePage(object):
    sleep_time = 0.5

    def __init__(self):
        print(get_abspath('files', 'chromedriver.exe'))
        print('初始化driver设置')
        option = webdriver.ChromeOptions()
        option.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })  # 初始化Chrome的时候，不弹出密码框
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置防止被检测为selenium
        self.driver = webdriver.Chrome(service=Service(get_abspath('config', 'chromedriver.exe')),
                                       options=option)
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

    def select(self, element, value):
        print(f'下拉框选择{element}元素')
        Select(self.driver.find_element(element[0], element[1])).select_by_value(value)
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

    def get_iframe(self, element):
        print(f'进入{element}元素中的iframe框')
        self.driver.switch_to.frame(self.driver.find_element(element[0], element[1]))
        sleep(self.sleep_time)

    def get_parent_frame(self):
        print(f'退出进入iframe框')
        self.driver.switch_to.default_content()
        sleep(self.sleep_time)

    def get_script(self, element):
        print(f'滚动到所定位的目标处{element}')
        target = self.driver.find_element(element[0], element[1])
        self.driver.execute_script('arguments[0].scrollIntoView()', target)

    def uploadWinFile(self, filepath):
        '''
        通过Windows系统上传文件
        '''
        try:
            pyautogui.write(filepath)  # 输入文件绝对路径
            sleep(2)
            pyautogui.press('enter', 2)  # 按2次回车键（按2次是为了防止出错）
        except Exception as e:
            logger.logger.error(e)
            e.args = ('上传文件操作异常',)
            raise e
        else:
            return filepath

    def wait_element_visibility(self, element, timeout=15, poll=0.3, extra_wait=None):
        """
        等待元素可见(浏览器窗口显示范围内)
        :param extra_wait: 智能等待结束后的额外等待时间/秒
        :param element: 元素定位信息
        :param timeout: 超时时间
        :param poll: 轮询间隔时间/秒
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll).until(ec.element_to_be_clickable(element))
            if extra_wait:
                sleep(extra_wait)
            print(f"{element}可见")
            return True
        except Exception as e:
            print(f"{element}不可见.{e}")
            return False

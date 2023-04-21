from abc import abstractmethod
import platform
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from helper_class.handle_event_helper import HandleEnventHelper
from helper_class.remote_api_helper import RemoteAPIHelper
from core_class.captcha_solver import CaptchaSolver


class ChromeDriverBase():
    def __init__(self) -> None:
        op = webdriver.ChromeOptions()
        # op.add_argument("--incognito")
        op.add_argument("--start-maximized")
        op.add_argument("----user-data-dir=/home/huythanh0x/.config/google-chrome/Default")
        if "Linux" in platform.platform():
            self.driver = webdriver.Chrome(
                executable_path="/usr/bin/chromedriver", options=op)
        elif "macOS" in platform.platform():
            self.driver = webdriver.Chrome(
                executable_path="/usr/local/bin/chromedriver", options=op)
        self.handle_event_helper = HandleEnventHelper(self.driver)
        self.captcha_solver = CaptchaSolver(self.driver)
        self.remote_api_helper = RemoteAPIHelper(self.driver)
        
    def browser_is_active(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def is_page_source_contains_text(self, text):
        return text in str(self.driver.page_source)

    def openUrl(self, URL):
        self.driver.get(URL)

    def close_browser(self):
        self.driver.quit()
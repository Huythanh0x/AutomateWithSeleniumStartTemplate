from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TIMEOUT = 30


class HandleEnventHelper():
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def execute_element_by_tag(self, type, value, input_text=None):
        sleep(0.5)
        element = self.wait_for_presence(type, value)
        self.move_cursor_and_click(element, input_text)
        sleep(0.5)

    def wait_for_presence(self, type, value, time_out=TIMEOUT):
        element_present = EC.presence_of_element_located((type, value))
        return WebDriverWait(self.driver, time_out).until(element_present)

    def execute_element_by_attribute(self, attribute_name, attribute_value, input_text=None):
        sleep(0.5)
        element_xpath = f'//*[@{attribute_name}="{attribute_value}"]'
        element = self.wait_for_presence(By.XPATH, element_xpath)
        self.move_cursor_and_click(element,input_text)
        sleep(0.5)

    def move_cursor_and_click(self,element, input_text=None):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.click(element)
        action.perform()
        if input_text != None:
            element.send_keys(input_text)

    def execute_element_have_text(self, tag_name, text_value: str, input_text=None):
        sleep(0.5)
        for element in self.driver.find_elements(By.TAG_NAME, tag_name):
            if text_value  in element.text:
                action = webdriver.ActionChains(self.driver)
                action.move_to_element(element)
                action.click(element)
                action.perform()
                if input_text != None:
                    element.send_keys(input_text)
                break
        sleep(0.5)
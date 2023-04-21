from time import sleep
import os
import cv2
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from helper_class.handle_event_helper import HandleEnventHelper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
TIME_FOR_LOADING_CAPTCHA = 600
TIME_FOR_SOLVING_CAPTCHA = 3000


class CaptchaSolver():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.handle_event_helper = HandleEnventHelper(self.driver)
        self.waiting_time = 0
        
    def bypass_login_captcha(self):
        self.waiting_for_loading_login_captcha()
        start_solving_time = int(time.time()*10)
        while self.was_login_captcha_not_solved() and int(time.time()*10) - start_solving_time < TIME_FOR_SOLVING_CAPTCHA:
            try:
                if self.is_page_source_contains_text("Verify failed"):
                    self.driver.refresh()
                self.solve_captcha(is_login=True)
            except:
                pass
        if int(time.time()*10) - start_solving_time >= TIME_FOR_SOLVING_CAPTCHA:
            raise Exception("TOO LONG TO SOLVE CAPTCHA")

    def was_login_captcha_not_solved(self):
        try:
            self.driver.find_element(
                By.CLASS_NAME, value="Mui-disabled")
            return True
        except:
            return False

    def waiting_for_loading_login_captcha(self):
        count_second = 0
        while "https://necaptcha.nosdn" not in str(self.driver.page_source):
            sleep(0.1)
            count_second += 1
            if count_second > TIME_FOR_LOADING_CAPTCHA:
                break
            elif count_second >= TIME_FOR_LOADING_CAPTCHA // 3 and (int(count_second) - TIME_FOR_LOADING_CAPTCHA//3) % TIME_FOR_LOADING_CAPTCHA//2/3 == 0:
                self.driver.refresh()
            if self.is_page_source_contains_text("Load failed"):
                self.driver.refresh()
        if count_second > TIME_FOR_LOADING_CAPTCHA:
            return False
        return True

    def solve_captcha(self, is_login=True):
        os.system("mkdir -p captcha_images")
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, 'yidun_bg-img'))
        WebDriverWait(self.driver, 30).until(element_present)
        tp_element = self.driver.find_element(
            by=By.CLASS_NAME, value='yidun_bg-img')
        bg_element = self.driver.find_element(
            by=By.CLASS_NAME, value='yidun_jigsaw')
        bg_url = str(bg_element.get_attribute('src'))
        tp_url = str(tp_element.get_attribute('src'))
        os.system(
            f"curl -sS {bg_url} > captcha_images/bg_img.png & curl -sS {tp_url} > captcha_images/tp_img.png")
        bg_img = cv2.imread('captcha_images/bg_img.png')
        tp_img = cv2.imread('captcha_images/tp_img.png')
        x = self.get_captcha_drag_position(bg_img, tp_img)
        os.system("rm -rf captcha_images")
        try:
            self.drag_captcha(x, is_login)
        except:
            pass

    def get_captcha_drag_position(self, bg_img, tp_img):
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(res)
        x, _ = max_loc
        return x

    def drag_captcha(self, x, is_login):
        if is_login:
            x += 11
        else:
            x = x*7/10
        control_element = self.driver.find_element(
            By.XPATH, value='//*[@id="captcha"]/div/div[2]/div[2]/span')
        webdriver.ActionChains(self.driver).click_and_hold(
            control_element).move_by_offset(x, 0).release().perform()

    def is_page_source_contains_text(self, text):
        return text in str(self.driver.page_source)

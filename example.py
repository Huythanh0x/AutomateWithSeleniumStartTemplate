from base_class.chrome_driver_base import ChromeDriverBase
from selenium.webdriver.common.by import By
import time

class ExampleDriver(ChromeDriverBase):
    pass

def sample_with_attribute():
    driver.openUrl(skill_share_login_url)
    driver.handle_event_helper.execute_element_by_attribute("name", "email", "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_attribute("type", "button")

def sample_with_class_name():
    driver.openUrl(skill_share_login_url)
    driver.handle_event_helper.execute_element_by_tag(By.CLASS_NAME, "login-inputs-fields", "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_tag(By.CLASS_NAME, "submit-btn")


def sample_with_x_path():
    driver.openUrl(skill_share_login_url)
    driver.handle_event_helper.execute_element_by_tag(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/form/div[2]/input', "sample@gmail.com")
    driver.handle_event_helper.execute_element_by_tag(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/form/button[4]')


def sample_with_pure_text():
    driver.openUrl(skill_share_login_url)
    time.sleep(5)
    #Have to set a fixed wait time. And the input field have no text content at all
    driver.handle_event_helper.execute_element_have_text("input", 'Email address', "sample@gmail.com")
    driver.handle_event_helper.execute_element_have_text("button", 'Sign In')

def sample_step_by_step():
    driver.openUrl(skill_share_login_url)
    element = driver.handle_event_helper.wait_for_presence(By.CLASS_NAME, "submit-btn")
    driver.handle_event_helper.move_cursor_and_click(element)

def sample_fetch_api():
    api_url = "https://api.usercentrics.eu/translations/translations-en.json"
    json_result =  driver.remote_api_helper.loadJsonFromURL(api_url)
    print(json_result)

skill_share_login_url = "https://www.skillshare.com/en/login"
driver =  ExampleDriver()
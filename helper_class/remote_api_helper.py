from helper_class.handle_event_helper import HandleEnventHelper
import json
from selenium.webdriver.common.by import By


class RemoteAPIHelper():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.handle_event_helper = HandleEnventHelper(self.driver)

    def loadJsonFromURL(self, apiURL):
        self.driver.get(apiURL)
        return json.loads(
            self.driver.find_element(By.TAG_NAME, "pre").text)        
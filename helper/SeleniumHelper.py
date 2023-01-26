from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver

    def open_login_url(self, login_url):
        self.driver.get(login_url)

    def wait_till_element_present(self, locator, timeout=10):
        flag = False
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            flag = True
        except Exception as e:
            print(f"Exception occurred while checking for element presence: {e}")
        return flag

    def insert_text_in_input_field(self, locator, input_text):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)

    def verify_element_displayed(self, locator):
        is_displayed = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).is_displayed()
        return is_displayed

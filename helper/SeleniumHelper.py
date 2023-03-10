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

    def wait_browser_to_load_completely(self, timeout=30):
        self.driver.implicitly_wait(timeout)

    def click_on_element(self, locator):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()

    def is_element_enabled(self, locator):
        element = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
        return element.is_enabled()

    def clear_input_field(self, locator):
        text = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).clear()
        return text

    def get_element_text(self, locator):
        text = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).text
        return text

    def insert_text_in_input_field(self, locator, input_text):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)

    def verify_element_displayed(self, locator):
        is_displayed = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).is_displayed()
        return is_displayed

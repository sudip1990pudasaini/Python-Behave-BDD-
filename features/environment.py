from webdriver import webdriver
from helper.SeleniumHelper import SeleniumHelper

login_url = "https://qa-test.avenuecode.io/tasks"


def before_scenario(context, scenario):
    context.driver = webdriver.get_chrome_webdriver()
    context.driver.maximize_window()
    SeleniumHelper(context.driver).open_login_url(login_url)


def after_scenario(context, scenario):
    context.driver.close()

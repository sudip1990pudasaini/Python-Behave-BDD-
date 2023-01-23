from behave import *
from selenium import webdriver
import time


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/sudippudasaini/Drivers/chromedriver_mac_arm64/chromedriver")


@when(u'landed on main page')
def open_main_page(context):
    context.driver.get("https://avenuecode.com")


@then('verify that logo is present')
def verify_logo(context):
    status = context.driver.find_element("xpath", "//*[@id='navbar']/div/div[1]/div/div/a/img").is_displayed()
    assert status is True


time.sleep(5)


@then('nav bar is displayed')
def verify_nav_bar(context):
    nav_bar_displayed = context.driver.find_element("id", "menu-item-18296").is_displayed()
    assert nav_bar_displayed is True


@then('close browser')
def close_browser(context):
    context.driver.close()

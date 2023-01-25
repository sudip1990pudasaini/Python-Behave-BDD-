from behave import *
from selenium import webdriver
import time


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/sudippudasaini/Drivers/chromedriver_mac_arm64/chromedriver")


@when('landed on test login page')
def open_main_page(context):
    context.driver.get("https://qa-test.avenuecode.io/tasks")


@then('verify that login page is displayed')
def verify_todo_link(context):
    status = context.driver.find_element("xpath", "//*[@class='panel-heading']/h4").is_displayed()
    assert status is True


@then('nav bar is displayed')
def verify_nav_bar(context):
    nav_bar_displayed = context.driver.find_element("xpath", "//*[@class='navbar-brand']").is_displayed()
    assert nav_bar_displayed is True


@then('email field label is displayed')
def verify_email_label(context):
    email_label_displayed = context.driver.find_element("xpath", "//*[@for='user_email']").is_displayed()
    assert email_label_displayed is True


@then('email input field is displayed')
def verify_email_input(context):
    email_field_displayed = context.driver.find_element("id", "user_email").is_displayed()
    assert email_field_displayed is True


@then('password field label is displayed')
def verify_password_label(context):
    password_label_displayed = context.driver.find_element("xpath", "//*[@for='user_password']").is_displayed()
    assert password_label_displayed is True


@then('password input field is displayed')
def verify_password_input(context):
    password_input_displayed = context.driver.find_element("id", "user_password").is_displayed()
    assert password_input_displayed is True


@then('remember me checkbox is displayed')
def verify_remember_me(context):
    remember_me_displayed = context.driver.find_element("id", "user_remember_me").is_displayed()
    assert remember_me_displayed is True


@then('sign in button is displayed')
def verify_signin_button(context):
    signin_button_displayed = context.driver.find_element("xpath", "//*[@class='btn btn-primary' "
                                                                   "and @name='commit']").is_displayed()
    assert signin_button_displayed is True


time.sleep(10)


@then('close browser')
def close_browser(context):
    context.driver.close()

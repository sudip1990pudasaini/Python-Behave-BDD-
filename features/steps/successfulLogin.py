from behave import *
from selenium import webdriver
import time


@given('I launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/sudippudasaini/Drivers/chromedriver_mac_arm64/chromedriver")


@given('I am on the login page')
def open_login_page(context):
    context.driver.get("https://qa-test.avenuecode.io/tasks")
    time.sleep(10)
    login_page_opened = context.driver.find_element("id", "sign_in").is_displayed()
    assert login_page_opened is True


@when('I enter email "{email}" and password "{password}"')
def enter_email_password(context, email, password):
    context.driver.find_element("id", "user_email").send_keys(email)
    context.driver.find_element("id", "user_password").send_keys(password)


@when('I click on sign in button')
def click_sign_in(context):
    context.driver.find_element("xpath", "//*[@class='btn btn-primary' "
                                         "and @name='commit']").click()


time.sleep(5)


@then('I should be logged in successfully and message is "{message}" displayed')
def verify_success_message(context, message):
    success_msg_displayed = context.driver.find_element("xpath", "//*[@class='alert alert-info']").is_displayed()
    assert success_msg_displayed is True

    success_message = context.driver.find_element("xpath", "//*[@class='alert alert-info']").text
    assert success_message == message


@then('I should be landed on the my tasks page')
def verify_my_tasks_page(context):
    my_tasks_page_displayed = context.driver.find_element("id", "my_task").is_displayed()
    assert my_tasks_page_displayed is True


@then('title of the task page should be "{title}"')
def verify_title(context, title):
    tasks_page_title = context.driver.find_element("xpath", "//div/h1").text
    assert tasks_page_title == title
    # TODO [Bug: 1098 Tasks page title copy is incorrect] has to be fixed to pass this test
    # Remove this comment when bug is fixed

from behave import *
from selenium import webdriver
import time


@given('I launch the browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/sudippudasaini/Drivers/chromedriver_mac_arm64/chromedriver")


@given('login with "{email}" and password "{password}"')
def login(context, email, password):
    context.driver.get("https://qa-test.avenuecode.io/tasks")
    time.sleep(5)
    login_page_opened = context.driver.find_element("id", "sign_in").is_displayed()
    assert login_page_opened is True

    context.driver.find_element("id", "user_email").send_keys(email)
    context.driver.find_element("id", "user_password").send_keys(password)
    context.driver.find_element("xpath", "//*[@class='btn btn-primary' "
                                         "and @name='commit']").click()


@given('I land on my tasks page')
def verify_my_tasks_page(context):
    my_tasks_page_displayed = context.driver.find_element("id", "my_task").is_displayed()
    assert my_tasks_page_displayed is True


@given('tasks input field is displayed')
def verify_task_input_displayed(context):
    time.sleep(5)
    task_input_displayed = context.driver.find_element("id", "new_task").is_displayed()
    assert task_input_displayed is True


@given('create a task button is displayed')
def verify_add_button_displayed(context):
    add_button_displayed = context.driver.find_element(
        "xpath", "//*[@class='input-group-addon glyphicon glyphicon-plus']").is_displayed()
    assert add_button_displayed is True


@when('I type "{task_text}" in tasks input field')
def add_tasks(context, task_text):
    context.driver.find_element("id", "new_task").send_keys(task_text)


@when('click on the add button')
def click_add_button(context):
    context.driver.find_element("xpath", "//*[@class='input-group-addon glyphicon glyphicon-plus']").click()


@then('I should see the task getting added in the list')
def verify_task_added(context):
    context.driver.find_element("xpath", "//*[@class='table']/tbody/tr[1]/td[2]/a")


@then('I should not see the empty task getting added')
def verify_task_added(context):
    task_text = context.driver.find_element("xpath", "//*[@class='table']/tbody/tr[1]/td[2]/a").text
    assert task_text != "    "


@then('task of char length 254 should not get added')
def verify_task_added(context):
    task_text = context.driver.find_element("xpath", "//*[@class='table']/tbody/tr[1]/td[2]/a").text
    task_char_length = len(task_text)
    if task_char_length <= 250:
        assert True, "Test Passed"
    else:
        assert False, "Char limit exceeded, test failed!"

    # TODO [1101 Task is exceeding more than 250 Chars] should get passed once reported bug is fixed
    #   Remove the comment when it starts passing


@then('I should not see the task getting added with less than 3 characters')
def verify_task_added(context):
    task_text = context.driver.find_element("xpath", "//*[@class='table']/tbody/tr[1]/td[2]/a").text
    task_char_length = len(task_text)
    if task_char_length >= 250:
        assert True, "Test Passed"
    else:
        assert False, "Test Failed! Minimum 3 characters required to add task!"

    # TODO [1099 Minimum character validation is not implemented while creating tasks]
    #  should get passed once reported bug is fixed
    #  Remove the comment when it starts passing

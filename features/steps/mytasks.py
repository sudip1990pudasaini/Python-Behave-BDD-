from behave import *
from helper.SeleniumHelper import SeleniumHelper
from locators import login_page_locators
from locators import my_tasks_page_locators


@given('I am logged in with "{email}" and password "{password}"')
def login(context, email, password):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        login_page_locators.email_input_field, email)

    SeleniumHelper(context.driver).insert_text_in_input_field(
        login_page_locators.password_input_field, password)

    SeleniumHelper(context.driver).click_on_element(
        login_page_locators.sign_in_button)
    SeleniumHelper(context.driver).wait_till_element_present(my_tasks_page_locators.my_task_menu)


@then('title of the task page should be "{title}"')
def verify_title(context, title):
    tasks_page_title_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.title_message)
    title_copy = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.title_message)

    if tasks_page_title_displayed and title_copy == title:
        assert True, "Test passed"
    else:
        assert False, "Test Failed! Title did not match with the given copy"
    # TODO [Bug: 1098 Tasks page title copy is incorrect] has to be fixed to pass this test
    #   Remove this comment when bug is fixed


@given('I land on my tasks page')
def verify_my_tasks_page(context):
    my_tasks_page_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.my_task_menu)
    assert my_tasks_page_displayed is True


@given('tasks input field is displayed')
def verify_task_input_displayed(context):
    task_input_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.task_input_field)
    assert task_input_displayed is True


@given('create a task button is displayed')
def verify_add_button_displayed(context):
    add_button_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.add_task_button)
    assert add_button_displayed is True


@when('I type "{task_text}" in tasks input field')
def add_tasks(context, task_text):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        my_tasks_page_locators.task_input_field, task_text)


@when('click on the add button')
def click_add_button(context):
    SeleniumHelper(context.driver).click_on_element(
        my_tasks_page_locators.add_task_button)


@then('I should see the task getting added in the list')
def verify_task_added(context):
    row_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.added_task_in_table)


@then('I should not see the empty task getting added')
def verify_task_text(context):
    task_text = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.added_task_in_table)
    assert task_text != "    "


@then('task of char length 254 should not get added')
def verify_task_added(context):
    task_text = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.added_task_in_table)
    task_char_length = len(task_text)
    if task_char_length <= 250:
        assert True, "Test Passed"
    else:
        assert False, "Char limit exceeded, test failed!"

    # TODO [1101 Task is exceeding more than 250 Chars] should get passed once reported bug is fixed
    #   Remove the comment when it starts passing


@then('I should not see the task getting added with less than 3 characters')
def verify_task_added(context):
    task_text = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.added_task_in_table)
    task_char_length = len(task_text)
    if task_char_length >= 250:
        assert True, "Test Passed"
    else:
        assert False, "Test Failed! Minimum 3 characters required to add task!"

    # TODO [1099 Minimum character validation is not implemented while creating tasks]
    #  should get passed once reported bug is fixed
    #  Remove the comment when it starts passing

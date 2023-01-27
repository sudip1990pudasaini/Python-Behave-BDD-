from behave import *
from helper.SeleniumHelper import SeleniumHelper
from locators import my_tasks_page_locators
from locators import manage_subtasks_modal_locators
from time import sleep


@when('a task is added')
def verify_task_is_added(context):
    task_in_table = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.added_task_in_table)
    assert task_in_table is True


@then('I should see manage subtasks button')
def verify_manage_subtasks_button_displayed(context):
    button_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.first_task_manage_subtasks_button)
    assert button_displayed is True


@then('subtasks counter should be zero')
def verify_subtasks_counter(context):
    button_text_with_counter = "(0) Manage Subtasks"
    subtasks_text = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.first_task_manage_subtasks_button)

    assert subtasks_text == button_text_with_counter, "Subtasks count is not 0"


@when('I click on manage subtasks button')
def click_on_manage_subtasks_button(context):
    SeleniumHelper(context.driver).click_on_element(
        my_tasks_page_locators.first_task_manage_subtasks_button)
    sleep(5)


@then('it should open up the subtasks modal')
def verify_subtasks_modal_appears(context):
    modal_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        manage_subtasks_modal_locators.modal)
    assert modal_displayed is True


@then('modal has the edit subtask title')
def verify_title_displayed(context):
    title_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        manage_subtasks_modal_locators.modal_title)
    assert title_displayed is True


@then('task description should be read-only')
def verify_task_des_readonly(context):
    task_des_enabled = SeleniumHelper(context.driver).is_element_enabled(
        manage_subtasks_modal_locators.task_description
    )
    assert task_des_enabled is False, "Task description is not read-only"


@when('I click on add subtask button')
def click_on_add_subtasks_button(context):
    SeleniumHelper(context.driver).click_on_element(
        manage_subtasks_modal_locators.add_subtask_button)


@then('I should not see an empty subtask getting added')
def verify_empty_subtask(context):
    is_subtasks_table_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        manage_subtasks_modal_locators.table_title
    )
    assert is_subtasks_table_displayed is True

    is_subtask_content_empty = SeleniumHelper(context.driver).get_element_text(
        manage_subtasks_modal_locators.subtasks_table_first_row_content)
    if is_subtask_content_empty == "empty":
        assert False, "Test Failed! Should not have saved an empty subtask"
    else:
        assert True, "Test Passed!"


@when('I wipe out the default date value')
def clear_due_date(context):
    SeleniumHelper(context.driver).clear_input_field(
        manage_subtasks_modal_locators.subtask_due_date)


@when('enter "{date_value}" on due date field')
def clear_due_date(context, date_value):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        manage_subtasks_modal_locators.subtask_due_date, date_value)


@when('enter text "{subtask_text}" on subtask description')
def clear_due_date(context, subtask_text):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        manage_subtasks_modal_locators.subtask_description, subtask_text)


@then('I should see the subtask getting added')
def verify_subtask_added(context):
    is_subtasks_table_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        manage_subtasks_modal_locators.table_title
    )
    assert is_subtasks_table_displayed is True

    is_subtask_content_empty = SeleniumHelper(context.driver).get_element_text(
        manage_subtasks_modal_locators.subtasks_table_first_row_content)
    if is_subtask_content_empty != "empty":
        assert True, "Test Passed!"
    else:
        assert False, "Test Failed! Subtasks could not be added"


@when('I close the modal')
def close_modal(context):
    SeleniumHelper(context.driver).click_on_element(
        manage_subtasks_modal_locators.modal_close_button)
    SeleniumHelper(context.driver).wait_till_element_present(
        my_tasks_page_locators.first_task_manage_subtasks_button)


@then('I subtask counter "{count}" on manage subtask button should be increased')
def counter_on_manage_subtasks_button(context, count):
    button_text = SeleniumHelper(context.driver).get_element_text(
        my_tasks_page_locators.first_task_manage_subtasks_button)
    counter_value = [*button_text]
    subtask_count = int(counter_value[1])
    count = int(count)

    if subtask_count == count:
        assert True, f"Test Passed! counter has been increased : {subtask_count}"
    else:
        assert False, f"Test Failed! counter has not been increased to {subtask_count}"



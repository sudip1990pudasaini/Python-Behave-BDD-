from behave import *
from locators import login_page_locators
from locators import my_tasks_page_locators
from helper.SeleniumHelper import SeleniumHelper


@when('login page is displayed')
def verify_todo_link(context):
    SeleniumHelper(context.driver).wait_till_element_present(login_page_locators.nav_bar_todo)


@then('verify nav bar is displayed')
def verify_nav_bar(context):
    nav_bar_displayed = SeleniumHelper(context.driver).verify_element_displayed(login_page_locators.nav_bar)
    assert nav_bar_displayed is True


@then('verify email field label is displayed')
def verify_email_label(context):
    email_label_displayed = SeleniumHelper(context.driver).verify_element_displayed(login_page_locators.email_label)
    assert email_label_displayed is True


@then('verify email input field is displayed')
def verify_email_input(context):
    email_field_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        login_page_locators.email_input_field
    )
    assert email_field_displayed is True


@then('verify password field label is displayed')
def verify_password_label(context):
    password_label_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        login_page_locators.password_label
    )
    assert password_label_displayed is True


@then('verify password input field is displayed')
def verify_password_input(context):
    password_input_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        login_page_locators.password_input_field
    )
    assert password_input_displayed is True


@then('verify remember me checkbox is displayed')
def verify_remember_me(context):
    remember_me_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        login_page_locators.remember_me
    )
    assert remember_me_displayed is True


@then('verify sign in button is displayed')
def verify_signin_button(context):
    signin_button_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        login_page_locators.sign_in_button
    )
    assert signin_button_displayed is True


@given('login page is displayed')
def login_page(context):
    SeleniumHelper(context.driver).wait_till_element_present(login_page_locators.nav_bar_todo)


@when('I enter valid email "{email}"')
def enter_email(context, email):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        login_page_locators.email_input_field, email
    )


@when('I enter valid password "{password}"')
def enter_password(context, password):
    SeleniumHelper(context.driver).insert_text_in_input_field(
        login_page_locators.password_input_field, password
    )


@when('I click on sign in button')
def click_sign_in(context):
    SeleniumHelper(context.driver).click_on_element(login_page_locators.sign_in_button)
    SeleniumHelper(context.driver).wait_browser_to_load_completely()


@then('I should be logged in successfully and message is "{message}" displayed')
def verify_success_message(context, message):
    success_msg_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.successful_login_msg
    )
    if success_msg_displayed:
        message_copy = SeleniumHelper(context.driver).get_element_text(
            my_tasks_page_locators.successful_login_msg)
        assert message_copy == message, "Test passed"
    else:
        assert False, "Test Failed! Could not find success message."


@then('I should be landed on the my tasks page')
def verify_my_tasks_page(context):
    my_tasks_page_displayed = SeleniumHelper(context.driver).verify_element_displayed(
        my_tasks_page_locators.my_task_menu
    )
    assert my_tasks_page_displayed is True

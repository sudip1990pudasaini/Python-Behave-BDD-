from behave import *
from locators import login_page_locators
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

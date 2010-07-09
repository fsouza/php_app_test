# -*- coding: utf-8 -*-
from lettuce import *

@step(u'Given that is a user registered in the system with the username "admin" and the password "123"')
def given_that_is_a_user_registered_in_the_system_with_the_username_group1_and_the_password_group2(step):
    pass

@step(u'When I navigate to the login page')
def when_i_navigate_to_the_login_page(step):
    login_url = world.root_url + 'login.php'
    world.browser.get(login_url)

@step(u'And I fill the username field with (.*)')
def and_i_fill_the_username_field_with_login(step, login):
    username_field = world.browser.find_element_by_xpath('//input[@name="username"]')
    username_field.send_keys(login)

@step(u'And I fill the password field with <password>')
def and_i_fill_the_password_field_with_password(step, password):
    password_field = world.browser.find_element_by_xpath('//input[@name="password"]')
    password_field.send_keys(password)

@step(u'And I click the "(.*)" button')
def and_i_click_the_group1_button(step, button_value):
    button = world.browser.find_element_by_xpath('//input[@value="%s"]' %(button_value))
    button.click()

@step(u'Then I see the message <message>')
def then_i_see_the_message_message(step, message):
    assert message in world.browser.get_page_source()

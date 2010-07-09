# -*- coding: utf-8 -*-
from lettuce import *

@step(u'Given that there is a user registered in the system with the username "admin" and the password "123"')
def do_nothing(step):
    '''There is nothing that Lettuce can do to guarantee this sentence'''
    pass

@step(u'When I navigate to the login page')
def when_i_navigate_to_the_login_page(step):
    login_url = world.root_url + 'login.html'
    world.browser.get(login_url)

@step(u'And fill the username field with (.*)')
def and_i_fill_the_username_field_with_login(step, login):
    username_field = world.browser.find_element_by_xpath('//input[@name="username"]')
    username_field.send_keys(login)

@step(u'And fill the password field with (.*)')
def and_i_fill_the_password_field_with_password(step, password):
    password_field = world.browser.find_element_by_xpath('//input[@name="password"]')
    password_field.send_keys(password)

@step(u'And click the "(.*)" button')
def and_i_click_the_group1_button(step, button_value):
    button = world.browser.find_element_by_xpath('//input[@value="%s"]' %(button_value))
    button.click()

@step(u'Then I see the message (.*)')
def then_i_see_the_message_message(step, message):
    assert message in world.browser.get_page_source()

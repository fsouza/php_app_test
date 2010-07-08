from lettuce import before, after, world
from selenium import get_driver, FIREFOX

@before.all
def setup_browser():
    world.browser = get_driver(FIREFOX)
    world.root_url = 'http://localhost/'

@after.all
def teardown_browser():
    world.browser.quit()

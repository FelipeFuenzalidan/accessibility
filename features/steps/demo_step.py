import allure
from axe_selenium_python import Axe
from behave import step
from selenium import webdriver


@step('I am on google search page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://www.google.com/')


@step('I inject axe-core javascript into page')
def step_impl(context):
    context.axe = Axe(context.driver)
    context.axe.inject()


@step('I run axe accessibility checks')
def step_impl(context):
    context.results = context.axe.run()


@step('I write results to file')
def step_impl(context):
    context.axe.write_results(context.results["violations"], 'demo_google.json')
    context.driver.close()
    assert len(context.results["violations"]) == 0, context.axe.report(context.results["violations"])

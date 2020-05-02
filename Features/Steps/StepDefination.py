from behave import *
from selenium.webdriver import Chrome

@given(u'User is on registration page')
def step_impl(context):
    context.driver.get("http://www.theTestingWorld.com/testings")

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name("fld_username").send_keys("User1")

@when(u'User enters email ID')
def step_impl(context):
    context.driver.find_element_by_name("fld_email").send_keys("user11111@admin.com")

@when(u'User enters Password')
def step_impl(context):
    context.driver.find_element_by_name("fld_password").send_keys("Hello@123")

@when(u'User click on sign-up button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Sign up']").click()

@then(u'User should register successfully')
def step_impl(context):
    print("Registered Successfully")


@when(u'User enters duplicate username')
def step_impl(context):
    print("Duplicate Username")


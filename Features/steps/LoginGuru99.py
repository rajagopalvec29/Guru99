from selenium import webdriver
from behave import *
from PageObjects.loginObjects import Login99
from webdriver_manager.firefox import GeckoDriverManager
import time
from Utility.Config import configread

@given(u'Launch Firefox browser')
def step_impl(context):
    context.driver = configread.lauchbrowser()

@then(u'Open Guru99 Url')
def step_impl(context):
    url = configread.configurl()
    lp = Login99(context.driver)
    lp.Openhomepage(url)

@then(u'enter "{userid}" and "{password}"')
def step_impl(context,userid,password):
    lp = Login99(context.driver)
    lp.EnterUserid(userid)
    lp.EnterPassword(password)


@then(u'click submit')
def step_impl(context):
    lp = Login99(context.driver)
    lp.ClickLoginbtn()
    try:
        alert = context.driver.switch_to_alert()
        alert.accept()
        context.driver.quit()
        assert False
    except:
        assert True
        context.driver.quit()





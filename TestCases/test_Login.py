import pytest
from Utility.Config import configread
from selenium import webdriver
from PageObjects.loginObjects import Login99
import time

class Test_001_login:
    driver = configread.lauchbrowser()
    url = configread.configurl()
    userid = configread.configuserid()
    password = configread.configpassword()

    def test_Login(self):
        lp = Login99(self.driver)
        lp.Openhomepage(self.url)
        lp.EnterUserid(self.userid)
        lp.EnterPassword(self.password)
        lp.ClickLoginbtn()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.quit()
            assert False
        except:
            lp.Clicklogout()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.quit()
            assert True








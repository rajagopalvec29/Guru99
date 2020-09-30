from Utility.Config import configread
from PageObjects.loginObjects import Login99
from Utility import XLUtility
import time


class Test_002_loginDD:
    url = configread.configurl()
    path = 'TestData/Gurulogin.xlsx'

    def test_LoginDD(self):
        self.driver = configread.lauchbrowser()
        lp = Login99(self.driver)
        lp.Openhomepage(self.url)
        rows = XLUtility.NoRows(self.path,'Sheet1')
        for rw in range(2,rows+1):
            username = XLUtility.readdata(self.path, 'Sheet1', rw, 1)
            passowrd = XLUtility.readdata(self.path, 'Sheet1', rw, 2)
            lp.EnterUserid(username)
            lp.EnterPassword(passowrd)
            lp.ClickLoginbtn()
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
                XLUtility.writedata(self.path, 'Sheet1', rw, 3, 'Login Fail')
            except:
                time.sleep(2)
                lp.Clicklogout()
                time.sleep(1)
                alert = self.driver.switch_to.alert
                alert.accept()
                XLUtility.writedata(self.path, 'Sheet1', rw, 3, 'Login Pass')

        self.driver.quit()

















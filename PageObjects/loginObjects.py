from selenium import webdriver
import time


class Login99:
    url = 'http://www.demo.guru99.com/V4/index.php'
    userid = 'uid'
    passid =  'password'
    btnlogin = 'btnLogin'
    linklogout = 'Log out'

    def __init__(self,driver):
        self.driver = driver

    def Openhomepage(self,url):
        self.driver.get(url)

    def EnterUserid(self,username):
        self.driver.find_element_by_name(self.userid).send_keys(username)

    def EnterPassword(self,password):
        self.driver.find_element_by_name(self.passid).send_keys(password)

    def ClickLoginbtn(self):
        self.driver.find_element_by_name(self.btnlogin).click()


    def Clicklogout(self):
        self.driver.find_element_by_link_text(self.linklogout).click()





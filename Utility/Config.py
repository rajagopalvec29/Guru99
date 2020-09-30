from selenium import webdriver

class configread:
    @staticmethod
    def configurl():
        url = 'http://www.demo.guru99.com/V4/index.php'
        return url

    @staticmethod
    def configuserid():
        username = 'mngr287661'
        return username

    @staticmethod
    def configpassword():
        password = 'ygYguqu'
        return password

    @staticmethod
    def lauchbrowser():
        driver = webdriver.Chrome(executable_path='Webdriver/chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
from selenium.webdriver.common.by import By
import time
import os
import configparser
class login:
    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)

    config=configparser.RawConfigParser()
    config.read(os.path.abspath(os.curdir) + r'\\config\\config.ini')
    email=(config.get('commonInfo', 'baseid'))
    passwd=(config.get('commonInfo', 'basepasswrd'))
    def login_1(self):
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(self.email)
        self.driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys(self.passwd)
        self.driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]').click()

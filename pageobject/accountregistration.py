# registration form to fill the entities
from jinja2 import TemplateRuntimeError
from selenium.webdriver.common.by import By
import time

class accountpage:
    txt_first_name='customer_firstname'
    xpath_last_name='customer_lastname'
    txt_email='email'
    txt_password='passwd'
    register_buttn='submitAccount'

    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)

    def setfirstname(self,frstname):
        self.driver.find_element(By.NAME, self.txt_first_name).send_keys(frstname)

    def setlastname(self, lstname):
        self.driver.find_element(By.NAME, self.xpath_last_name).send_keys(lstname)

    def setemail(self, email):
        self.driver.find_element(By.NAME, self.txt_email).send_keys(email)

    def setpasswd(self, pswd):
        self.driver.find_element(By.NAME, self.txt_password).send_keys(pswd)

    def setregtclick(self):
        self.driver.find_element(By.NAME,self.register_buttn).click()

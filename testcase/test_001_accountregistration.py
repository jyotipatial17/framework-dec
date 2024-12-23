import pytest
import time
from pageobject import homepage as home
from pageobject import accountregistration as account
from utility.logger import loggen
from pageobject import Search
import configparser  # to read data from ini file
import os

class Test_001:
    #Create an instance of RawConfigParser
    config=configparser.RawConfigParser()
    # Read the config file
    config.read(os.path.abspath(os.curdir)+ r'\\config\\config.ini')
    # Access values from the config file
    url=(config.get('commonInfo', 'baseurl'))
    logger = loggen.log_txt()
    # we have no need to creat object for static method juts call using class name
    def test_account_reg(self,setup):

        self.logger.info("   Test 001 account Registration started   ")
        self.driver=setup     # set browser from user
        self.driver.get(self.url)  # access url from config file
        self.logger.info("   Launching Browser  ")
        self.driver.maximize_window()
        # we enter email and click on register button
        home.obj1=home.homep(self.driver)
        home.obj1.setregistlogin("jasminethakur.jo1@gmail.com")
        time.sleep(5)
        # we enter into form details
        account.obj3=account.accountpage(self.driver)
        account.obj3.setfirstname("jyoti")
        account.obj3.setlastname("bala")
        account.obj3.setemail("jasminethakur.jo1@gmailcom")
        account.obj3.setpasswd("set123")
        account.obj3.setregtclick()
        self.logger.info("   Test 001 Account Registration successfully Ended   ")
        self.driver.close()






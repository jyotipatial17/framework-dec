import time
from selenium.webdriver.common.by import By
from pageobject import firstaddress as ad
from pageobject import excel_code as utl
from pageobject import login as lgt
from selenium.webdriver.common.alert import Alert
import configparser  # to read data from ini file

import os
# here error will add in the last coloumn of sheet when repeted adress is used.
# data -driven testing is done.
class Test_003:
    config=configparser.RawConfigParser()
    config.read(os.path.abspath(os.curdir)+ r'\\config\\config.ini')
    url=(config.get('commonInfo', 'baseurl'))

    def test_home_adress(self,setup):
        self.driver=setup     # set browser from user
        self.driver.get(self.url)  # access url from config file
        self.driver.maximize_window()
        # we login with valid credentials
        lgt.obj6=lgt.login(self.driver)
        lgt.obj6.login_1()
        ad.obj5 = ad.adress(self.driver)
        file =(os.path.abspath(os.curdir)+ r'\\testdata\\data.xlsx')
        rows = utl.getRowCount(file,"Sheet3")
        # fetching data from excel ..for 1 row move to column...1,2,3,4,5,6
        for r in range(2, rows+1):
            name=utl.readData(file, "Sheet3", r, 1)
            lstname=utl.readData(file, "Sheet3", r, 2)
            homeadrs= utl.readData(file, "Sheet3", r, 3)
            city = utl.readData(file, "Sheet3", r, 4)
            state= utl.readData(file, "Sheet3", r, 5)
            pincode= utl.readData(file, "Sheet3", r, 6)
            phone = utl.readData(file, "Sheet3", r, 7)
            # after fetching data fill in the website automatically
            ad.obj5.ads_buton()
            ad.obj5.frst_name(name)
            ad.obj5.lst_name(lstname)
            ad.obj5.home_ads(homeadrs)
            ad.obj5.home_city(city)
            ad.obj5.home_state(state)
            ad.obj5.home_pin(pincode)
            ad.obj5.home_phone(phone)
            time.sleep(5)
            ad.obj5.home_button()

            act_value=self.driver.find_element(By.XPATH, '//*[@class="alert alert-danger"]/p').text
            utl.writeData(file, "Sheet3", r, 8, act_value)  # mentioned text after it fill out the address

            time.sleep(5)
            self.driver.find_element(By.XPATH,'//*[@class="icon-chevron-left"]').click()
            self.driver.find_element(By.XPATH, '//*[@class="icon-chevron-left"]').click()
            time.sleep(5)
            # alt = self.driver.switch_to.alert()
            # alt.accept()
        self.driver.close()
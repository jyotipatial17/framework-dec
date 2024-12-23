import time
from selenium.webdriver.common.by import By
from utility.logger import loggen
from pageobject import Search
from pageobject import excel_code as utl
import configparser  # to read data from ini file
import os

class Test_001:
    config=configparser.RawConfigParser()
    config.read(os.path.abspath(os.curdir)+ r'\\config\\config.ini')
    url=(config.get('commonInfo', 'baseurl'))
    logger = loggen.log_txt()
    def test_search_item(self,setup):

        self.logger.info("   Test 002 Search items started   ")
        self.driver=setup     # set browser from user
        self.driver.get(self.url)  # access url from config file
        self.logger.info("   Launching Browser  ")
        self.driver.maximize_window()
        # we search the items
        Search.obj4 = Search.search(self.driver)


        file =(os.path.abspath(os.curdir)+ r'\\testdata\\data.xlsx')
        rows = utl.getRowCount(file, "Sheet2")
        # fetching data from excel ..for 1 row move to column...1,2,3,4,5,6
        for r in range(2, rows + 1):
            txt=utl.readData(file, "Sheet2", r, 1)
            real=utl.readData(file, "Sheet2", r, 2)
            # after fetching data fill in the website automatically
            Search.obj4.search_txt(txt)
            Search.obj4.search_button()
            act_value=self.driver.find_element(By.XPATH, "//*[@class='lighter']").text
            print("We are entering in", act_value, "search section")
            self.driver.find_element(By.XPATH,'//*[@class="icon-home"]').click()

            if real==act_value:
                print("test passed")
                utl.writeData(file, "Sheet2", r, 3, "Passed")  # mentioned pass if value match
                utl.fillGreenColor(file, "Sheet1", r, 3)  # fill with color green
            else:
                print("test failed")
                utl.writeData(file, "Sheet2", r, 3, "Failed")
                utl.fillRedColor(file, "Sheet2", r, 3)
        print(act_value)
        print(real)
        self.driver.close()

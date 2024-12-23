# its a home page of application
# to register into application
from selenium.webdriver.common.by import By
import time
import os

class homep:
    subm_butn='//*[@id="SubmitCreate"]'
    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)

    def setregistlogin(self,email):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="email_create"]').send_keys(email)
        self.driver.find_element(By.XPATH, self.subm_butn).click()
        re_url=self.driver.current_url

        # if re_url=="http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation":
        #     assert True
        # else:
        #     print(re_url)
        #     screen_path=(os.path.abspath(os.curdir)+ r'\\framework\\screenshot\\failed_registration.png')
        #     self.driver.save_screenshot(screen_path)
        #     assert False

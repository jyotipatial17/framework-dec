# search the item
import time
from selenium.webdriver.common.by import By

class search:
    search_buttn='submit_search'

    search_box='//*[@name="search_query"]'
    time.sleep(4)
    def __init__(self,driver):
        self.driver=driver
        time.sleep(4)

    def search_txt(self,txt):
        self.driver.find_element(By.XPATH, self.search_box).send_keys(txt)
    def search_button(self):
        self.driver.find_element(By.NAME, self.search_buttn).click()

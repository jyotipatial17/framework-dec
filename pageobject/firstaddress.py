import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select as sel
class adress:
    # XPATH of element
    ads_button='//*[@title="Addresses"]/i'
    ads_but2 = '//*[@title="Add an address"]'
    fst_name='firstname'
    last_name='//*[@name="lastname"]'
    homadres='address1'
    city='//*[@name="city"]'
    state='//*[@name="id_state"]'
    pin='//*[@id="postcode"]'
    # cntry='//*[@id="id_country"]'
    hmphone='//*[@id="phone"]'
    hmbutn='//*[@id="submitAddress"]'
    def __init__(self,driver):
        self.driver=driver
        time.sleep(4)
    def ads_buton(self):
        self.driver.find_element(By.XPATH,self.ads_button).click()
        self.driver.find_element(By.XPATH, self.ads_but2).click()
    def frst_name(self,name):
        self.driver.find_element(By.NAME,self.fst_name).send_keys(name)
    def lst_name(self,lstname):
        self.driver.find_element(By.XPATH,self.last_name).send_keys(lstname)
    def home_ads(self,homeadrs):
        self.driver.find_element(By.ID,self.homadres).send_keys(homeadrs)
    def home_city(self,city):
        self.driver.find_element(By.XPATH,self.city).send_keys(city)
    # Select by DROP DOWN
    def home_state(self,state):
        drop=sel(self.driver.find_element(By.XPATH,self.state))
        drop.select_by_visible_text(state)

    def home_pin(self,pincode):
        self.driver.find_element(By.XPATH,self.pin).send_keys(pincode)
    # def home_country(self,country):
    #     drop1=sel(self.driver.find_element(By.XPATH,self.cntry))
    #     drop1.select_by_visible_text(country)
    def home_phone(self,phone):
        self.driver.find_element(By.XPATH, self.hmphone).send_keys(phone)

    def home_button(self):
        self.driver.find_element(By.XPATH, self.hmbutn).click()

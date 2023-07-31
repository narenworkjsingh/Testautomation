from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Dashboardpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in dashboard page
    label_currentlisting = (By.XPATH, "//a[text()='Current Listings']")
    
    img_feedback =(By.XPATH, "//*[local-name()='svg' and @aria-label='Feedback']")
    img_logout = (By.XPATH, "//*[local-name()='svg' and @aria-label='Logout']")
    btn_dashsearch = (By.XPATH, "//button[text()='Search by city or town name']")
    btn_smartsearch = (By.XPATH, "//button[text()='Smart Search']")
    btn_regions = (By.XPATH, "//button[text()='Region']")
    btn_address = (By.XPATH, "//button[text()='Address']")
    btn_zipcode = (By.XPATH, "//button[text()='Zipcode']")
    btn_collection = (By.XPATH, "//button[text()='Collection']")
    txt_findnatural = (By.XPATH, "//textarea[@placeholder='Find properties your natural language...']")
    btn_search = (By.XPATH, "//button[text()='Search']")
    elm_smartresult = (By.XPATH, "//tr[@class ='MuiTableRow-root css-1q58hck']")
    


# methods for dashboard page
# method to click logout button
    def click_logout(self):
        self.click(self.img_logout)
        time.sleep(5)

# Check dashboard page loaded successuflly
    def check_dashboardpageload(self):
        self.check_elementpresent(self.label_currentlisting)

# click dashboard search button
    def click_dashsearchbutton(self):
        self.click(self.btn_dashsearch)
        time.sleep(5)

# method for smart search 
    def check_smartsearch(self, smartsearchtext):
        self.click(self.btn_smartsearch)
        time.sleep(4)
        self.send_keys(self.txt_findnatural, smartsearchtext)
        self.click(self.btn_search)
        time.sleep(20)

# Check Smart search result   
    def verify_smartsearchresult(self):
        if (self.get_elementscount(self.elm_smartresult)==True):
            assert True, "smart search working fine for selected text"
        else:
            assert False, "Smart search is not showing result. please check"




    





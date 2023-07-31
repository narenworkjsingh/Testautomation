from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Collectionpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in collection page 
    img_collection = (By.XPATH, "//div[@aria-label='Collections']//ancestor::div[@role='button']")
    btn_createcollection = (By.XPATH, "//button//span[text()='Create collection']")
    lst_searchbykeyword = (By.XPATH, "//li[text()='Search by keyword']")
    edt_searchquery = (By.XPATH, "//input[@placeholder='Search query']")
    btn_creatnewcollection = (By.XPATH, "//div[@class='MuiBox-root css-1yuhvjn']//following-sibling::button[text()='Create collection']")
    btn_view = (By.XPATH, "//button[text()='View']")
    img_listview = (By.XPATH, "//*[local-name()='svg' and @data-testid='ViewListIcon']")
    btn_delete = (By.XPATH, "(//button[text()='Delete'])[1]")
    
# methods for collection page
# Click on Collection icon
    def click_collectionicon(self):
        self.click(self.img_collection)
        time.sleep(5)

# check collection page load
    def check_collectionpageload(self):
        self.check_elementpresent(self.btn_createcollection)

# click on Create Collection button
    def click_createcollection(self):
        self.click(self.btn_createcollection)
        time.sleep(15)

# select search by keyword option   
    def click_searchbykeywords(self):
        self.click(self.lst_searchbykeyword)
        time.sleep(2)

# enter collection cretiera and add collections
    def setup_newcollection(self, searchbykeywords):
        self.send_keys(self.edt_searchquery, searchbykeywords)
        self.click(self.btn_creatnewcollection)
        time.sleep(15)
# verify collection has created 
    def check_collectioncreated(self):
        count = self.check_elementscount(self.btn_view)
        if (count == True):
            assert True, "Collection created successfully"
            self.browserrefresh()
            time.sleep(5)
        else:
            self.browserrefresh()
            assert False, "Collection has not created please check for error"
# verify delete collection
    def check_deletecollection(self):
        self.click(self.img_listview)
        time.sleep(5)
        self.click(self.btn_delete)
        time.sleep(5)
               




import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from driver.test_base import BaseTest


class Testcheck(BaseTest):
    def __init__(self, driver):
      super().__init__(driver)
      self.driver = driver

# define pages for the test
# capture the object

    itemcount = (By.XPATH, "//span[@class='badge badge-pill badge-info m-2']")
    refreshbutton = (By.XPATH, "//i[@class='fa fa-refresh']")
    zerocount = (By.XPATH, "(//span[@class='badge m-2 badge-warning'])[1]")
    firstcount = (By.XPATH, "(//span[@class='badge m-2 badge-primary'])[1]")
    plusicon = (By.XPATH, "(//i[@class='fa fa-plus-circle'])[1]")
    plusiconsecond = (By.XPATH, "(//i[@class='fa fa-plus-circle'])[2]")
    plusiconthird = (By.XPATH, "(//i[@class='fa fa-plus-circle'])[3]")
    minusiconfirst = (By.XPATH, "(//i[@class='fa fa-minus-circle'])[1]")
    minusiconsecond = (By.XPATH, "(//i[@class='fa fa-minus-circle'])[2]")
    minusiconthrid = (By.XPATH, "(//i[@class='fa fa-minus-circle'])[3]")
    deleteiconfirst = (By.XPATH, "(//button[@class='btn btn-danger'])[1]")
    deleteiconsecond = (By.XPATH, "(//button[@class='btn btn-danger'])[2]")
    deleteiconthird = (By.XPATH, "(//button[@class='btn btn-danger'])[3]")
    deleteicontfour = (By.XPATH, "(//button[@class='btn btn-danger'])[4]")

# method for testing the pages
# method to test add items
 
    def testadditem(self):
        time.sleep(15)
        self.assert_element(self.zerocount, "Zero")
        gettext = self.get_elmtext(self.zerocount)
        
        if(gettext == "Zero"):
            #click on the pluse icon
            self.click(self.plusicon)
            time.sleep(4)
            #Verify the count change from zero to one
            self.assert_element(self.firstcount, str(1))
            
        else:
            self.click(self.plusicon)
            time.sleep(3)
            self.assert_element(self.zerocount, str(1) )

    # method is created to check total count when added the item   
    def totalcountadd(self):
        #test total count when adding the items
        #click the next plus icon
        self.click(self.plusiconsecond)
        self.assert_element(self.itemcount, str(2))
        #click the next plus icon
        self.click(self.plusiconthird)
        self.assert_element(self.itemcount, str(3))
        
    # method is created to check total count when deleted the item    
    def totalcountminus(self):
        self.click(self.minusiconfirst)
        self.assert_element(self.itemcount, str(2))
        self.click(self.minusiconsecond)
        self.assert_element(self.itemcount, str(1))
        self.click(self.minusiconthrid)
        self.assert_element(self.itemcount, str(0))

    #method is created to see if the item is deleted successfully
    def totalcountdelet(self):    
        # test total count when deleting the items
        self.click(self.deleteiconfirst)
        self.elm_visibilty(self.deleteiconthird)
        self.click(self.deleteiconsecond)
        self.elm_visibilty(self.deleteiconsecond)
    # method to check refresh icon functionality
    def pgrefresh(self):
        self.click(self.refreshbutton)
        time.sleep(2)
    # verify that item count is showing as 0
        self.assert_element(self.itemcount, str(0))
    # verify that row count is showing 0
        self.assert_element(self.zerocount, "Zero")
                








        





    



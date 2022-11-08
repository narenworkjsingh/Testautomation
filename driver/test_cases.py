import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.testcheck import Testcheck
from utility.utility import Utility

# Test case for testing the counter app
@pytest.mark.usefixtures("getDriver")
#@ddt
class TestCases():
    
    # Test method to check add count
    def test_addcount(self):
        testchk = Testcheck(self.driver)
        testchk.testadditem()
    
    # Test method to check total count when adding the item
    def test_totalcountadd(self):
        totalcount = Testcheck(self.driver)  
        totalcount.totalcountadd() 
    
    #Test method to check total when minus the item
    def test_totalcountminus(self):
        totalminus = Testcheck(self.driver)
        totalminus.totalcountminus()     

    # test method to check total count when delete the items
    def test_totalcountdelete(self):
        delcount = Testcheck(self.driver)
        delcount.totalcountdelet()  

    # test method to check the refresh page 
    # Verify the total item count is showing 0
    # verify that item count is showing zero text
    def test_checkrefresh(self):
        checkref = Testcheck(self.driver)
        checkref.pgrefresh()

              

                         




        
        
    

    
        
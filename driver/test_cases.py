import pytest
import time
from selenium.webdriver.common.by import By
from pages.loginpage import Loginpage
from pages.dashboardpage import Dashboardpage
from pages.collectionpage import Collectionpage
from pages.prospectpage import Prospectpage
from pages.marketpage import Marketpage
from pages.articlepage import Articlespage
from pages.statspage import Statspage
from pages.alertpage import Alertpage
from pages.settingpage import Settingpage
from utility.utility import Utility

# Test case for testing the counter app
@pytest.mark.usefixtures("getDriver")
#@ddt
class TestCases():
    
    # Test case to verify login functionality
    #@pytest.mark.build
    def test_loginfunctionality(self):
        username = Utility.getjsondata('login', 'username')
        password = Utility.getjsondata('login', 'password')
        loginpage = Loginpage(self.driver)
        loginpage.login(username, password)
        time.sleep(5)

    #@pytest.mark.build    
    # Test case to verify pages loads fine
    def test_dashboardpageload(self):
        dashboardpage = Dashboardpage(self.driver)
        dashboardpage.check_dashboardpageload()
        smartsearch = Utility.getjsondata('propertysearch', 'smartsearchtext')
        dashboardpage.click_dashsearchbutton()
        dashboardpage.check_smartsearch(smartsearch)
    
    #@pytest.mark.build
    # Test case to verify collection page loads fine
    def test_collectionpageload(self):
        collectionpage = Collectionpage(self.driver)
        collectionpage.click_collectionicon()
        time.sleep(5)
        collectionpage.check_collectionpageload()   

    # test case to verify creating new collections
    ##@pytest.mark.build
    def test_createnewcollection(self):
        newcollection = Collectionpage(self.driver)
        searchbykeword = Utility.getjsondata('newcollection', 'searchbykewords')
        newcollection.click_createcollection()
        newcollection.click_searchbykeywords()
        newcollection.setup_newcollection(searchbykeword)
        newcollection.check_collectioncreated()

    #test case to verify delete collection
    def test_deletecollection(self):
        deletecollection = Collectionpage(self.driver)
        deletecollection.check_deletecollection()  
            
    #@pytest.mark.build
    # Test case to verify prospect page loads fine
    def test_prospectpageload(self):
        prospectpage = Prospectpage(self.driver)  
        prospectpage.click_prospecticon()
        time.sleep(5)
        prospectpage.check_prospectpageload()

    # test case to verify heatmap loads fine.
    def test_heatmapload(self):
        heatmap = Prospectpage(self.driver)
        heatmap.check_heatmapload()

    
    #@pytest.mark.build
    # Test case to verify Market page loads fine
    def test_marketpageload(self):
        marketpage = Marketpage(self.driver)    
        marketpage.click_marketicon()
        time.sleep(5)
        marketpage.check_marketpageload()
    
    # Test data loads for apperication properties
    def test_marketappericationproperty(self):
        appr = Marketpage(self.driver)
        appr.check_apprtabledataloads()

    #@pytest.mark.build
    # Test case to verify article page loads fine
    def test_articlepageload(self):
        articlepage = Articlespage(self.driver)
        articlepage.click_articleicon()
        time.sleep(5)
        articlepage.check_articlepageload()   
    
    #@pytest.mark.build
    # test case to verify stats page loads fins
    def test_statsoageload(self):
        statspage = Statspage(self.driver)
        statspage.click_statsicon()
        time.sleep(5)
        statspage.check_statspageload()

    #@pytest.mark.build
    
    # test case to verify alert page loads fine
    def test_alertpageload(self):
        alertpage = Alertpage(self.driver)
        alertpage.click_alerticon()
        time.sleep(5)
        alertpage.check_alertpageload()
    
    #@pytest.mark.build
    # test case to verify setting page loads fine
    def test_settingpageload(self):
        settingpage = Settingpage(self.driver)
        settingpage.click_settingicon()
        time.sleep(5)
        settingpage.check_settingpageload()
        dashboardpage = Dashboardpage(self.driver)
        dashboardpage.click_logout()        

   

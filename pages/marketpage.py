from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Marketpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# cpature object in marktet page
    img_market = (By.XPATH, "//*[local-name()='svg' and @data-testid='ShowChartIcon']")
    label_marketheading = (By.XPATH, "//h1[text()='Current U.S. market status']")
    btn_yoy = (By.XPATH, "//button[@value='yoy']")
    btn_apperication = (By.XPATH, "//button[@value='apr']")
    btn_str = (By.XPATH, "//button[@value='str']")
    btn_ltr = (By.XPATH, "//button[@value='ltr']")
    btn_view = (By.XPATH, "//a[text()='View']")

# method for market page

# click marktet icon 
    def click_marketicon(self):
        self.click(self.img_market)
        time.sleep(5)

# method to check market page loads
    def check_marketpageload(self):
        self.check_elementpresent(self.label_marketheading)

# method to check YOY data loads up in the table
    def check_apprtabledataloads(self):
        self.click(self.btn_apperication)
        time.sleep(4)
        rescount = self.check_datatableloads(self.btn_view)
        print(rescount)
        if(rescount == True):
            assert True, "Datatable shows the apperication data"
        else:
            assert False, "Apperication data is not showing up in datatable."

from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Statspage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in state page
    img_stats = (By.XPATH, "//*[local-name()='svg' and @data-testid='AnalyticsIcon']")
    label_listing = (By.XPATH, "//h3[text()='Top Five Regions Listings']")

# methods for stats page
# click on stats icon
    def click_statsicon(self):
        self.click(self.img_stats)
        time.sleep(5)    

# check stats page load
    def check_statspageload(self):
        self.check_elementpresent(self.label_listing)    
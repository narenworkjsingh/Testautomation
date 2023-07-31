from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Alertpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture objects in alert page
    btn_alert = (By.XPATH, "//*[local-name()='svg' and @data-testid='NotificationsIcon']")
    btn_viewall = (By.XPATH, "//button[text()='View all']")

# method for alert page 
# click on alert icon
    def click_alerticon(self):
        self.click(self.btn_alert)
        time.sleep(5)

# check alert page loads
    def check_alertpageload(self):
        self.check_elementpresent(self.btn_viewall)
        self.click(self.btn_viewall)
        time.sleep(5)

from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Settingpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in setting page
    img_setting = (By.XPATH, "//*[local-name()='svg' and @aria-label='Settings']")
    label_email = (By.XPATH, "//th[text()='Email']")

# method for setting page
# click on setting icon
    def click_settingicon(self):
        self.click(self.img_setting)
        time.sleep(5)
# check setting page load
    def check_settingpageload(self):
        self.check_elementpresent(self.label_email)        

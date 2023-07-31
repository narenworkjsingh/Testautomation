from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Prospectpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in prospect page
    img_prospect = (By.XPATH, "//*[local-name()='svg' and @data-testid='ExploreIcon']") 
    btn_hospital = (By.XPATH, "//button[text()='Hospitals']")
    btn_default = (By.XPATH, "//button[text()='Default']")
    btn_heatmap = (By.XPATH, "//button[text()='Heat map']")
    lst_yoyselection = (By.XPATH, "//div[@aria-haspopup='listbox']")

# mthods for prospect page
# click on prospect icon
    def click_prospecticon(self):
        self.click(self.img_prospect)
        time.sleep(5)

# method to check prospect page loads fine
    def check_prospectpageload(self):
        self.check_elementpresent(self.btn_hospital) 

#mthod to check default map loads fine
    def check_defaultmapload(self):
        self.click(self.btn_default)
        time.sleep(5)

#method to check heat map loads fine
    def check_heatmapload(self):
        self.click(self.btn_heatmap)
        time.sleep(5)
        self.check_elementpresent(self.lst_yoyselection) 

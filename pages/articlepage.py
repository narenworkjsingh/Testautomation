from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time

class Articlespage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture object in Article page
    img_article = (By.XPATH, "//*[local-name()='svg' and @data-testid='ArticleIcon']")
    btn_readarticle = (By.XPATH, "(//h6[text()='Read Full Article'])[1]")

# click article icon 
    def click_articleicon(self):
        self.click(self.img_article)
        time.sleep(5)

# check article page load
    def check_articlepageload(self):
        self.check_elementpresent(self.btn_readarticle)
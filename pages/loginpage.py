from selenium.webdriver.common.by import By
from driver.test_base import BaseTest
import time


class Loginpage(BaseTest):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# capture obhects in login page
    
    edt_email = (By.NAME, "email")
    edt_password = (By.NAME, "password")
    btn_signin = (By.XPATH, "//button[text()='Sign in']")
    chk_rememberme = (By.XPATH, "//span[text()='Remember me']")
    lnk_forgotpassword = (By.XPATH, "//h6[text()='Forgot Password?']")\

# methods for login page

# method for entering email and password
    def login(self, username, password):
        self.send_keys(self.edt_email, username)
        self.send_keys(self.edt_password, password)
        self.click(self.btn_signin)
        time.sleep(5)

# method to click forgot password link
    def forgotpassword(self):
        self.click(self.lnk_forgotpassword)
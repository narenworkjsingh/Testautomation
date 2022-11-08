import pytest
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE

# common method used in framework
pytest.mark.usefixtures("getDriver")
class BaseTest:
    def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()
    
    def send_keys(self, by_locator, value):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)
    
    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innertext")
    
    def wait_for(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator))

    def assert_element(self, by_locator, text):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
    
        try:
            assert text in element.text
            print("Passed in Assertion" + "expecting for" + text + "but actual is" +element.text)
        except AssertionError:
            print("Failed in Assertion" + "expecting for" + text + "but actual is" +element.text)
            print(traceback.format_exc())    

    def press_key(self, by_locator, key):
        if(key == "enter"):
            self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_elmtext(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        print(element.text)
        return element.text 
    
    def elm_visibilty(self, by_locator):
        try:
            assert self.wait.until(EC.presence_of_element_located(by_locator))
            assert True
            print("passed: selected record row has deleted")
        except TE:
            print("failed: selected element is still showing up") 
            assert False
            
               

         
        



    





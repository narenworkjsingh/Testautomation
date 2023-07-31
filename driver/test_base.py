import pytest
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import NoSuchElementException as NE

# common method used in framework
pytest.mark.usefixtures("getDriver")
class BaseTest:
    def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 10)

    def browserrefresh(self):
        self.driver.refresh()  

    def click(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator)).click()
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to click the element: {}".format(str(e)))    

    
    def send_keys(self, by_locator, value):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to send keys to the element: {}".format(str(e)))    
    
    def get_text(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innertext")
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to get the element text: {}".format(str(e)))
    
    def wait_for(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while waiting for the element: {}".format(str(e)))    

    def assert_element(self, by_locator, text):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
    
        try:
            assert text in element.text
            print("Passed in Assertion" + "expecting for" + text + "but actual is" +element.text)
        except AssertionError:
            print("Failed in Assertion" + "expecting for" + text + "but actual is" +element.text)
            print(traceback.format_exc())    

    def press_key(self, by_locator, key):
        try:
            if(key == "enter"):
                self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(Keys.ENTER)
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to press the key: {}".format(str(e)))        

    def get_elmtext(self, by_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            print(element.text)
            return element.text 
        except TE:
            print("Element not found on page within the specified time.")
        except Exception as e:
            print("An error occurred while trying to get the element text: {}".format(str(e)))
    
    def elm_visibilty(self, by_locator):
        try:
            assert self.wait.until(EC.presence_of_element_located(by_locator))
            assert True, "Selected element is visible"
            return True
        except TE:
            assert False, "Selected element is not visible in page, please check the element properties"
            return False
            
        
    def get_elementscount(self, by_locator):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located((by_locator)))
            print(len(elements))
            assert len(elements) > 1, "Result are showing more than one object"
            return True
        except NE:
            print("Selected element is not present in search result")    
        else:
         print("No Matching element found for given selector")
         return False
        
    def check_elementpresent(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            assert True, "Object exist on the page"
        except TE:
            assert False, "Object does not exist on the page"
        except Exception as e:
            print("An error occurred while waiting for the element: {}".format(str(e)))        
                                     

    def check_elementscount(self, by_locator):
        
            try:
                elements = self.wait.until(EC.presence_of_all_elements_located((by_locator)))
                print(len(elements)) 
                count = len(elements) + 1
                print(count)
                counter = 0
                while counter < 40: 
                    elements = self.wait.until(EC.presence_of_all_elements_located((by_locator)))   
                    if (len(elements) == count):
                        return True
                        break
                    else:
                        print(counter)
                    counter += 1                        
            except NE:
              print("Selected element is not present in search result")
              return False    
         

    def elm_action(self, by_locator):
        action = ActionChains(self.driver)
        actionelement = self.wait.until(EC.presence_of_element_located(by_locator))
        action.move_to_element(actionelement).perform()
        actionelement.click()

    def check_datatableloads(self, by_locator):
        
            try:
                elements = self.wait.until(EC.presence_of_all_elements_located((by_locator)))
                count = len(elements)
                print(count)
                if(count > 0):
                    return True, "Datatable showing the data"
                else:
                    return False, "Datatable does not show up the data"
                                           
            except NE:
              print("Selected element is not present in search result")
              return False    
        



    





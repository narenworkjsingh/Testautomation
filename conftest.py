import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webbrowser import get
import time
from datetime import datetime

#browser = "chrome"
global driver

def pytest_addoption(parser):
   parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def getBrowser(request):
   browser = request.config.getoption("--browser")
   return browser


@pytest.fixture(scope="class")
def getDriver(request, getBrowser):
    #drivercommn = None
    if getBrowser == "chrome":
       chrome_options = Options()
       chrome_options.add_experimental_option("detach", True)
       chrome_executable = Service(executable_path="C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
       driver = webdriver.Chrome(service=chrome_executable,options=chrome_options)
       #driver = webdriver.Chrome(executable_path="C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
    elif getBrowser == "firefox":    
       driver = webdriver.Firefox("C:/SeleniumDrivers/geckodriver-v0.31.0-win64")
       
    driver.get ("http://localhost:3000/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield request.cls.driver
    time.sleep(20)
    #//driver.close()

def pytest_html_report_title(report):
   report.title = "TestCheck test exeuction report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
       extra.append(pytest_html.extras.url("https://stgadminverkademy.learnorteach.com/"))

       xfail = hasattr(report, "wasxfail")
       if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('getDriver')
            driver.save_screenshot('C:/Testcheck/reports'+timestamp+'.png')
            extra.append(pytest_html.extras.image('C:/Testcheck/reports'+timestamp+'.png')) 
            #extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
       report.extra = extra 
       if (report.passed):
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('getDriver')
            driver.save_screenshot('C:/Testcheck/reports'+timestamp+'.png')
            extra.append(pytest_html.extras.image('C:/Testcheck/reports'+timestamp+'.png')) 
       report.extra = extra  
          #file_name = report.nodeid.replace("::", "_")+".png"
          #driver.get_screenshot_as_file(file_name)
          #if file_name:
               #html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       #'onclick="window.open(this.src)" align="right"/></div>' % file_name
               #extra.append(pytest_html.extras.html(html))

            
         #extra.append(pytest_html.extras.html(screen_file))
         #report.extra = extra

  

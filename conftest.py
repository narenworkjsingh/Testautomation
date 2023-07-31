import pytest
import json
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webbrowser import get
import time
from datetime import datetime

#browser = "chrome"
global driver

def pytest_addoption(parser):
   #parser.addoption("--browser", action="store", default="chrome")
   #parser.addoption("--json-report", action="store", default=None,
    #                 help="Create a JSON report file with the specified filename.")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser to use for tests. Default is 'chrome'.")


@pytest.fixture(scope="class")
def getBrowser(request):
   browser = request.config.getoption("--browser")
   return browser


@pytest.fixture(scope="class")
def getDriver(request, getBrowser):
    #drivercommn = None
    if getBrowser == "chrome":
       chrome_options = Options()
       chrome_options.add_argument('--no-sandbox')
       chrome_options.add_argument('--disable-dev-shm-usage')
       chrome_options.add_experimental_option("detach", True)
       chrome_executable = Service(executable_path="C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
       driver = webdriver.Chrome(service=chrome_executable,options=chrome_options)
       #driver = webdriver.Chrome(executable_path="C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
    elif getBrowser == "firefox":    
       driver = webdriver.Firefox("C:/SeleniumDrivers/geckodriver-v0.31.0-win64")
       
    driver.get ("https://dashboard.zoomprop.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield request.cls.driver
    time.sleep(20)
   

# def pytest_html_report_title(report):
#    report.title = "ZoomProp test exeuction report"

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     timestamp = datetime.now().strftime('%H-%M-%S')
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#        extra.append(pytest_html.extras.url("https://dashboard.zoomprop.com/"))

#        xfail = hasattr(report, "wasxfail")
#        if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             feature_request = item.funcargs['request']
#             driver = feature_request.getfixturevalue('getDriver')
#             driver.save_screenshot('C:/DemoTest/reports'+timestamp+'.png')
#             extra.append(pytest_html.extras.image('C:/DemoTest/reports'+timestamp+'.png')) 
#             #extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#        report.extra = extra 
#        if (report.passed):
#             feature_request = item.funcargs['request']
#             driver = feature_request.getfixturevalue('getDriver')
#             driver.save_screenshot('C:/DemoTest/reports'+timestamp+'.png')
#             extra.append(pytest_html.extras.image('C:/DemoTest/reports'+timestamp+'.png')) 
#        report.extra = extra 
  
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     timestamp = datetime.now().strftime('%H-%M-%S')
#     timestamp_for_filename = datetime.now().strftime('%H-%M-%S').replace(':', '-')
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     result_data = {}

#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://dashboard.zoomprop.com/"))

#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             feature_request = item.funcargs['request']
#             driver = feature_request.getfixturevalue('getDriver')
#             screenshot_path = os.path.join('C:', 'DemoTest', f'reports{timestamp_for_filename}.png')
#             driver.save_screenshot(screenshot_path)
#             extra.append(pytest_html.extras.image(screenshot_path))
#             result_data['status'] = 'failed'
#             result_data['screenshot'] = screenshot_path
#         elif report.passed:
#             feature_request = item.funcargs['request']
#             driver = feature_request.getfixturevalue('getDriver')
#             screenshot_path = os.path.join('C:', 'DemoTest', f'reports{timestamp_for_filename}.png')
#             driver.save_screenshot(screenshot_path)
#             extra.append(pytest_html.extras.image(screenshot_path))
#             result_data['status'] = 'passed'
#             result_data['screenshot'] = screenshot_path
#         else:
#             result_data['status'] = 'skipped'
        
#         # Save the 'extra' information as 'details' in result_data
#         result_data['details'] = [str(detail) for detail in extra]
#         report.extra = extra

#         # Create the directory if it doesn't exist
#         #os.makedirs('C:/DemoTest', exist_ok=True)

#         # Save result_data to a JSON file
#         json_file_path = os.path.join('C:\\', 'DemoTest', f'reports{timestamp_for_filename}.json')
#         with open(json_file_path, 'w') as json_file:
#             json.dump(result_data, json_file)

# #     report.extra = extra
# def pytest_runtest_makereport(item, call):
#     report = None
#     try:
#         report = call.excinfo.getrepr()
#     except AttributeError:
#         pass

#     if hasattr(item, "_test_results"):
#         item._test_results.append({
#             "nodeid": item.nodeid,
#             "outcome": call.excinfo.typename if call.excinfo is not None else "passed",
#             "duration": call.stop-call.start,
#             "call": {
#                 "result": "failed" if call.excinfo is not None else "passed",
#                 "excinfo": str(report) if report else None,
#             }
#         })
#     else:
#         item._test_results = [{
#             "nodeid": item.nodeid,
#             "outcome": call.excinfo.typename if call.excinfo is not None else "passed",
#             "duration": call.stop-call.start,
#             "call": {
#                 "result": "failed" if call.excinfo is not None else "passed",
#                 "excinfo": str(report) if report else None,
#             }
#         }]
#     return report


# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     json_report_filename = config.getoption("--json-report")
#     if json_report_filename:
#         test_results = getattr(config.rootdir, "_test_results", [])
#         if test_results:
#             with open(json_report_filename, 'w') as f:
#                 json.dump(test_results, f, indent=2)
#         else:
#             print("No test results found. JSON report will not be generated.")

@pytest.fixture(scope='session')
def environment_info():
    info = {
        'environment': 'zoomprop_prod',
        'python_version': platform.python_version(),
        'operating_system': platform.system(),
        # Add more environment details as needed
    }
    return info

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("applicationname", 'zoomprop_prod')
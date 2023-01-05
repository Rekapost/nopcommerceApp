# Writing fixture to avoid duplication
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
#def setup(browser):
#   if browser=='chrome':
    serv_object=Service("C://Users//Reka//Drivers//chromedriver.exe")
    driver = webdriver.Chrome(service=serv_object)
    print("launching chrome browser")
#   elif browser=='firefox':
#       driver=webdriver.Firefox()
#       print("launching firefox browser")
#   else:
#       driver=webdriver.Ie()
#       print("launching Internet Explorer browser")
    return driver

#write two methods to get browser from command prompt
def pytest_addoption(parser):    # this will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # this will return the browser value to setup method
    return request.config.getoption("--browser")

# to generate  pytest  html report
# it is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Reka'
# it is hook for delete/modify environment info into HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

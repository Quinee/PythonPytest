import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )

@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )

    #driver.implicitly_wait( 5 )
    driver.get( "https://practicetestautomation.com/practice-test-login/" )
    yield driver  #Before test function execution
    driver.close()  #post your test function execution
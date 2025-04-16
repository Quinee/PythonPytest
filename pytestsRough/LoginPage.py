from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import *

from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID,"username")
        self.pwd_input = (By.ID, "password")
        self.submit = (By.ID,"submit")
    def login(self,uname,pwd):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(uname)#where * is used to unpack a tuple into separate arguments.it becmes > self.driver.find_element(By.ID, "username")
        self.driver.find_element(*self.pwd_input).send_keys(pwd)
        self.driver.find_element(*self.submit).click()
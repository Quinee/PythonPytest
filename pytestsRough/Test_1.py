import json
import time
import pytest
from pytestsRough.LoginPage import LoginPage

test_data_path = '../data/LoginPage.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]




class Test1:

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_list_item", test_list)
    def test_login_1(self, browserInstance,test_list_item):
        driver = browserInstance
        #driver.get('https://practicetestautomation.com/practice-test-login/')
        loginPage = LoginPage(driver)
        loginPage.getTitle()
        loginPage.login(test_list_item["username"],"Password123")
        time.sleep(5)
        # self.driver.maximize_window()
        # print('TITLE'+self.driver.title)
        #
        # print('CURL'+self.driver.current_url)
        # self.driver.find_element(By.ID,'username').send_keys('email@test.com')
        # msg = 'Success'
        #
        # assert 'Success' in msg
        #
        # # Static Dropdown
        # #dropdown = Select(driver.find_element(By.ID,''))


import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestHubSpot:

    @pytest.mark.parametrize("username, password", [
        ("un1@test.com", "pw1"),
        ("un2@test.com", "pw2"),
    ])
    def test_login(self,username,password):

        driver = webdriver.Chrome()

        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(1)# Wait

        driver.find_element(By.ID, "username").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)
        driver.close()


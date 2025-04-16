import csv
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def read_test_data():
    with open("test_data.csv", newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data[1:]  # Skip the header row


@pytest.mark.parametrize("username, password", read_test_data())
def test_login(username, password):
    driver = webdriver.Chrome()

    driver.get('https://practicetestautomation.com/practice-test-login/')

    driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    driver.close()
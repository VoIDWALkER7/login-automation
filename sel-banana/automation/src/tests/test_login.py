import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.dashboard import DashboardPage
import csv 

def load_test_data():
    '''CSV loaded'''
    data = []
    with open('data/test_data.csv', mode='r') as file: 
        csv_reader = csv.DictReader(file)
        for row in csv_reader: 
            data.append({"test_id": row["TestID"], "username":row["Username"], "password": row["Password"], "expected":row["Expected_Result"]})
    return data

@pytest.fixture
def driver(): 
    driver = webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/login")
    yield driver
    driver.quit()

@pytest.mark.parametrize("test_data", load_test_data())
def test_login_flow(driver, test_data): 
    login_page = LoginPage(driver)

    login_page.login(test_data["username"], test_data["password"])

    if test_data["expected"] == "Success":
        dashboard = DashboardPage(driver)
        assert "secure area" in dashboard.get_welcome_text()
    else: 
        assert "invalid" in login_page.get_error_message()

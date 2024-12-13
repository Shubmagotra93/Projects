import json
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def params():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    yield
    driver.close()

'''
# Fixture to load data from the YAML file
@pytest.fixture(scope="session")
def config_data():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)  # Returns the content as a dictionary
'''

"""
@pytest.fixture(scope="session")
def config_data():
    with open("config.json", "r") as file:
        return json.load(file)  # Returns the content as a dictionary

def test_example(params, config_data):
    # Use data from the YAML configuration
    url = config_data["url"]
    username = config_data["username"]
    password = config_data["password"]

    # Open the URL
    driver.get(url)
    time.sleep(2)

    # Test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(4)

"""
# Fixture to load test cases from JSON
@pytest.fixture(scope="session")
def load_test_data():
    with open("testData/config.json", "r") as file:
        return json.load(file)["test_cases"]



# Parameterize tests with data from the JSON file
@pytest.mark.parametrize("test_case", load_test_data())
def test_example(params, test_case):
    # Extract data for the current test case
    url = test_case["url"]
    username = test_case["username"]
    password = test_case["password"]

    # Open the URL
    driver.get(url)
    time.sleep(4)

    # Perform test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()
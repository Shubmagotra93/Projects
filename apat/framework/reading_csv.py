import json
import time
import csv
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
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    yield
    driver.close()

# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
def test_example(params):
    path ="/home/shubham/PycharmProjects/APAT/Framework/test_data.csv"
    test_data = get_csv_data(path)
    print(test_data)

    for data in test_data:
        username = data['username']
        password = data['password']

        # Enter username and password
        driver.find_element("name", "username").send_keys(username)
        driver.find_element("name", "password").send_keys(password)

        # Click login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Update locator as per the webpage

        # Perform validation after login (example: check for dashboard)
        # try:
        #     dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        #     assert dashboard.is_displayed(), "Dashboard not displayed, login failed!"
        #     print(f"Login successful for username: {username}")
        # except Exception as e:
        #     print(f"Login failed for username: {username}. Error: {str(e)}")

        # Navigate back to the login page for the next iteration
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()


@pytest.mark.smoke
def test_clickBooks(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()

@pytest.mark.smoke
def test_click_logout():
    pass

@pytest.mark.regression
def test_SignIn():
    pass

@pytest.mark.regression
@pytest.mark.login
def test_SignOut():
    pass

@pytest.mark.login
def test_function():
    pass
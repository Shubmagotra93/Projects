import logging
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@given(u'open browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    logger.info(f"Entered username: {username} and password: {password}")

@then(u'click login button')
def step_impl(context):
    driver.find_element(By.XPATH, "//button[@type='submit']").click()



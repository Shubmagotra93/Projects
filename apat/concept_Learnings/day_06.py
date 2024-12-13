import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
driver = webdriver.Chrome(options= options, service = s)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Explicit Wait
wait = WebDriverWait(driver, 10)

"""
web_element = {"by":By.XPATH, "value":"//button[text()='Submit']"}
print(By.ID)
print(type(By.XPATH))
print(web_element["by"])
print(web_element["value"])
"""

button_locator = (By.NAME, "username")
element = driver.find_element(By.NAME, "username")

# wait.until(EC.visibility_of_element_located(button_locator)).send_keys("Admin")
# wait.until(EC.visibility_of(driver.find_element(button_locator[0], button_locator[1]))).send_keys("Admin")
# wait.until(EC.visibility_of(driver.find_element(By.NAME, "username"))).send_keys("Admin")
# wait.until(EC.visibility_of(element))


# driver.find_element(button_locator[0], button_locator[1]).send_keys("Admin")









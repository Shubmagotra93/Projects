import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
driver.get("https://demoqa.com/alertsWindows")
driver.implicitly_wait(10)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
element = driver.find_element(By.XPATH, "(//ul//li[@id='item-1'])[2]")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
time.sleep(2)
"""
driver.find_element(By.CSS_SELECTOR, "#alertButton").click()
alert= Alert(driver)
print("alert text:", alert.text)
alert.accept()
"""
alert_btn = driver.find_element(By.CSS_SELECTOR, "#promtButton")
driver.execute_script("arguments[0].scrollIntoView();", alert_btn)
alert_btn.click()

a = wait.until(EC.alert_is_present())
print(a.text)
a.send_keys("Shubham")
time.sleep(1)
a.accept()

# alert= Alert(driver)
# print("alert text:", alert.text)
# time.sleep(1)
# alert.send_keys("Shubham")
# alert.accept()




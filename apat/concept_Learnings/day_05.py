import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.print_page_options import PrintOptions
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
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait = WebDriverWait(driver, 10)
dashboard_text = driver.find_element(By.XPATH, "//div[@class='oxd-brand-banner']")


# wait.until(EC.frame_to_be_available_and_switch_to_it(By.XPATH, ""))
# wait.until(EC.alert_is_present())
try:
    wait.until(EC.title_contains("Orange HRM"))
except:
    print("TimeoutException")
finally:
    print("In finally block")









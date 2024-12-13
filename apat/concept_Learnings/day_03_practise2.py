import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
driver = webdriver.Chrome(options= options, service = s)
driver.get("https://blazedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)


departure_city = driver.find_element(By.XPATH, "(//select[@class='form-inline'])[1]")
select = Select(departure_city)
select.select_by_visible_text("Boston")
destination_city = driver.find_element(By.XPATH, "(//select[@class='form-inline'])[2]")
select = Select(destination_city)
select.select_by_visible_text("London")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='submit'])[2]").click()
driver.find_element(By.ID, "inputName").send_keys("Test")
driver.find_element(By.ID, "address").send_keys("Pune VIMAAN NAGAR")
driver.find_element(By.ID, "city").send_keys("Pune")
driver.find_element(By.ID, "state").send_keys("UK")
driver.find_element(By.ID, "zipCode").send_keys("1213")
card_type = driver.find_element(By.XPATH, "//select[@id='cardType']")
select = Select(card_type)
select.select_by_visible_text("Diner's Club")
driver.find_element(By.ID, "creditCardNumber").send_keys("2313131")
driver.find_element(By.ID, "nameOnCard").send_keys("Test User")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
response = driver.find_element(By.XPATH, "//h1")
print(response.text)









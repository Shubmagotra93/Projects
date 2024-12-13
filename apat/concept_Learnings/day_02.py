import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless=new")
s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
driver = webdriver.Chrome(options= options, service = s)
# driver.get("https://demowebshop.tricentis.com/register")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)
print("Title is: ", driver.title)
print("Current URL is: ", driver.current_url)
"""
driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Prophix")
driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("User")
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("prophix2@mailinator.com")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Prophix@123")
driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Prophix@123")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='register-button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(3)
"""
# driver.find_element(By.XPATH, "//a[text()='Log in']").click()
login= driver.find_element(By.LINK_TEXT, "Log in")  # check for href attribute but added text is showing on display
print("href attribute for login is: ",login.get_attribute("href"))
print("class attribute for login is: ",login.get_attribute("class"))
print("text value is: ", login.text)
login.click()
email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.send_keys("prophix@mailinator.com")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Prophix@123")
login_btn = driver.find_element(By.XPATH, "(//input[@type='submit'])[2]")
print("tagname is: ", login_btn.tag_name)
login_btn.click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a[contains(text(),'Computers')])[1]").click()
driver.find_element(By.XPATH, "(//a[@title='Show products in category Notebooks'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='button'])[3]").click()
time.sleep(3)
try:
    added = driver.find_element(By.XPATH, "//p[@class='content']").text
    print(added)
except:
    print("Exception")
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "Shopping cart").click()

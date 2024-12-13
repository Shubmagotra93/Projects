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
driver.get("https://toolsqa.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.save_screenshot("/home/shubham/planami.png")
driver.find_element(By.ID, "accept-cookie-policy").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "ENROLL YOURSELF").click()
driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "last-name").send_keys("User")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("testuser@mailinator.com")
driver.find_element(By.CSS_SELECTOR, "#mobile").send_keys("0123456789")
country = driver.find_element(By.CSS_SELECTOR, "#country")
select = Select(country)
select.select_by_visible_text("India")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("New York")
driver.find_element(By.ID, "message").send_keys("Lorem Ipsum is simply dummy text of the printing and \
                                                        typesetting industry")
time.sleep(10)
driver.find_element(By.XPATH, "//button[text()='Send']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='navbar__tutorial-menu']").click()

time.sleep(2)
tutorials = driver.find_element(By.XPATH, "//span[text()='Back-End Testing Automation']")
action = ActionChains(driver)
action.move_to_element(tutorials).perform()
postman = driver.find_element(By.XPATH, "(//a[text()='Postman'])[3]")
print("href: ", postman.get_attribute("href"))
print(postman.tag_name)
print("text:", postman.text)
postman.click()
time.sleep(2)
postman_site = driver.find_element(By.CSS_SELECTOR, ".article-meta-data__title")
print(postman_site.text)



import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.print_page_options import PrintOptions
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

# you can get/set the page orientation — either PORTRAIT or LANDSCAPE.
# print_options = PrintOptions()
# print_options.orientation = "landscape" ## landscape or portrait

# print(driver.get_cookies())
# driver.delete_all_cookies()

driver.find_element(By.ID, "accept-cookie-policy").click()
# read_more = driver.find_element(By.XPATH, "//a[@href='/selenium-training?q=banner']")
# read_more.click()
# text = driver.find_element(By.CSS_SELECTOR, ".enroll__heading").text
# print(text)

# driver.back()
ele = driver.find_element(By.XPATH, "//a[@href='/categories']")
# print("Coordinates of element: ", ele.rect)
print("location of element: ", ele.location)

# driver.execute_script("arguments[0].scrollIntoView();", ele)
# driver.execute_script("window.scrollTo(225.140625,3628.859375);")
# driver.execute_script("window.scrollBy(225,3629)")

ActionChains(driver).scroll_to_element(ele).perform()
print("Text of element: ", ele.text)
time.sleep(3)
driver.execute_script("window.scrollTo(0, 0);")




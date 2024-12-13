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
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

# Select dropdown using Select class: sel = Select(element)
# sel.select_by_index(), select_by_visible_text(""), select_by_value("")
# driver.get("https://demowebshop.tricentis.com/books")
"""
element = driver.find_element(By.ID, "products-orderby")
select = Select(element)
time.sleep(1)
# select.select_by_index(3)
# select.select_by_visible_text("Created on")
# select.select_by_value("https://demowebshop.tricentis.com/books?orderby=5")
"""
# ActionChains class for mouse hover interactions: action = ActionChains(driver)
# move_to_element, context_click (right click), double_click, drag_and_drop
# driver.get("https://demowebshop.tricentis.com/")
"""
computers = driver.find_element(By.XPATH, "(//a[contains(text(),'Computers')])[1]")
action = ActionChains(driver)
action.move_to_element(computers).perform()
time.sleep(1)
action.context_click(computers).perform()
"""
# Javascript Alerts using Alert Class : alert = Alert(driver)
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")
"""
element =driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
action = ActionChains(driver)
action.double_click(element).perform()
time.sleep(2)
alert = Alert(driver)
print("alert text: ", alert.text)
alert.accept()
# alert.dismiss()
"""
action = ActionChains(driver)
action.move_to_element(computers).perform()

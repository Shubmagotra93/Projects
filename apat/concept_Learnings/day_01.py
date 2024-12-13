import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_Service
from selenium.webdriver.firefox.service import Service as firefox_Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
"""
options = webdriver.ChromeOptions()  #from webdriver/chrome/options.py file
options.add_experimental_option("detach", True) #from webdriver/chromium/options.py file
# options.add_argument("--headless=new")  #from webdriver/common/options.py file
# chrome = chrome_Service("/home/shubham/Shubham_QA/Projects/apat/chromedriver") #from webdriver/chrome/service.py file
# driver = webdriver.Chrome(options= options, service=chrome) #from webdriver/chrome/webdriver.py file
driver = webdriver.Chrome(options= options, service=chrome_Service(ChromeDriverManager().install())) #from webdriver/chrome/webdriver.py file
"""
# Run with Firefox
firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
firefox = firefox_Service("/home/shubham/Shubham_QA/Projects/apat/geckodriver")
firefox_binary_path = "/usr/bin/firefox"  #use which command to find path >> "which firefox"
firefox_options.binary_location = firefox_binary_path  # from webdriver/firefox/options.py
# driver = webdriver.Firefox(options=firefox_options, service= firefox)
driver = webdriver.Firefox(options=firefox_options, service=firefox_Service(GeckoDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
print("Title is: ", driver.title)
print("Current URL is: ", driver.current_url)

driver.find_element(By.NAME, value = "username").send_keys("Admin")  # old way of writing locators
driver.find_element(By.NAME,"password").send_keys("admin123") # preferred way
driver.find_element("xpath","//button[@type='submit']").click() # incorrect way
# driver.find_element(by="name", value="username") # also works

time.sleep(2)
driver.close()
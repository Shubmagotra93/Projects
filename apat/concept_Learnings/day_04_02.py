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
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
time.sleep(2)

# frames
"""
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
ele = driver.find_element(By.ID, "tinymce")
print(ele.text)
driver.switch_to.default_content()
outer_ele= driver.find_element(By.TAG_NAME, "h3")
print(outer_ele.text)
"""
#top frame
top_frame = driver.find_element(By.XPATH, "//frame[@src='/frame_top']")
driver.switch_to.frame(top_frame)
print("switched to top frame")

#middle frame
middle_frame = driver.find_element(By.XPATH, "//frame[@src= '/frame_middle']")
driver.switch_to.frame(middle_frame)
print("switched to middle frame")
middle_text = driver.find_element(By.XPATH, "//div[@id='content']")
print(middle_text.text)

#switch to top
driver.switch_to.parent_frame()
print("again switched to top frame means parent of middle")

#right frame
right_frame = driver.find_element(By.XPATH, "//frame[@src= '/frame_right']")
driver.switch_to.frame(right_frame)
print("switched to right frame")

driver.switch_to.default_content()
print("out of frame")


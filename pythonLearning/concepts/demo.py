import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://abcinc.zennero.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, value="username").send_keys("ABCINCADMIN")
driver.find_element(By.ID, value="password").send_keys("WR@8517!#uI01")
driver.find_element(By.XPATH, value="//button[@type='submit']").click()
print(driver.current_url)
ele = driver.find_element(By.XPATH, value="//h6[contains(text(), 'Volume By Object')]")
wait = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Volume By Object')]")))
wait = WebDriverWait(driver, 60).until(EC.visibility_of(ele))

all_links = driver.find_elements(By.TAG_NAME, value="a")
print(len(all_links))
for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken links: {href} and status code{response.status_code}")
driver.quit()


# //div/div[1]/input - traversing through xpath
# div div:nth-child(2) input - traversing through css  # remove index [1]   with :nth-child(1)
# //button[text()='Save'] - xpath based on text
# Select from dropdown using Select
# dd= Select(driver.find_element(""))
# dd.select_by_index()

# dd = Select(driver.find_elements(By.XPATH, value= "//input[@class='test']"))

# windows = driver.window_handles
# driver.switch_to.window(windows[1])
# and then perform operations
# driver.switch_to.window(windows[0])
# driver.execute_script("arguments[0].scrollIntoView();", self.super_admin.get_from_date())
# ActionChains class is used to handle mouse interations like drag and drop, doubleclick, context_click(right click)
# action = ActionChains(driver)
# action.move_to_element(ele).click().perform() # perform method helps in terminating the actions


driver.switch_to.frame("value")
driver.execute_script(window)
driver.switch_to.default_content()
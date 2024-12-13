import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
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
driver.get("https://toolsqa.com/")
driver.maximize_window()


# Windows handling

# Access each dimension individually
# width = driver.get_window_size().get("width")
# height = driver.get_window_size().get("height")
# print(width, height)

# Access each dimension individually
# x = driver.get_window_position().get('x')
# y = driver.get_window_position().get('y')
# print(x, y)

# Set window position
# driver.set_window_position(0, 0)


# Set window size
# driver.set_window_size(1024, 768)

errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, 20, poll_frequency=.20, ignored_exceptions=errors)
# Store the ID of the original window
original_window = driver.current_window_handle
print("original_window: ", original_window)

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

# Click the link which opens in a new window
ele = driver.find_element(By.XPATH, "(//a[@href='https://demoqa.com'])[1]")
ele.click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

print("after opening new window: ", driver.window_handles)

# Loop through until we find a new window handle
for child_window in driver.window_handles:
    if child_window != original_window:
        driver.switch_to.window(child_window)
        break

# [driver.switch_to.window(child_window) for child_window in driver.window_handles if child_window != original_window][0]

# Wait for the new tab to finish loading content
wait.until(EC.title_is("DEMOQA"))
driver.save_screenshot("./demoqapage.png")
print(driver.title)

element = driver.find_element(By.XPATH, "//h5[text()='Elements']")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.screenshot("./elementscreenshot.png")
driver.execute_script('return arguments[0].innerText', element)
element.click()

# Switched back to main window
driver.switch_to.window(original_window)

# Fetch text on main window
ele = driver.find_element(By.CSS_SELECTOR, ".new-training__heading")
print(ele.text)

elem = driver.find_element("name", 'p')  # Find the search box
wait.until(lambda d: revealed.is_displayed())










from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def params():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    yield
    driver.close()


# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)

# a = ("username, password",[("Admin", "admin123"), ("invalid_user", "admin123"), ("Admin", "wrongpassword"), ("", ""),])


def test_login(params, username, password):
    # Locate and interact with username field
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver.find_element(By.NAME, "password")
    #password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()





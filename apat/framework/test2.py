from allure_commons.types import AttachmentType
from requests_unixsocket import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure

@pytest.fixture()
def test_verifyURL(request):
    # to print each test case name when it got failed
    test_name = request.node.name
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://blazedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name, attachment_type=AttachmentType.PNG)
        request.session.testsfailed = before_failed  # Reset the testsfailed count
    driver.close()


# @pytest.mark.regression
# @pytest.mark.login
@allure.feature("Booking Feature")
@allure.story("Flight booking")
@allure.title("Select source and destination city")
def test_select_city(test_verifyURL):
    expected_url = "https://blazedemo.com/"
    assert expected_url == driver.current_url, "Incorrect URL"
    departure_city = driver.find_element(By.XPATH, "(//select[@class='form-inline'])[1]")
    select = Select(departure_city)
    select.select_by_visible_text("Boston")
    destination_city = driver.find_element(By.XPATH, "(//select[@class='form-inline'])[2]")
    select = Select(destination_city)
    select.select_by_visible_text("London")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    flight_text = driver.find_element(By.TAG_NAME, "h3").text
    assert flight_text == "Flights from Boston to London:"
    # try:
    #     assert flight_text == "Flight from Boston to London:"
    # except AssertionError as e:
    #     allure.attach(driver.get_screenshot_as_png(), name= "Screenshot_on_Failure", attachment_type=AttachmentType.PNG)
    #     raise e
    # finally:
    #     print("Executed try except block")

@allure.feature("Booking Feature")
@allure.story("Flight booking")
@allure.title("Select Flight from various options")
def test_select_flight(test_verifyURL):
    test_select_city(test_verifyURL)
    driver.find_element(By.XPATH, "(//input[@type='submit'])[2]").click()

@allure.feature("Booking Feature")
@allure.story("Flight booking")
def test_enter_details(test_verifyURL):
    test_select_flight(test_verifyURL)
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

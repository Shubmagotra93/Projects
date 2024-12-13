import time
from linecache import clearcache
from webbrowser import open_new_tab, open_new

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/market-data/oi-spurts")
driver.maximize_window()
driver.implicitly_wait(10)

stocks_list= []
rows = driver.find_elements(By.XPATH, value="//tbody//tr")
for row in rows[0:]:
    cells = row.find_elements(By.TAG_NAME, value="td")
    if float(cells[4].text) >= float(7):
        symbol = cells[0].text
        stocks_list.append(symbol)
    # if len(stocks_list) == 30:
    #     break
print("Stocks List with OI data: ",stocks_list )
# stocks = ', '.join(stocks_list)
print(len(stocks_list))

driver.close()
driver = webdriver.Chrome()
#NSE TOP GAINERS/LOOSERS
driver.get("https://www.nseindia.com/market-data/top-gainers-losers")
driver.maximize_window()
driver.implicitly_wait(10)
print(len(stocks_list))
wait = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.ID, "index0")))
select_index = driver.find_element(By.ID, value="index0")
select = Select(select_index)
select.select_by_visible_text("F&O Securities")

#TOP GAINERS
top_gainers= []
rows = driver.find_elements(By.XPATH, value="//tbody//tr")
for row in rows[0:]:
    cells = row.find_elements(By.TAG_NAME, value="td")
    if cells[6].text >= str(2):
        symbol = cells[0].text
        top_gainers.append(symbol)
print("TOP GAINERS: ", top_gainers)

#TOP LOSERS
loser_tab = driver.find_element(By.XPATH, value="//a[@id='LOSERS']")
loser_tab.click()

top_losers= []
rows = driver.find_elements(By.XPATH, value="//tbody//tr")
for row in rows[0:]:
    cells = row.find_elements(By.TAG_NAME, value="td")
    if cells[6].text >= str(-2):
        symbol = cells[0].text
        top_losers.append(symbol)
print("TOP LOSERS: ", top_losers)

# Compare stocks in NSE Spurt with the top gainers/losers list
final_stocks = [symbol for symbol in stocks_list if symbol in top_gainers or symbol in top_losers]
# print("FINAL STOCKS: ",final_stocks)
stocks = ', '.join(final_stocks)
print("Stocks for trade:", stocks)

#tradingview action
driver.get("https://in.tradingview.com/")
signin_link = driver.find_element(By.XPATH, value="//button[@class='tv-header__user-menu-button tv-header__user-menu-button--anonymous js-header-user-menu-button']")
signin_link.click()
signin_button = driver.find_element(By.XPATH, value="//div[@role='menu']/button[1]")
signin_button.click()
google_link = driver.find_element(By.XPATH, value="//button[@name='Email']")
google_link.click()
driver.find_element(By.ID, value="id_username").send_keys("shubmagotra93@gmail.com")
driver.find_element(By.ID, value="id_password").send_keys("Tradingview@#2274")
driver.find_element(By.XPATH, value= "//button[@data-overflow-tooltip-text='Sign in']").click()
time.sleep(5)
# clicking watchlist icon
watchlists_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-name='watchlists-button']"))
)
watchlists_button.click()
# Wait and click the 4th menu item
menu_item = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@data-role='menuitem'])[4]"))
)
menu_item.click()
# Wait and click the 'yes' button
yes_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@name='yes']"))
)
yes_button.click()
# adding stocks list from NSE Spurt site
add_symbol = driver.find_element(By.XPATH, value=" //button[@data-tooltip='Add symbol']")
wait = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@data-tooltip='Add symbol']")))
add_symbol.click()
driver.find_element(By.XPATH, value="//input[@placeholder='Search']").send_keys(stocks + Keys.ENTER)

time.sleep(5)



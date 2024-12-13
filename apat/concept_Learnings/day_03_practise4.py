import time

from fontTools.ttLib.tables.D__e_b_g import table_D__e_b_g
from numpy.distutils.conv_template import header
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
driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()

time.sleep(3)
table = driver.find_element(By.CSS_SELECTOR, ".table.table-striped")

# handling dynamic tables
# Get all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterate through each row
row_lst = []
for row in rows:
    headers = row.find_elements(By.TAG_NAME, "th")
    columns = row.find_elements(By.TAG_NAME, "td")


    column_lst=[]
    for header in headers:
        data_header = header.text
        column_lst.append(data_header)
    for column in columns:
        data = column.text
        column_lst.append(data)
    """
    column_lst = []
    for header, column in zip(headers, columns):
        column_lst.append(header.text)
        column_lst.append(column.text)
    """
        # column_lst = [header.text for header in headers] + [column.text for column in columns]

    row_lst.append(column_lst)

# print(row_lst)
for row in row_lst:
    print(row)



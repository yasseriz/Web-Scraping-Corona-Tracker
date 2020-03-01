from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import json
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.common.exceptions import NoSuchElementException
from pandas.io.json import json_normalize
import urllib.request
import requests
import csv
import time
import calendar

url = 'https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/'

driver = webdriver.Chrome()
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, features='lxml')
time.sleep(2)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    except WebDriverException:
        return False
    return True

num = soup.findAll('h4')
dateList = []
for link in num:
    dateList.append(link.get_text())
monthName = list(calendar.month_name[1:])
print(type(monthName))

cleanedData = []
test = driver.find_element_by_xpath('//*[@id="mvp-content-main"]/ul[3]').text
print(test)
# dateName = driver.find_element_by_xpath('//*[@id="mvp-content-main"]/h4[1]')
# //*[@id="mvp-content-main"]/h4[1]
# //*[@id="mvp-content-main"]/h4[2]
# //*[@id="mvp-content-main"]/ul[3]/li[1]/text()[1]
# //*[@id="mvp-content-main"]/ul[3]/li[2]/text()[1]
# //*[@id="mvp-content-main"]/ul[4]/li[1]/text()[1]

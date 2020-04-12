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
from datetime import datetime

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
time.sleep(5)
num = soup.findAll('h4')
dateList = []
for link in num:
    # print(link)
    dateList.append(link.get_text())
monthName = list(calendar.month_name[1:])
# print(dateList)
# print(monthName)
presentDates = []
for nameofmonth in monthName:
    for month in dateList:
        if nameofmonth in month:
            presentDates.append(month)
presentDates.sort()
print(presentDates)
noofdays = len(presentDates)
# print(noofdays)
cleanedData = []


dateCounter = 0
for i in range(3, noofdays+3):
    cleanedData.append(presentDates[dateCounter])
    temp = driver.find_element_by_xpath('//*[@id="mvp-content-main"]/ul['+str(i)+']').text
    tempNew = temp.splitlines()
    for sentence in tempNew:
        cleanedData.append(sentence)
    dateCounter+=1
df = pd.DataFrame(cleanedData)
filename = datetime.today().strftime('%Y-%m-%d')

df.to_csv(str(filename)+'.csv', index=False)


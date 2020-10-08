
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:25:09 2020

@author: enesy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pandas as pd
import time
import sys

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import re
#%matplotlib inline

from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def act(driver):
    actions = ActionChains(driver) 
    nextPage=driver.find_element_by_class_name("pagination__next")
    actions.click(on_element=nextPage) 
    actions.perform()
    time.sleep(10)

page=4
delay=5

chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(5)
time.sleep(delay)

driver.maximize_window()
driver.get('https://www.nasdaq.com/market-activity/stocks/tsla/news-headlines')
time.sleep(delay)

try:
    popup=driver.find_element_by_xpath("//button[@id='_evh-ric-c']")
    #.find_element_by_id("gb_23")
    if popup is not None:
        popup.click()
except:
    print("Unexpected error:", sys.exc_info()[0])

    


#Get links
newsLinks=[]
recentList = driver.find_elements_by_xpath("//div[@class='symbol-back-to-overview']") 
for list in recentList :
    driver.execute_script("arguments[0].scrollIntoView();", list )
    
for i in range(1,page+1):
    lnk=[]
    lnk=[links.get_attribute("href") for links in driver.find_elements_by_xpath('//a[@class="quote-news-headlines__link"]')]
    newsLinks.append(lnk)
    #act(driver)
    time.sleep(delay)
    
    try:
        element=WebDriverWait(driver,delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "pagination__next")))
        act(driver)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    #driver.find_element_by_class_name("pagination__next").click();
    #try:
    #    #nextPage = driver.find_element_by_class_name("pagination__next")
    #    nextPage=driver.find_element_by_xpath("//button[@class='pagination__next']")
    #    print("--------------------------------------------------------------------------------------------------")
    #    print("klik: ",nextPage)
    #    time.sleep(delay)
    #    nextPage.click()
    #except ElementClickInterceptedException:
    #    time.sleep(delay)
    #    nextPage.click()


#pagination-news-headlines--pagination__next---symbol-back-to-overview
    

news=np.array(newsLinks)
xNews=np.array(news).flatten()
xNews[0]


#url="https://www.nasdaq.com/articles/us-stocks-tech-bank-shares-drive-wall-street-higher-2020-09-28"
#html=urlopen(url)
#soup=BeautifulSoup(html,"html.parser")
#print(soup.get_text())

    
    

text=[]
dateTime=[]
for links in xNews:
    r=requests.get(links,headers=headers).text
    soup=BeautifulSoup(r,'lxml')
    div=soup.find("div",class_="body__content")
    p=div.find_all("p")
    time=soup.find("time",class_="timestamp__date")
    tempStr=""
    for ps in p:
        tempStr+=ps.text
    text.append(tempStr)
    dateTime.append(time.text)
    
"""    
print("text: ",text[0])
print("date: ",dateTime[0])
"""

dfText=pd.DataFrame(text)
dfDates=pd.DataFrame(dateTime)
df=pd.concat([dfDates,dfText],ignore_index=True,axis=1)
df.columns=["Dates","Text"]
df.to_csv("NasdaqNews.csv",encoding="utf-8")
print(df.tail())
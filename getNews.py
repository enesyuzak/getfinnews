
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:25:09 2020

@author: enesy
"""
#import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#import web scrapy librarires
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests

#import data libraries
import pandas as pd
import numpy as np

#import system libraries
import time
import datetime
import sys
import random
import io
import math


#headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

#Functions:
#click event
def act(driver):
    actions = ActionChains(driver) 
    nextPage=driver.find_element_by_class_name("pagination__next")
    actions.click(on_element=nextPage) 
    actions.perform()
    time.sleep(10)

def log(logMessage):
    file1=io.open("log.txt","a",encoding="utf-8")
    file1.writelines(st+"\n")
    file1.close()

def WriteToFile(filePath,text):
    file1=io.open(filePath,"a",encoding="utf-8")
    file1.writelines(text+"\n")
    file1.close()
    
#consts
page=500
delay=2

#chrome driver options
chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(5)
#driver.maximize_window()
driver.get('https://www.nasdaq.com/market-activity/stocks/tsla/news-headlines')
time.sleep(delay)

#if there is a popup close it
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

startDate=datetime.datetime.now()
for i in range(1,page+1):
    
    lnk=[]
    lnk=[links.get_attribute("href") for links in driver.find_elements_by_xpath('//a[@class="quote-news-headlines__link"]')]
    newsLinks.append(lnk)
    time.sleep(random.randrange(0,10))
    
    try:
        element=WebDriverWait(driver,delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "pagination__next")))
        act(driver)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
#calculate running time
endDate=datetime.datetime.now()
minute=divmod((endDate-startDate).total_seconds(),60)[0]
minute=math.floor(minute)
second=divmod((endDate-startDate).total_seconds(),60)[1]
st="Lİnklerin yüklenme süresi: "+str(minute)+" dakika "+str(second)+"saniye sürmüştür"
#write log
log(st)
#pagination-news-headlines--pagination__next---symbol-back-to-overview

news=np.array(newsLinks)
xNews=np.array(news).flatten()
for i in xNews:
    WriteToFile("links.txt",i)


#url="https://www.nasdaq.com/articles/us-stocks-tech-bank-shares-drive-wall-street-higher-2020-09-28"
#html=urlopen(url)
#soup=BeautifulSoup(html,"html.parser")
#print(soup.get_text())


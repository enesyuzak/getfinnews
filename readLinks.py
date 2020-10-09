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

import pandas as pd
import numpy as np
import random
import time

#headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

#reading links from file
file1 = open(r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews\links.txt', 'r')
Lines=file1.readlines()
newsLinks=[]
for l in Lines:
    newsLinks.append(l)

news=np.array(newsLinks)
xNews=np.array(news).flatten()



chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\chromedriver', chrome_options=chrome_options)

"""
driver.get(url)
html1 = driver.page_source
soup = BeautifulSoup(html1, 'lxml')
a = soup.find('div', 'body__content')
p=a.find_all("p")
tempStr=""
for ps in p:
    tempStr+=ps.text
"""


text=[]
dateTime=[]
for links in xNews[0:3]:
    try:
        print("links: ",links)
        r=requests.get(links,headers=headers)
        time.sleep(4)
        soup=BeautifulSoup(r.content,'lxml')
        div=soup.find("div",class_="body__content")
        p=div.find_all("p")
        time1=soup.find("time",class_="timestamp__date")
        tempStr=""
        for ps in p:
            tempStr+=ps.text
        text.append(tempStr)
        dateTime.append(time1.text)
    except Exception as e:
        print("Error: ",e)
        pass
    #time.sleep(random.randrange(0,6))



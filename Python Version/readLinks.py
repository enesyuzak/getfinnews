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
import math
import random
import time
import datetime
import io

#functions
def WriteToFile(filePath,text):
    file1=io.open(filePath,"a",encoding="utf-8")
    file1.writelines(str(text)+"\n")
    file1.close()

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




text=[]
dateTime=[]
lnk=[]
startDate=datetime.datetime.now()
for links in xNews[0:5]:
    try:
        print("links: ",links)
        driver.get(links)
        time.sleep(random.randrange(0,10))
        html1 = driver.page_source
        soup = BeautifulSoup(html1, 'lxml')
        div = soup.find('div', 'body__content')
        p=div.find_all("p")
        print("p alındı")
        time1=soup.find("time",class_="timestamp__date")
        tempStr=""
        for ps in p:
            tempStr+=ps.text
        text.append(tempStr)
        dateTime.append(time1.text)
        lnk.append(links)
    except Exception as e:
        WriteToFile("logLinks.txt",e)
        print("Error: ",e)
        pass
startDate=datetime.datetime.now()    
endDate=datetime.datetime.now()
minute=divmod((endDate-startDate).total_seconds(),60)[0]
minute=math.floor(minute)
second=divmod((endDate-startDate).total_seconds(),60)[1]
st=str(minute)+" dakika "+str(second)+"saniye sürmüştür"
sta="işlem bitiş zamanı: "+startDate
fns="işlem bitiş zamanı: "+endDate
elapsed="toplam işlem süresi: "+st
WriteToFile("logLinks.txt",sta)
WriteToFile("logLinks.txt",fns)
WriteToFile("logLinks.txt",st)

dfText=pd.DataFrame(text)
dfDates=pd.DataFrame(dateTime)
dfLinks=pd.DataFrame(lnk)
df=pd.concat([dfDates,dfText,dfLinks],ignore_index=True,axis=1)
df.columns=["Dates","Text","Link"]
df.to_csv("TeslaNews.csv",encoding="utf-8")
print(df.tail())


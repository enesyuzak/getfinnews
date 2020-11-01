# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:31:18 2020

@author: enesy
"""
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import io
import time

class Mail:
    def send_mail(subject,message,plain="plain"):
        
        msg=MIMEMultipart()
        msg['from']="enesyuzak@yandex.com"
        msg['to']="enesyuzak@gmail.com"
        msg['subject']=subject
        
        msg_setting=MIMEText(message,plain)
        msg.attach(msg_setting)
        
        try:
            mail=smtplib.SMTP("smtp.yandex.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("enesyuzak@yandex.com","yanEg-167010")
            mail.sendmail(msg["from"],msg["to"],msg.as_string())
            print("Mail gönderildi")
            
        except:
            print("Hata: ", sys.exc_info()[0])
    
        finally:
            mail.close()

class File :
    def log(logMessage):
        file1=io.open("log.txt","a",encoding="utf-8")
        file1.writelines(logMessage+"\n")
        file1.close()
    
    def WriteToFile(filePath,text):
        file1=io.open(filePath,"a",encoding="utf-8")
        file1.write(text)
        file1.close()
    
    def ReadFromFile(fileName):
        with open(fileName,"r",encoding='utf-8') as reader:
            x=reader.readlines()
        reader.close()
        return x

class Scrap:
    def act(driver):
        actions = ActionChains(driver) 
        nextPage=driver.find_element_by_class_name("pagination__next")
        actions.click(on_element=nextPage) 
        actions.perform()
        time.sleep(10)
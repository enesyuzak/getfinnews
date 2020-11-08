# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:39:09 2020

@author: enesy
"""
from selenium.webdriver.common.action_chains import ActionChains
import io
import time



class selenium:
    def act(driver):
        actions = ActionChains(driver) 
        nextPage=driver.find_element_by_class_name("pagination__next")
        actions.click(on_element=nextPage) 
        actions.perform()
        time.sleep(10)
        
class logs:
    def log(logMessage):
        file1=io.open("log.txt","a",encoding="utf-8")
        file1.writelines(logMessage+"\n")
        file1.close()
    
    def WriteToFile(filePath,text):
        file1=io.open(filePath,"a",encoding="utf-8")
        file1.write(text)
        file1.close()
    
    def ReadFromFile(fileName):
        with open(fileName,"r") as reader:
            x=reader.read()
        reader.close()
        return x
    
    

        
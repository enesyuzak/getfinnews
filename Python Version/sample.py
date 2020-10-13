# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:41:36 2020

@author: enesy
"""
import numpy as np
from task import logs as l
import sys
sys.path.insert(1, r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews') 


from task import logs as l

path=r"C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews\pre_links2.txt"
a=l.ReadFromFile(path)
a=np.array(a)
a=a.flatten()

x=[]
for i in a:
    x.append(i)
  
news=np.array(x)
news=np.reshape(news,-1)
 
for i in news:
    l.WriteToFile("cleaned_text.txt",str(i))
    #print(i)
    #print("\n")

#log1=l.log("denemeler")
#log2=l.WriteToFile("bla.txt","text")


c=l.ReadFromFile("cleaned_text2.txt")
z=[]
for i in c:
    z.append(i)



for x in z:
    l.WriteToFile("links_last.txt",x)

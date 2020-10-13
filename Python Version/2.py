# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:57:59 2020

@author: enesy
"""

import numpy as np
import sys
sys.path.insert(1, r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews') 
sys.path.insert(1, r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews\Python Version') 
from task import logs as l

path=r"C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews\deneme.txt"
a=l.ReadFromFile(path)
print(type(a))
b=a.split(",")
for link in b:
    l.WriteToFile(r'C:\Users\enesy\OneDrive\Okul\Tez\Codes\tez\getfinnews\cleanedData.txt',str(link))

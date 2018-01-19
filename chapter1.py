# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:51:14 2018

@author: PRAVIN
"""

from datetime import datetime 
import time
import random


odds=[1,3,5,7,9,11,13,15,17,21,23,25,27,
        29,31,33,35,37,41,4,45,47,
        49,51,53,55,57,59]

for i in range(5):
    time_now = datetime.today().minute
    if time_now in odds:
        print("this minutes seems little Odd")
    else:
        print("This minute seems Even")
    wait_time=random.randint(1,60)
    time.sleep(wait_time)
    
    
        
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:17:45 2017

@author: PRAVIN
"""

'''from datetime import datetime
odds = [1,3,5,7,9,11,13,15,17,21,23,25,27,
        29,31,33,35,37,41,4,45,47,
        49,51,53,55,57,59 ]
right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute")    
    
'''
from datetime import datetime
import time

odds=[1,3,5,7,9,11,13,15,17,21,23,25,27,
        29,31,33,35,37,41,4,45,47,
        49,51,53,55,57,59]
for i in range(5):    
    time_now= datetime.today().minute
    time.sleep(5)    
    if time_now in odds:
        print("This minute seems little Odd")
    else:
        print("Not an Odd Minute")
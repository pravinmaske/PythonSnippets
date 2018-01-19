# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:51:41 2017

@author: PRAVIN
"""

from datetime import datetime

today = datetime.today()

if today == 'sunday':
    print("Recover.")
    
elif today =='saturday':
    print("Party.. Party.. Party")
else:
    print("Work  work  work")
    
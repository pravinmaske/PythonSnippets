# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:54:04 2018

@author: PRAVIN
"""


vowels =['a','e','i','o','u']
found=[]
word ="Milliways"
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(letter)
            
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:56:00 2018

@author: PRAVIN
"""

vowels =['a','e','i','o','u']
found=[]
word =input("Enter the word to searcg for vowels :")
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(letter)
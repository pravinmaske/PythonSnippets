# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:12:21 2018

@author: PRAVIN
"""

vowels=set('aeiou')
word=input("Please enter word to find vowels \t\n")
'''found=set(word)

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)'''
letter=vowels.intersection(set(word))
print(letter)
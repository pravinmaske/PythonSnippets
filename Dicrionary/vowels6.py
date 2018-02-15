# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:00:58 2018

@author: PRAVIN
"""

vowels=['a','e','i','o','u']
word=input("Enter a word to know the vowels\n\t")
found={}
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k,'found ',v,' times')
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:03:18 2018

@author: PRAVIN
"""

phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)


new_phrase=''.join(plist[1:3])
new_phrase= new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])
#new_phrase=''.join(plist[1:3:1]) +" " +''.join(plist[4:5:1])+''.join(plist[7:5:-1])
#plist=list(new_phrase)
print(plist)
print(new_phrase)
#on tap
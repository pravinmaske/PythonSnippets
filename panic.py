# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:43:30 2018

@author: PRAVIN
"""
'''
phrase="Don't Panic!"
plist=list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
print(plist)
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
new_phrase=''.join(plist)
print(plist)
print(new_phrase)
'''
phrase = "Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

plist.pop(0)
plist.pop(2)
plist.extend([plist.pop(),plist.pop()])

plist.insert(2,plist.pop(3))
new_phrase= ''.join(plist)
print(plist)
print(new_phrase)

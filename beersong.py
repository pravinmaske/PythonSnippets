# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:14:43 2018

@author: PRAVIN
"""

word="Bottles"
for beer_num in range(3,0,-1):
    print(beer_num,word,"of Beer on the wall.")
    print(beer_num,word,"of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num= beer_num-1
        if new_num == 1:
            word="Bottle"
        print(new_num,word,"of beer on the wall.")
    print()
        
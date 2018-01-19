# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:56:24 2018

@author: PRAVIN
"""

paranoid_android="Parvin, the Paranoid Android"
letters=list(paranoid_android)
for char in letters[:6]:
    print('\t',char)
for char in letters[-7:]:
    print('\t'*2,char)
for char in letters[12:20]:
    print('\t'*3,char)
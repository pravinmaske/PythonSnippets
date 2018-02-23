# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:00:31 2018

@author: PRAVIN
"""

def double(arg):
    print('before :',arg)
    arg= arg*2
    print('After :',arg)

def change(arg):
    print('Before :',arg)
    arg.append('Make change')
    print('After :',arg)

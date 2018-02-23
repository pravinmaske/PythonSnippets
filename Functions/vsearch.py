# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:36:38 2018

@author: PRAVIN
"""
'''
def search4Vowels(word):
     display any vowels found in an asked-for word
    vowels=set('aeiou')
    #word=input("Please enter a word to search vowels")
    found=vowels.intersection(set(word))
    #for latter in found:
     #   print(latter)
    return bool(found)    '''
    
def search4Vowels(phrase):
    vowels=set('aeiou')
    return vowels.intersection(set(phrase))
    
def search4Letters(phrase:str,letter:str='aeiou') ->set:
    """Returns set of the letters found in 'phrase' """
    return set(letter).intersection(set(phrase))
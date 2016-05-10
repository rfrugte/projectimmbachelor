# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:56:12 2016

@author: gebruiker
"""

def list_to_txtfile(to_write):
    '''Writes a list to a text file.'''
    with open("testfile.txt", "w",encoding="utf-8") as text_file:
        for item in to_write:
            text_file.write(item + "\n\n")
 
def print_list_with_enter(to_print):
    '''Print list separated by enters'''
    for item in to_print:
        print(item + "\n\n")  
        
def contains_number(to_search):
    return sum(char.isdigit() for char in to_search)        
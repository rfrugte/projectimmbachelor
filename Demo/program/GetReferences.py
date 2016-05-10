# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:30:24 2016

@author: Jordi
"""

import rd
import codecs
import os
from bs4 import BeautifulSoup
from collections import defaultdict

def open_location():
    '''Changes the working directory and loops through all files with extension "htm"  '''
    os.chdir("..")
    os.chdir(os.getcwd() + "/HTM")
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".htm"):
            get_raw_text(filename)
        else:
            continue
        
def get_raw_text(filename):
    '''Import the files and gets the raw text in lowercase, this makes it easier to search'''   
    htm_file = codecs.open(filename, "r","utf-8")
    soup = BeautifulSoup(htm_file, 'html.parser')
    raw_text= soup.get_text().lower()
    get_references(raw_text,filename)

def get_references(raw_text,filename):
    '''Takes all lines after the last occurrence of the searched query '''    
    last_instance= raw_text.rfind('references\n')
    references = raw_text[last_instance:]
    listed_references_cluttered=references.splitlines()
    remove_clutter(listed_references_cluttered, filename)
   
def remove_clutter(listed_references_cluttered, filename):
    if "dict_references" not in globals():
        dict_references={}
    listed_references=[]
    '''Deletes the first instance in the list. It does this because the first item is not a reference but the search query'''
    del listed_references_cluttered[0]
    '''Removes the clutter from the reference list.(empty strings, pagenumbers,language tag) and puts them in a dict '''
    for item in listed_references_cluttered:
        if item and not item.isdigit()==True and not item=="en":
            listed_references.append(item)
    dict_references.update({filename:(listed_references)}) 
    global dict_references       
    '''write the references to text file in working directory'''        
    #rd.list_to_txtfile(listed_references)
    '''print the references in the console '''
    #rd.print_list_with_enter(listed_references)
            
def execute():
    open_location()   
      
'''This begins the retrievel of the references in the "reference" section'''
execute()
          



             
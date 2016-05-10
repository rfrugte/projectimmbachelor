# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:43:27 2016

@author: gebruiker
"""

import rd
import codecs
import os
import xlrd

def open_location():
    '''Changes the working directory and loops through all files with extension "xlsx"  '''
    os.chdir("..")
    os.chdir(os.getcwd() + "/Results")    
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".xlsx"):
            read_lines(filename)
        else:
            continue
    return(filename) 
    
def read_lines(filename):
    '''Converts the rows in a xlsx file into a list '''
    listed_footnotes =[]
    footnotes = xlrd.open_workbook(filename)
    sheet_name= footnotes.sheet_by_index(0)
    number_of_rows = sheet_name.nrows
    for i in range(0,number_of_rows):
        listed_footnotes.append(sheet_name.row_values(i)[0].strip())
    first_classification(listed_footnotes)    

def first_classification(listed_footnotes):
    most_likely_relevant=[]
    likely_relevant=[]
    likely_not_relevant=[]
    for footnote in listed_footnotes:
        if "://" in footnote:
            most_likely_relevant.append(footnote)
        elif rd.contains_number(footnote)>=3:
            likely_relevant.append(footnote)
        else:
            likely_not_relevant.append(footnote)
            
    global most_likely_relevant, likely_relevant ,likely_not_relevant     
            

    
def execute():
    open_location()
    
execute()   
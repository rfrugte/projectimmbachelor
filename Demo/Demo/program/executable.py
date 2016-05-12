# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:48:12 2016

@author: gebruiker
"""
import GetReferences
import GetFootnotes
import ProcessFootnotes
import dictionary
import rd

get_references = True
get_footnotes = False
process_footnotes = True

def run():
    
    if get_references:
        info_references = GetReferences.execute()
        
    if get_footnotes:
        GetFootnotes.execute()
        
    if process_footnotes:   
        info_footnotes = ProcessFootnotes.execute()
        
    check =dictionary.execute(info_references, info_footnotes) 
    global check
    
run()    
    
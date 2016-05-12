# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:35:59 2016

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
        
    dictionary.execute(info_references, info_footnotes) 
    
run()  
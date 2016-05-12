# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:51:32 2016

@author: gebruiker
"""
import re

def main_loop(references, footnotes):
    dict_references={}
    problems=[]
    pre_dict=[]
    print(footnotes[1])
    filenames=references[0]
    filenames2=footnotes[0]
    print(filenames2)
    for i in range(0,len(filenames)):
        name=filenames[i]
        string_name= name[:name.find('.')]
        for j in range(0,len(filenames2)):
            name2=filenames2[j]
            #string_name2=re.compile(r"^(.*?)\..*",name2).group(1)
            string_name2=name2[:name2.find('.')]
            if string_name==string_name2:
                dict_references.update({string_name:(references[1][i],len(references[2][i]),footnotes[1][j],len(footnotes[2][j]),references[2][i],footnotes[2][j])})
                break
            else:
                continue
            
        problems.append(filenames)        
    return dict_references
   
   
   #dict_references.update({filename:(pagenumber,len(listed_references),listed_references)})
    

def execute(references, footnotes):
    return main_loop(references, footnotes)
    
#execute()    
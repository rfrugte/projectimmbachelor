# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:55:41 2016

@author: RPA
"""

import codecs
from bs4 import BeautifulSoup
file = codecs.open("C:/Users/RPA/AppData/Local/Programs/Python/Python35-32/convert.htm", "r","utf-8")
soup = BeautifulSoup(file, 'html.parser')
x= soup.get_text()
x = x.lower()  
y= x.rfind('references\n')
z = x[y:]
r=z.splitlines()

del x
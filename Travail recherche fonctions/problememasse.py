# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 15:45:51 2014

@author: isn
"""

cmol=float(raw_input("Entrer la concentration molaire (en mol/L):"))
mmol=float(raw_input("Entrer la masse molaire de votre entité (en mol/g):"))
vol=float(raw_input("Entrer le volume voulu (en L):"))
n=cmol*vol
m=n*mmol
print("La masse (en g) a prelever est :",m)

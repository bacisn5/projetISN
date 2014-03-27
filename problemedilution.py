# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:20:32 2014

@author: isn
"""

cmolm=float(raw_input("Entrer la concentration molaire de la solution mere (en mol/L):"))
cmolf=float(raw_input("Entrer la concentration molaire de la solution fille (en mol/L):"))
volf=float(raw_input("Entrer le volume voulu (en L) de la solution fille :"))
v=(cmolf*volf)/cmolm
print("Le volume (en L) de la solution mere a prelever est :",v)

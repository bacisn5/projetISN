# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 10:41:40 2014

@author: isn
"""
def calculmasse(cmol,mmol,vol):
    """on demande à l'utilisateur la concentration molaire de la solution, la masse molaire de l'entité et le volume voulu. On renvoie la masse (en g) a prelever."""
    return cmol*vol*mmol
    



print calculmasse(2,4,12)
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 10:17:17 2014

@author: isn
"""

def calculdilution (cmolm,cmolf,volf):
    """on demande ici la concentration molaire de la solution mère ainsi que celle de la solution fille et le volume de solution fille voulu. On renvoie le volume de solution mere a prelever pour la dillution"""
    return (cmolf*volf)/cmolm


print calculdilution(5,3,8)
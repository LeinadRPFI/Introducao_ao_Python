# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:20:10 2021

@author: danie
"""

nome = str(input("Digite o seu nome: ")).upper()

for i in range(0, len(nome)+1):
    print(nome[:i])
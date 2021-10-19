# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:23:35 2021

@author: danie
"""

import random

numerosJogados = []

numerosUm = numerosDois = numerosTres = numerosQuatro = numerosCinco = numerosSeis = 0

def geradorRandom():
        return random.randint(1, 6)
    
for i in range(100):
    numerosJogados.append(geradorRandom())

for x in numerosJogados:
    if(x == 1): 
        numerosUm+= 1
    if(x == 2):
        numerosDois += 1
    if(x == 3): 
        numerosTres += 1
    if(x == 4):
        numerosQuatro += 1
    if(x == 5): 
        numerosCinco += 1
    if(x == 6):
        numerosSeis += 1
    
    
print("\n O numero 1 apareceu: ", numerosUm)
print("\n O numero 2 apareceu: ", numerosDois)
print("\n O numero 3 apareceu: ", numerosTres)
print("\n O numero 4 apareceu: ", numerosQuatro)
print("\n O numero 5 apareceu: ", numerosCinco)
print("\n O numero 6 apareceu: ", numerosSeis)
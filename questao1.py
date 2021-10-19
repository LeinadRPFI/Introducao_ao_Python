# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:47:06 2021

@author: Daniel Chielle
"""

import statistics

nomeAtleta = input("Nome do atleta: ")

primeiroSalto = int(input("Primeiro Salto: "))
segundoSalto = int(input("Segundo Salto: "))
terceiroSalto = int(input("Terceiro Salto: "))
quartoSalto = int(input("Quarto Salto: "))
quintoSalto = int(input("Quinto Salto: "))

lista_saltos = [primeiroSalto, segundoSalto, terceiroSalto, quartoSalto, quintoSalto]
media = statistics.mean(lista_saltos)

print("\nResultado Final: ")
print("Atleta: ", nomeAtleta)
print("Saltos: ", primeiroSalto, " - ", segundoSalto, " - ", terceiroSalto, " - ", quartoSalto, " - ", quintoSalto )
print("Média dos saltos: ", media)
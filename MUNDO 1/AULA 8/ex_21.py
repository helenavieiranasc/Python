'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

from random import shuffle

a1 = input('digite seu nome: ')
a2 = input('digite seu nome: ')
a3 = input('digite seu nome: ')
a4 = input('digite seu nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista) # embaralha a lista de forma aleatória
print(f"a ordem de apresentação será \n{lista}")
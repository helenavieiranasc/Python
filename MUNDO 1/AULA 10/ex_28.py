'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou 
perdeu.'''

from random import randint

numero = int(input("que numero de 0 a 5 você acha que escolhi? "))
n = randint(0, 5)

if numero < 0 or numero > 5:
    print('numero invalido, por favor digite um numero de 0 a 5!')
elif numero == n:
    print(f'Você ganhou! Tambem escolhi o numero {n}')
else:
    print(f'Você perdeu! O numero escolhido foi {n}')
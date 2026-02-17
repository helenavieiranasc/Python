'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians

angulo = float(input('digite um angulo: '))
print(f'o sen, cos e tg do angulo {angulo} sao: ')
print(f'SENO: {sin(radians(angulo)):.2f}') # tem que passar para radianos antes de calcular
print(f'COSSENO: {cos(radians(angulo)):.2f}')
print(f'TANGENTE: {tan(radians(angulo)):.2f}')
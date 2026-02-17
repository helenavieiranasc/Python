'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc

n = float(input('digite um numero: '))
print(f'o numero {n} tem a parte inteira {trunc(n)}')

 
n = float(input('digite um numero: '))
print(f'o numero {n} tem a aprte inteira {int(n)}') # da a parte inteira sem importar
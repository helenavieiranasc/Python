'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print(f'o numero {numero} é par!')
else:
    print(f'o numero {numero} é impar!')
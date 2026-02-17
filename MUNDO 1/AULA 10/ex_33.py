'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

menor = min(n1, n2, n3)
print(f'o menor valor é {menor}')
maior = max(n1, n2, n3)
print(f'o maior valor é {maior}')
'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um 
triângulo.'''

lado_1 = float(input('digite o primeiro lado: '))
lado_2 = float(input('digite o segundo lado: '))
lado_3 = float(input('digite o terceiro lado: '))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    print('esses lados podem formar um triangulo!')
else:
    print('esses lados não podem formar um triangulo!')
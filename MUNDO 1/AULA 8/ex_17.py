'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule 
e mostre o comprimento da hipotenusa.'''

from math import hypot

cateto_oposto = float(input('digite o valor do cateto oposto: '))
cateto_adjacente = float(input('digite o valor do cateto adjacente: '))
hi = hypot(cateto_oposto, cateto_adjacente) # importa calculo da hipotenusa
print(f'a hipotenusa vale {hi:.2f}')

# sem importação
cateto_oposto = float(input('digite o valor do cateto oposto: '))
cateto_adjacente = float(input('digite o valor do cateto adjacente: '))
h1 = (cateto_oposto**2 + cateto_adjacente**2)**0.5
print(f'a hipotenusa mede {h1:.2f}')

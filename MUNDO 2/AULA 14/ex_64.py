'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre 
eles (desconsiderando o flag).'''

numeros = []
numero = 0
while numero != 999:
    numero = int(input("digite um numero (ou 999 para parar): "))
    numeros.append(numero)
print((len(numeros)) - 1)
print((sum(numeros)) - 999)
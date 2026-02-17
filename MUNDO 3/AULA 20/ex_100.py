'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função 
vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

numeros = []

def sorteia():
    print("Sorteando 5 valores: ")
    for i in range(0, 5):
        numero = randint(1, 10)
        print(numero, end=" ", flush=True)
        sleep(0.5)
        numeros.append(numero)
    print("PRONTO!")


def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f"Somando os valores pares de {numeros}, temos {soma}")     

sorteia()
somaPar()
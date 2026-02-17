'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

import time

def maior(* num):
    print("Analisando valores passados...")
    time.sleep(1)
    print("Valores informados:")
    for n in num:
        print(n, end=" ", flush= True)
        time.sleep(0.5)
    print(f"\n{len(num)} valores ao todo, {max(num)} é o maior")

maior(1, 2, 3, 4, 5)
maior(20, 2, 30, 4, 1, 0.5)
maior(1, 2)
maior(9, 7)
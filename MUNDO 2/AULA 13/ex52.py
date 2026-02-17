'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input("digite um numero: "))
total = 0
for i in range(1, n+1):
    if n % i == 0:
        print("\033[33m", end=" ")
        total += 1
    else:
        print("\033[31m", end=" ")
    print(i, end=" ")
if total == 2:
    print(f"\n\033[mO numero é primo!")
else:
    print("\n\033[mO numero nn é primo!")
'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos 
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não 
continuar a digitar valores.'''

numeros = []
while True:
    numero = int(input("digite um numero: "))
    numeros.append(numero)
    continuar = input("deseja add mais um numero (s/n): ").lower()
    if continuar == "s":
        continue
    else:
        break
print(sum(numeros) / len(numeros))
print(max(numeros))
print(min(numeros))
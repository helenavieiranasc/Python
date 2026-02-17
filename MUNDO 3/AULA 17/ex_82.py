'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três 
listas geradas.'''

lista = []
pares = []
impares = []

while True:
    valor = int(input("digite um numero pra add: "))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    continuar = input("s/n: ")
    if continuar == "s":
        continue
    else:
        break

print(lista)
print(pares)
print(impares)
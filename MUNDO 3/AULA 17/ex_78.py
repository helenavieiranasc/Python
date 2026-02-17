'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []

for i in range(0, 5):
    valor = int(input(f"digite o {i + 1}º valor da lista: "))
    lista.append(valor)


print(f"o maior valor da lista foi {max(lista)} nas posições ", end="")

for i, v in enumerate(lista):
    if v == max(lista):
        print(f"{i} - ", end='')
print()

print(f"o menor valor da lista foi {min(lista)} nas posições ", end="")

for i, v in enumerate(lista):
    if v == min(lista):
        print(f"{i} - ", end='')
print()

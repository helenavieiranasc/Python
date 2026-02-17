'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

lista = []
for i in range(0, 5):
    peso = int(input("Digite seu peso: "))
    lista.append(peso)
print(f"{min(lista)} é o menor dos pesos e {max(lista)} é o maior")

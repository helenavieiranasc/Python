'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = 0
caros = 0
cont = 0
while True:
    nome = input("nome do produto: ")
    preco = float(input("preço: R$"))
    cont += 1
    if preco > 1000:
        caros += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = input("qr continuar (s/n): ").lower()
    if continuar == "s":
        continue
    else:
        print(f"o total gasto foi de R${total}")
        print(f"tem {caros} produtos q custam mais de R$1000")
        print(f"o produto mais barato foi {barato} por R${menor}")
        break
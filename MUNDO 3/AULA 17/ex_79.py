'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem 
crescente.'''

lista = []

while True:
    valor = int(input("digite um valor para add na lista (ou '0' para parar): "))
    if valor in lista:
        continue
    elif valor == 0:
        break
    else:
        lista.append(valor)

lista.sort()
print(lista)

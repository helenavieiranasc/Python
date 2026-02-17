'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:      
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente                      
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    valores = int(input("digite um numero para add na lista: "))
    lista.append(valores)
    continuar = input("qr continuar (s/n): ")
    if continuar == "s":
        continue
    else:
        break


print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("o número 5 está na lista")
else:
    print("o número 5 nn está na lista")
'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

valores = []

for i in range(0, 4):
    valor = int(input(f"digite o {i+1}º valor: "))
    valores.append(valor)

tupla = tuple(valores)
print(tupla)

print(f"O valor 9 apareceu {tupla.count(9)} vezes")

if 3 in tupla:
    print(f"O primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}")
else:
    print("O valor 3 não apareceu em nenhuma posição da tupla")

print("os números pares na tupla foram: ")
for valor in tupla:
    if valor % 2 == 0:
        print(valor)

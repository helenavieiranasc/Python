'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição 
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []

for i in range(0, 5):
    valor = int(input(f"digite o {i}º valor: "))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1

print(lista)
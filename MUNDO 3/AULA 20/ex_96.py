'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''

def area(l, c):
    a = l*c
    print(f"A área de um terreno {l}x{c} é de {a}m²")


print("-"*40)
print(f"{'CONTROLE DE TERRENOS':^40}")
print("-"*40)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)

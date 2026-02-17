'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

print("""0- pedra
1- papel
2- tesoura""")
jogador = int(input("Digite o item q vc deseja escolher: "))
while jogador < 0 or jogador > 2:
    print("jogada invalida!")
    jogador = int(input("Digite o item q vc deseja escolher: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print("=-"*20)
print(f"O computador escolheu {(itens[computador])}")
print(f"Voce escolheu {(itens[jogador])}")
print("=-"*20)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    else:
        print("COMPUTADOR VENCE")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    else:
        print("JOGADOR VENCE")
else:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    else:
        print("EMPATE")


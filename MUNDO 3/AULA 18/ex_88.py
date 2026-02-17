'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

import random
import time

print("-"*40)
print("           JOGO DA MEGA SENA         ")
print("-"*40)

qtd_jogos = int(input("Quantos jogos você quer que eu gere? "))
print(f"Sorteando {qtd_jogos} jogos...")
for i in range(qtd_jogos):
    time.sleep(1)
    print(f"Jogo {i+1}: {[random.randint(1,60) for _ in range(6)]}")

print("-"*40)
print("           BOA SORTE!         ")
print("-"*40)
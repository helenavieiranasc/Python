'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

import time

jogador = {}
gols = []

jogador["Nome"] = input("Nome do jogador: ")

partidas = int(input("Partidas jogadas: "))
for i in range(partidas):
    qtd_gols = int(input(f"Quantidade de gols na partida {i + 1}: "))
    gols.append(qtd_gols)

jogador["Gols"] = gols
jogador["Total de gols"] = sum(gols)

print(jogador)

for k, v in jogador.items():
    print(f"{k} = {v}")

print(f"O jogador {(jogador['Nome'])} jogou {partidas} partidas")

for i, gols in enumerate(gols):
    print(f" -> Na partida {i + 1}, fez {gols} gols")
    time.sleep(1)

print(f" -> Total de {(jogador['Total de gols'])} gols")
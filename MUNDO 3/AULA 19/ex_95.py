'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''

import time

jogador = {}
jogadores = []
gols = []

while True:
    jogador.clear()
    gols.clear()
    jogador["Nome"] = input("Nome do jogador: ")

    partidas = int(input("Partidas jogadas: "))
    for i in range(partidas):
        qtd_gols = int(input(f"Quantidade de gols na partida {i + 1}: "))
        gols.append(qtd_gols)

    jogador["Gols"] = gols[:]
    jogador["Total de gols"] = sum(gols)
    jogadores.append(jogador.copy())
    continuar = input("Continuar (S/N): ").strip().upper()
    if continuar == "S":
        continue
    else:
        break

print("cod", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end=" ")
print()

for k, v in enumerate(jogadores):
    print(f"{k:>4}", end=" ")
    for d in v.values():
        print(f"{str(d):>15}", end=" ")
    print()

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para sair) "))
    if busca == 999:
        print("Saindo...")
        break
    else:
        if busca >= len(jogadores) or busca < 0:
            print(f"ERRO! Não existe jogador com código {busca}!")
        else:
            print(f"O jogador {jogadores[busca]['Nome']} jogou {len(jogadores[busca]['Gols'])} partidas")
            for i, gols in enumerate(jogadores[busca]['Gols']):
                print(f" -> Na partida {i + 1}, fez {gols} gols")
                time.sleep(1)

            print(f" -> Total de {jogadores[busca]['Total de gols']} gols")
'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado.'''

import random
import time
from operator import itemgetter

jogos = {
    'jogador 1': random.randint(1, 6),
    'jogador 2': random.randint(1, 6),
    'jogador 3': random.randint(1, 6),
    'jogador 4': random.randint(1, 6)
}

print("Valores sorteados:")
for k, v in jogos.items():
    print(f"O {k} tirou {v}")
    time.sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("\nRanking")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    time.sleep(1)
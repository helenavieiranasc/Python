'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

artistas = ('The Weeknd', 'Taylor Swift', 'Bad Bunny',
 'Drake', 'Billie Eilish', 'Bruno Mars', 'Ariana Grande',
 'Ed Sheeran', 'Dua Lipa', 'Travis Scott') # exercicío adaptado!!!

print(f"Os 5 primeiros colocados da lista são: \n{artistas[0:5]}")
print(f"Os últimos 4 colocados são: \n{artistas[-4:]}")
print(f"Lista de artistas em ordem alfabetica: \n{(sorted(artistas))}")
print(f"Taylor swift está na posição {artistas.index('Taylor Swift')}")
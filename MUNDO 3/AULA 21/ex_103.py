'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gols!")


nome = input("Nome do jogador: ").strip()
gols = input("Quantidade de gols: ")

if gols.isnumeric():
    gols = int(gols)
else: 
    gols = 0

if nome == "":
    ficha(gols= gols)
else:
    ficha(nome, gols)
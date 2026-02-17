'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

cont = 0
while True:
    vc = int(input("digite um valor: "))
    poui = input("par ou impar (p/i): ").lower()
    computador = randint(1, 10)
    soma = vc + computador 
    if soma % 2 == 0:
        resultado = "p"
    else:
        resultado = "i"
    if poui == resultado:
        cont += 1
        print(f"vc escolheu {vc} e o computador {computador} que da {soma} entao: ")
        print("vc ganhou!!")
    else:
        print(f"vc escolheu {vc} e o computador {computador} que da {soma} entao: ")
        print("vc perdeu")
    dnv = input("quer ir dnv (s/n): ").lower()
    if dnv == "s":
        continue
    else:
        print(f"vc ganhou {cont} vezes")
        break

'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai 
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

n = int(input("digite o numero de 0 a 10 que vc acha q eu escolhi: "))
numero = randint(0, 10)

palpites = 0
while n != numero:
    print("errou, tenta de novo!")
    if numero > n:
        print("dica: é mais...")
    else:
        print("dica: é menos...")
    n = int(input("digite o numero de 0 a 10 que vc acha q eu escolhi: "))
    palpites += 1 
print(f"vc acertou dps de {palpites} palpites")
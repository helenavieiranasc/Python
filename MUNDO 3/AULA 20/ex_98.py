'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(i, end=" ", flush=True)
    print("FIM!")


def personalizar():
    print("Agora é sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    contador(inicio, fim + 1, passo)


print("Contagem de 1 até 10 de 1 em 1")
contador(inicio=1, fim= 11, passo=1)
print("Contagem de 10 até 0 de 2 em 2")
contador(inicio=10, fim= -1, passo=-2)

while True:
    personalizar()
    dnv = input("Quer tentar de novo? (s/n) ").strip().lower()
    if dnv == "s":
        continue
    else:
        break
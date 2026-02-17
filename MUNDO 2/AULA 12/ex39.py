'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

ano_atual = date.today().year
ano_alistamento = 18
ano_nasc = int(input("Digite o ano em que vc nasceu: "))

idade = ano_atual - ano_nasc 
if idade < ano_alistamento:
    tempo_falta = ano_alistamento - idade
    print(f"Vc tem {idade} anos e precisa se alistar daqui a {tempo_falta} anos")
elif idade == ano_alistamento:
    print(f"Vc tem {idade} anos e deve ir se alistar esse ano!")
else:
    tempo_passou = idade - ano_alistamento
    print(f"Vc tem {idade} anos e deveria ter se alistado {tempo_passou} anos atras")

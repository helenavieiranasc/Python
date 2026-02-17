'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.'''

def voto(ano_nasc):
    idade = 2026 - ano_nasc
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    elif 16 <= idade < 18 or idade > 60:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

ano_nasc = int(input("Digite o ano em que você nasceu: "))
print(voto(ano_nasc))
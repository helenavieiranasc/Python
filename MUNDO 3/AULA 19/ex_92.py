'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

import datetime

info = {}

while True:
    info["Nome"] = input("Nome: ")

    ano_nasc = int(input("Ano de nascimento: "))
    idade = datetime.date.today().year - ano_nasc
    info["Idade"] = idade

    info["CTPS"] = int(input("Carteira de trabalho (0 não tem): "))
    if info["CTPS"] == 0:
        break
    else:
        info["Ano de contratação"] = int(input("Ano de contratação: "))
        if datetime.date.today().year - info["Ano de contratação"] >= 35:
            info["Aposentadoria"] = "Aposentado"
        else:
            info["Aposentadoria"] = info["Idade"] + (35 - (datetime.date.today().year - info["Ano de contratação"]))

        info["Salário"] = float(input("Salário: R$"))
        break

for k, v in info.items():
    print(f"{k} = {v}")
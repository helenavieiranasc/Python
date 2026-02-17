'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

ano = int(input('digite um ano: '))
if ano == 0:
    from datetime import date
    ano = date.today().year # importa o ano atual (da maquina)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'o ano {ano} é bissexto!')
else:
    print(f'o ano {ano} não é bissexto!')
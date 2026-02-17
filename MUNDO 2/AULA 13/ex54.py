'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não 
atingiram a maioridade e quantas já são maiores.'''

maiores = 0
menores = 0
for i in range(0, 7):
    ano_nasc = int(input("Digite seu ano de nascimento: "))
    if 2025 - ano_nasc >= 18:
        maiores += 1
    else:
        menores += 1
print(f"{maiores} pessoas são maiores de idade e {menores} são menores")
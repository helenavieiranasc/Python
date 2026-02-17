'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior = 0
homens = 0
mulheres = 0
while True:
    print("\n------ cadastro ------")
    idade = int(input("idade: "))
    if idade > 18:
        maior += 1
    sexo = input("sexo (m/f): ").lower()
    if sexo == "m":
        homens += 1
    elif sexo == "f" and idade < 20:
        mulheres += 1
    print("-"*22)
    continuar = input("qr continuar (s/n): ").lower()
    if continuar == "s":
        continue
    else:
        print(f"tem {maior} pessoas com mais de 18 anos")
        print(f"{homens} homens cadastrados")
        print(f"{mulheres} mulheres com menos de 20 anos")
        break

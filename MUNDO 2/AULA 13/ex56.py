'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade 
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

idades = []
mulheres = 0
for i in range(0, 4):
    print(f"------ {i + 1}º PESSOA ------")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    idades.append(idade)
    sexo = input("Sexo (f/m): ").strip().lower()
    if sexo == "f" and idade < 20:
        mulheres += 1
    elif sexo == "m" and idade == max(idades):
        nomeh = nome

print(f"O homem mais velho tem {max(idades)} e chama {nomeh}")
print(f"Tem {mulheres} mulheres com menos de 20 anos no grupo")
print(f"A média das idades do grupo é de {sum(idades)/4}")
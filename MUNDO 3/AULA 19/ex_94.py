'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

dados = {}
pessoas = []
mulheres = []
idades = []

while True:
    dados["Nome"] = input("Nome: ")
    dados["Sexo"] = input("Sexo (F/M): ").strip().upper()
    if dados["Sexo"] == "F":
        mulheres.append(dados["Nome"])

    dados["Idade"] = int(input("Idade: "))
    idades.append(dados["Idade"])
    pessoas.append(dados.copy())
    continuar = input("Continuar (S/N): ").strip().upper()
    if continuar == "S":
        continue
    else:
        break

print(pessoas)

media = sum(idades) / len(idades)
         
print(f"Foram cadastradas {(len(pessoas))} pessoas")
print(f"A média das idades do grupo é de {media:.1f}")
print("Mulheres cadastradas: ")
for i in mulheres:
    print(i)

print("Pessoas com idades acima da média: ")
for i in pessoas:
    if i["Idade"] >= media:
        print(f"{i['Nome']} -> {i['Idade']} anos")




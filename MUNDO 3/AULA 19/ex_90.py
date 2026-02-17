'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}

aluno["Nome"] = input("Nome do aluno: ")
aluno["Média"] = float(input("Média do aluno: "))
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

for k, v in aluno.items():
    print(f"{k} = {v}")
'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

info = []

while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    info.append([nome, [nota1, nota2], media])

    continuar = input("Deseja adicionar mais alunos? (s/n): ").strip().lower()
    if continuar == "n":
        break
    else:
        continue

print("-"*40)
print("               BOLETIM      ")
print("-"*40)

print(f'{"No.":<4}{"NOME":>10}{"MÉDIA":>20}')
print("-"*40)
for i, a in enumerate(info):
    print(f"{i:<4}{a[0]:>10}{a[2]:>20.1f}")

while True:
    notas = int(input("Digite o número do aluno que deseja ver a nota (999 para fechar): "))
    if notas == 999:
        print("Saindo...")
        break
    else:
        if notas <= len(info) - 1:
            print(f"Notas de {info[notas][0]} são {info[notas][1]}")

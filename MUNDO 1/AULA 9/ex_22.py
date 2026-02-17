'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input("digite seu nome: ")).strip()
print(nome.upper())
print(nome.lower())
print(f'seu nome tem {(len(nome) - nome.count(" "))} letras')
primeiro_nome = nome.split()
print(f'seu primeiro nome é {primeiro_nome[0]} e ele tem {(len(primeiro_nome[0]))} letras')
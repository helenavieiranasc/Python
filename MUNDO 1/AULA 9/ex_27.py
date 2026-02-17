'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome 
separadamente.'''

nome = str(input("digite seu nome completo: ")).strip()
print(f'seu primeiro nome é {nome.split()[0]}')
print(f'seu ultimo nome é {nome.split()[-1]}')
'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = input("digite seu nome: ").lower().strip()
print(f'Tem Silva no seu nome? {("silva" in nome)}')


nome = input("digite seu nome: ").lower().strip()
if "silva" in nome:
    print('você tem silva no nome')
else:
    print('você não tem silva no nome')

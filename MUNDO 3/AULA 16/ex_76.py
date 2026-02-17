'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No 
final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00)

print("-"*60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print("-"*60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<53}", end="")
    else:
        print(f"R${listagem[pos]:>2.2f}")
print("-"*60)
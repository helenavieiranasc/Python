'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço 
for'''

n = int(input("Digite o numero q vc deseja ver a tabuada: "))
for i in range(0, 11):
    print(f"{n} X {i} = {n*i}")
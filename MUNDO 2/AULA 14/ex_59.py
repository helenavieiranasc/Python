'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

valor_1 = int(input("digite o 1º valor: "))
valor_2 = int(input("digite o 2º valor: "))

while True:
    print('''
    1- somar
    2- multiplicar
    3- maior
    4- novos numeros
    5- sair
    ''')
    opcao = int(input("sua opção: "))

    if opcao == 1:
        print(f"A soma entre {valor_1} e {valor_2} é igual a {valor_1 + valor_2}")
    elif opcao == 2:
        print(f"A multiplicação entre {valor_1} e {valor_2} é igual a {valor_1*valor_2}")
    elif opcao == 3:
        if valor_1 > valor_2:
            print(f"O maior valor é o {valor_1}")
        else:
            print(f"O maior valor é o {valor_2}")
    elif opcao == 4:
        valor_1 = int(input("digite o 1º valor: "))
        valor_2 = int(input("digite o 2º valor: "))
    elif opcao == 5:
        print("saindo...")
        exit()
    else:
        print("resposta invalida!")

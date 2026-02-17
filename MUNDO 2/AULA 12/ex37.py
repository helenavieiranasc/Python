'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base 
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input("Digite o numero q vc deseja converter: "))
print("1 - binario \n2 - octal \n3 - hexadecimal")

opcao = int(input("digite sua opção (1, 2 ou 3): "))
while opcao < 0 or opcao > 3:
    print("opção invalida!")
    opcao = int(input("digite sua opção (1, 2 ou 3): "))

def binario():
    print(f"O numero {numero} convertido pra binario é {bin(numero)[2:]}")

def octal():
    print(f"O numero {numero} convertido pra octal é {oct(numero)[2:]}")

def hexadecimal():
    print(f"O numero {numero} convertido pra hexadecimal é {hex(numero)[2:]}")


def menu():
    if opcao == 1:
        binario()
    elif opcao == 2:
        octal()
    else:
        hexadecimal()

menu()
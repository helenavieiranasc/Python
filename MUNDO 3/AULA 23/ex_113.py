'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!\033[m")
            continue
        except (KeyboardInterrupt):
              print("\033[0;31mUSUÁRIO INTERROMPEU O PROGRAMA!\033[m")
              return 0
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mDIGITE UM NÚMERO VÁLIDO!!\033[m")
            continue
        except (KeyboardInterrupt):
              print("\033[0;31mUSUÁRIO INTERROMPEU O PROGRAMA!\033[m")
              return 0
        else:
            return n
        
n1 = leiaInt("Digite um inteiro: ")
n2 = leiaFloat("Digite um real: ")
print(f"Você digitou o número {n1} e o número {n2}")
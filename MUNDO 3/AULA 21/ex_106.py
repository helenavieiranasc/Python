'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
Importante: use cores.'''

from time import sleep

def escreva(txt):
    palavra = txt
    print("~" * len(palavra))
    print(txt)
    print("~" * len(palavra))

def ajuda():
    while True:
        escreva("\033[45mSISTEMA DE AJUDA DO PYTHON\033[m")
        funcao = input("Função ou biblioteca >  ").lower()
        if funcao == "fim":
            escreva("\033[46mATÉ LOGO!\033[m")
            break
        else:
            escreva(f"\033[44mAcessando o manual do comando '{funcao}'\033[m")
            sleep(1)
            print("\033[7;30m")
            help(funcao)
            print("\033[m")
        

ajuda()

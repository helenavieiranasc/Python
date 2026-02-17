'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções, cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from interface import *
from time import sleep
from arquivo import *

arq = 'pessoascadastradas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair so sitema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo...")
        break
    else:
        print("\033[31mERRO: digite uma opção válida!\033[m")
    sleep(2)

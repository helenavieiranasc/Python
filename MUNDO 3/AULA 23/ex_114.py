'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print("O site não está acessivél no momento")
else:
    print("Site acessado com sucesso!")
    print(site.read())

'''
OBSERVAÇÕES SOBRE POR QUE O SITE PODE CONSTAR COMO INACESSÍVEL MESMO ESTANDO NO AR:
1. BLOQUEIO DE USER-AGENT: O servidor identifica que o acesso vem de um script Python 
   (biblioteca urllib) e recusa a conexão por segurança, tratando como um ataque de bot.
2. TIMEOUT: Em conexões lentas ou via Wi-Fi, o script pode desistir de esperar a resposta 
   antes do navegador, gerando um erro de tempo esgotado.
3. PERMISSÕES DE SISTEMA: Alguns antivírus ou Firewalls bloqueiam especificamente o 
   interpretador do Python de realizar requisições externas.
'''

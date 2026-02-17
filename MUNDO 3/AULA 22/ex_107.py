'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from utilidadesCeV import moeda1 
# criei um arquivo moeda1 para salvar a resolução antes da atualização das funções para os próximos exercícios

n = float(input("Digite o preço: R$"))
print(f"Aumentando 10% de {n} temos {moeda1.aumentar(n)}")
print(f"Diminuindo 10% de {n} temos {moeda1.diminuir(n)}")
print(f"Dobrando {n} temos {moeda1.dobro(n)}")
print(f"Dividindo {n} pela metade temos {moeda1.metade(n)}")
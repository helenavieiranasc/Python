'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''

from utilidadesCeV import moeda1
# criei um arquivo moeda1 para salvar a resolução antes da atualização das funções para os próximos exercícios

n = float(input("Digite o preço: R$"))
print(f"Aumentando 10% de {moeda1.moeda(n)} temos {moeda1.moeda(moeda1.aumentar(n))}")
print(f"Diminuindo 10% de {moeda1.moeda(n)} temos {moeda1.moeda(moeda1.diminuir(n))}")
print(f"Dobrando {moeda1.moeda(n)} temos {moeda1.moeda(moeda1.dobro(n))}")
print(f"Dividindo {moeda1.moeda(n)} pela metade temos {moeda1.moeda(moeda1.metade(n))}")
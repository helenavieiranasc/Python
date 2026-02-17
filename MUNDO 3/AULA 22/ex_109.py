'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from utilidadesCeV import moeda

n = float(input("Digite o preço: R$"))
print(f"Aumentando 10% de {moeda.moeda(n)} temos {moeda.aumentar(n, True)}")
print(f"Diminuindo 10% de {moeda.moeda(n)} temos {moeda.diminuir(n, True)}")
print(f"Dobrando {moeda.moeda(n)} temos {moeda.dobro(n, True)}")
print(f"Dividindo {moeda.moeda(n)} pela metade temos {moeda.metade(n, True)}")

print(f"\nAumentando 10% de {n} temos {moeda.aumentar(n, False)}")
print(f"Diminuindo 10% de {n} temos {moeda.diminuir(n, False)}")
print(f"Dobrando {n} temos {moeda.dobro(n, False)}")
print(f"Dividindo {n} pela metade temos {moeda.metade(n, False)}")
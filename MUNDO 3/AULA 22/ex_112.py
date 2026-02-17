'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dados. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.'''

from utilidadesCeV import dados, moeda

n = dados.leiaDinheiro("Digite o preço: R$")
moeda.resumo(n)
def aumentar(n, format):
    r = n + (n * 0.1)
    if format == True:
        return f"R${r:.2f}".replace('.', ',')
    else:
        return r

def diminuir(n, format):
    r = n - (n * 0.1)
    if format == True:
        return f"R${r:.2f}".replace('.', ',')
    else:
        return r

def dobro(n, format):
    r = n * 2
    if format == True:
        return f"R${r:.2f}".replace('.', ',')
    else:
        return r

def metade(n, format):
    r = n/2
    if format == True:
        return f"R${r:.2f}".replace('.', ',')
    else:
        return r

def moeda(r):
    return f"R${r:.2f}".replace('.', ',')

def resumo(n):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-"*30)
    print(f"Preço analisado:     {moeda(n)}")
    print(f"Aumento de 10%:      {aumentar(n, True)}")
    print(f"Redução de 10%:      {diminuir(n, True)}")
    print(f"Dobro do preço:      {dobro(n, True)}")
    print(f"Metade do preço:     {metade(n, True)}")
    print("-"*30)
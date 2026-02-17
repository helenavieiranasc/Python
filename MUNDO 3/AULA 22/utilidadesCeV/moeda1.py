def aumentar(n):
    r = n + (n * 0.1)
    return r

def diminuir(n):
    r = n - (n * 0.1)
    return r

def dobro(n):
    r = n * 2
    return r

def metade(n):
    r = n/2
    return r

def moeda(r):
    return f"R${r:.2f}".replace('.', ',')
lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')

print(lanche)
print(sorted(lanche)) # coloca em ordem

for comida in lanche:
    print(f"vou comer {comida}")

for i in range(0, len(lanche)):
    print(f"vou comer {lanche[i]} na posição {i}")

for pos, comida in enumerate(lanche):
    print(f"vou comer {comida} na posição {pos}")

############################################################

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
d = b + a
print(c, d)
print(c.count(2))
print(c.index(5)) # se tiver algum igual pega o primeiro
del(a) # apaga a tupla
print(a) # erro pq "a" não existe mais
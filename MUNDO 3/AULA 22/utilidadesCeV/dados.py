def leiaDinheiro(msg):
    while True:
        n = input(msg).replace(',', '.')
        if n.replace('.', '', 1).isdigit():
            return float(n)
        else:
            print("\033[0;31mDIGITE UM NÚMERO VÁLIDO!!\033[m")

'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

total = float(input("Digite o valor total das compras: "))
print("""Formas de pagamento
1- a vista dinheiro/cheque
2- a vista cartão
3- 2x no cartão
4- 3x ou mais no cartão""")

opcao = int(input("Digite sua opção: "))
while opcao < 0 or opcao > 4:
    print("Opção invalida!")
    opcao = int(input("Digite sua opção: "))

def vista():
    final = total - (total*0.1)
    print(f"Sua compra ganhou 10% de desconto e ficou no valor final de R${final}")

def vista_cartao():
    final = total - (total*0.05)
    print(f"Sua compra ganhou 5% de desconto e ficou no valor final de R${final}")

def duas_vzs():
    final = total/2
    print(f"Sua compra sera parcelada em 2x de R${final}")

def tres_mais():
    parcelas = int(input("Digite em quantas parcelas vc deseja dividir: "))
    while parcelas <= 2:
        print("opção invalida!")
        parcelas = int(input("Digite em quantas parcelas vc deseja dividir: "))
    
    juros = total + (total*0.2)
    final = juros/ parcelas
    print(f"Sua compra sera parcelada em {parcelas}x de R${final} com juros, o total é de {juros}")

def menu():
    if opcao == 1:
        vista()
    elif opcao == 2:
        vista_cartao()
    elif opcao == 3:
        duas_vzs()
    else:
        tres_mais()

menu()
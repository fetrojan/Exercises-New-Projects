#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

price = float(input('Digite o preço do produto: R$'))
print('''Confira as condições de pagamento, e escolha a sua opção:
[1] À VISTA DINHEIRO/CHEQUE = 10% de desconto
[2] À VISTA NO CARTÃO = 5% de desconto
[3] EM ATÉ 2X NO CARTÃO = PREÇO FORMAL
[4] 3X OU MAIS NO CARTÃO = 20% DE JUROS)''')
option = int(input('Digite sua opção: '))
if option == 1:
    desconto = price * 0.1
    final = price - desconto
    print('Você selecionou \33[35mDINHEIRO/CHEQUE\33[m, você ganhou R${:.2f} de desconto, valor final a ser pago é de R${:.2f}'.format(desconto,final))
elif option == 2:
    desconto = price * 0.05
    final = price - desconto
    print('Você selecionou \33[36mÀ VISTA NO CARTÃO\33[m, você ganhou R${:.2f} de desconto, valor final a ser pago é de R${:.2f}'.format(desconto, final))
elif option == 3:
    parcela = price / 2
    print('Você selecionou \33[34mEM ATÉ 2x NO CARTÃO\33[m, você pode pagar o valor total de R${:.2f} em até 2 parcelas de R${:.2f}'.format(price, parcela))
elif option == 4:
    juros = price * 0.20
    final = price + juros
    tparc = int(input("Digite em quantas vezes deseja parcelar: "))
    parcela = final / tparc
    print('Você selecionou \33[37m3x OU MAIS NO CARTÃO\33[m, o valor final ficará em R${:.2f} em {} parcelas de R${:.2f}'.format(final, tparc, parcela))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')

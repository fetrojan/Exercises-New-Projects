# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
money = float(input('Digite quanto dinheiro você tem em reais: R$'))
print('Com R${:.2f}, você consegue comprar US${:.2f}!'.format(money, money/5.05))

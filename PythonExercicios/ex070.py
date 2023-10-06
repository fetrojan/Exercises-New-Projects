#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('*-*'*6, 'CADASTRO DE PRODUTOS', '*-*'*6)

cont = total = prodmil = baratezaprice = 0
barateza = ' '

while True:
    produto = str(input('NOME DO PRODUTO: ')).strip()
    preco = float(input('PREÇO DO PRODUTO:R$ '))
    total += preco
    cadastro = ' '
    cont += 1

    if preco > 1000:
        prodmil += 1
    if cont == 1:
        barateza = produto
        baratezaprice = preco
    else:
        if baratezaprice < preco:
            barateza = produto
            baratezaprice = preco
    while cadastro not in 'SN':
        cadastro = str(input('Quer continuar comprando? [S/N] ')).strip().upper()[0]
    if cadastro == 'N':
        break

print('=*' *6, 'FIM DAS COMPRAS', '=*'*6)
print(f'Você esta levando {cont} produtos. O total gasto nos produtos é de R${total}', end='')
print(f' Dentro do carrinho existem {prodmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato do carrinho é o {barateza}, pelo preço de R${baratezaprice}')


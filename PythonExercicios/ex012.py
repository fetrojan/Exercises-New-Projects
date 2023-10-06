#Faça um algoritmo que leia o preço de um produto, e mostre o seu novo preço com 5% de desconto
preço = float(input('Digite o preço do produto que deseja comprar: R$'))
desconto = preço * (5/100)
nov_preço = preço - desconto
print('Este produto vale R${:.2f}, mas esta com um desconto de 5% que equivale a R${:.2f},\nportanto ele fica por R${:.2f}'.format(preço, desconto, nov_preço))
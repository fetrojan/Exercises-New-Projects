#Escreva um programa para aprovar um empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o salario
# do comprador, e em quantos anos ele vai quitar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30%
# do salario, ou o emprestimo sera negado
casa = float(input('Qual o valor da casa que você deseja comprar? '))
salario = float(input('Qual é a sua renda mensal? '))
tempo = float(input('Em quantos anos pretende quitar a divida? '))*12
parcela = casa/tempo
if parcela > 0.3 * salario:
    print('Desculpe, mas você não pode arcar com uma parcela de R${:.2f}! \033[31mEMPRESTIMO NEGADO!\033[m)'.format(parcela))
else:
    print('OK, você deverá pagar uma parcela de R${:.2f} mensais, por {} anos!'.format(parcela, tempo/12))

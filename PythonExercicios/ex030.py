#Escreva um programa que receba um número, e diga se ele é par ou impar
n = int(input('Digite um número inteiro e descubra se ele é par ou ímpar: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))

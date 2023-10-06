# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
n1 = eval(input('Digite um número inteiro e descubra seu sucessor e antecessor: '))

if isinstance(n1, int):
    s = n1 + 1
    sub = n1 - 1
    print('O sucessor deste número é {}, e seu antecessor é {}!'.format(s, sub))
else:
    print('Deve ser um valor inteiro!')

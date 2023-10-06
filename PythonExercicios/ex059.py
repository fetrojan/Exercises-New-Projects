# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''Escolha a operação que deseja realizar:
    Digite:
    [1] para somar
    [2] para multiplicar
    [3] para maior que
    [4] para informar novos números
    [5] para sair do programa''')
    opc = int(input('-------------- Informe a opção desejada: '))
    if opc == 1:
        soma = n1 + n2
        print('A soma de {} com {} é {}.'.format(n1, n2, soma))
    if opc == 2:
        prod = n1 * n2
        print('O produto da multiplicação entre {} e {} é {}.'.format(n1, n2, prod))
    if opc == 3:
        if n1 > n2:
            print('O valor de {} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('O valor de {} é maior que {}.'.format(n2, n1))
        else:
            print('Os dois números são iguais, não há maior!')
    if opc == 4:
        n1 = int(input('Digite um primeiro novo valor para a operação: '))
        n2 = int(input('Digite um segundo novo valor para a operação: '))
    if opc == 5:
        print('Finalizando...')
    print('-=-' * 15)
    sleep(2)

print('Programa FINALIZADO.')

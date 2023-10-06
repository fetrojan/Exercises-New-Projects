#Crie um programa que faça o computador jogar Jokenpô com você
import random
from time import sleep
print("{:^40}".format(' JOOOOOKEEEEN...PÔ!!!!! '))
print('Pronto pro PEDRA, PAPEL OU TESOURA? TENTA A SORTE!!!')
tentativa = str(input('DIGITE SUA TENTATIVA:')).upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
cppick = random.choice(lista)
print('JOOOOO')
sleep(0.6)
print('KEEEEEN')
sleep(0.6)
print('PÔ!!!')
print('O COMPUTADOR JOGOU! {}'.format(cppick))
if tentativa == 'PEDRA':
    if cppick == 'TESOURA':
        print('VOCÊ GANHOU! PEDRA DETRÓI TESOURA!')
    elif cppick == 'PAPEL':
        print('VOCÊ PERDEU! PAPEL ENROLA PEDRA!')
    elif cppick == 'PEDRA':
        print('EMPATE! PEDRA vs PEDRA!')
elif tentativa == 'TESOURA':
    if cppick == 'TESOURA':
        print('EMPATE! TESOURA vs TESOURA!')
    elif cppick == 'PAPEL':
        print('VOCÊ GANHOU! TESOURA CORTA O PAPEL!!')
    elif cppick == 'PEDRA':
        print('VOCÊ PERDEU! PEDRA DESTRÓI TESOURA!')
elif tentativa == 'PAPEL':
    if cppick == 'TESOURA':
        print('VOCÊ PERDEU! TESOURA CORTA O PAPEL!!')
    elif cppick == 'PAPEL':
        print('EMPATE! PAPEL vs PAPEL!')
    elif cppick == 'PEDRA':
        print('VOCÊ GANHOU! PAPEL ENROLA A PEDRA!')
else:
    print('INVÁLIDO, TENTE NOVAMENTE!')

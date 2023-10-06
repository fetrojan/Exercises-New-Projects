#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op = int(input('Digite sua opção: '))
if op == 1:
    print('O número {} na base BINÁRIA fica {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} na base OCTAL fica {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} na base HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
else:
    print('Número invalido, tente novamente!')


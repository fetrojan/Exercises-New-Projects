#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Descubra se 3 retas quaisquer, podem formar um triângulo!!')
a = float(input('Digite o comprimento do primeiro segmento de reta: '))
b = float(input('Digite o comprimento do segundo segmento de reta: '))
c = float(input('Digite o comprimento do terceiro segmento de reta: '))
if a + b > c and a + c > b and c + b > a:
    print('As três retas informadas \33[34mPODEM\33[m formar um triângulo!!')
else:
    print('As três retas informadas \33[33mNÃO CONSEGUEM\33[m formar um triângulo!')

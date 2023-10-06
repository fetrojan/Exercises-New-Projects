#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('''Descubra se 3 retas quaisquer, podem formar um triângulo!!
E qual será O TIPO deste triângulo formado!''')
a = float(input('Digite o comprimento do primeiro segmento de reta: '))
b = float(input('Digite o comprimento do segundo segmento de reta: '))
c = float(input('Digite o comprimento do terceiro segmento de reta: '))
if a + b > c and a + c > b and c + b > a:
    print('As três retas informadas \33[34mPODEM\33[m formar um triângulo!!')
    if a == b == c:
        print('Com todos os lados iguais, este será um triângulo EQUILATERO!')
    elif a == b or a == c or b == c:
        print('Com dois lados iguais, e outro diferente, este será um triângulo ISÓSCELES!')
    else:
        print('Com todos os lados diferentes, este será um triângulo ESCALENO!')
else:
    print('As três retas informadas \33[33mNÃO CONSEGUEM\33[m formar um triângulo!')
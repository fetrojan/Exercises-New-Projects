#Crie um programa que leia um número real qualquer e mostre sua porção inteira
import math
num = float(input('Digite um número: '))
num_int = math.trunc(num)
print('A parte inteira de {} é {}'.format(num, num_int))

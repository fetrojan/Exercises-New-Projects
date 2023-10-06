#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre a hipotenusa
import math
cat_opo = float(input('Informe o comprimento do cateto oposto do seu triângulo: '))
cat_adj = float(input('Informe o comprimento do cateto adjacente do seu triângulo: '))
h = ((math.pow(cat_opo,2))+(math.pow(cat_adj, 2)))**(1/2)
print('A hipotenusa do seu triângulo é {:.2f}m'.format(h))
print('A hipotenusa do seu triângulo é {:.2f}m'.format(math.hypot(cat_adj,cat_opo)))
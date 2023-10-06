#Faça um programa que leia um ângulo, e informe o seu seno, cosseno e tangente.
import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do ângulo {} é {:.2f}!\nO cosseno do ângulo {} é {:.2f}!\nA tangente do ângulo {} é {:.2f}!'.format(ang, sen, ang, cos, ang, tan))

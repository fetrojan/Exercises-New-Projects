# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = eval(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5
print('Você escolheu o número {}, o qual o seu dobro é {}, seu triplo é {} e o sua raiz quadrada é {:.2f}' .format(n, dobro, triplo, raiz))
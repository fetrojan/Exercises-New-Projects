#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorios = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

print(f'Lista de números: {aleatorios}')
print(f'O menor número sorteado foi: {min(aleatorios)}')
print(f'O maior número sorteado foi: {max(aleatorios)}')
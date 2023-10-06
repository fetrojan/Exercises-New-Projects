#Escreva um programa que faça o computador pensar em número inteiro entre 0 e 5, e peça para o usúario tentar adivinhar o número escolhido
#O programa deverá escrever na tela se o usuario venceu ou perdeu
import random
from time import sleep
n = random.randint(0,5)
chute = int(input('Digite um número inteiro entre 0 e 5 e veja se você é o sortudo: '))
print("PROCESSANDO... vamos ver se você é o sabichão!")
sleep(2)
if chute == n:
    print('Ah muleque! Você acertou!')
else:
    print('Você errou, tente outra vez! A resposta certa era {}!'.format(n))

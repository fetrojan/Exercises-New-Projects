#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
n = randint(0,10)
tent = 1
chute = int(input('Vamos ver se você é o sabichão, escolha um número inteiro entre 0 e 10: '))
print('Processando...')
sleep(1)
while chute != n:
    chute = int(input('\33[33mBEHHHH!!! Resposta errada!!\33[mTente mais uma vez: '))
    tent += 1
    print('Processando...')
    sleep(1)
if tent == 1:
    print('\33[32mVOCÊ É O SABICHÃO MESMO!\33[m EM APENAS {} tentativa!!'.format(tent))
elif 2 >= tent <= 5:
    print('FINALMENTE!! Você ganhou! Após {} tentativas'.format(tent))
else:
    print('ACHEI QUE NÃO IA TERMINAR NUNCA, você precisou de {} tentativas para vencer!'.format(tent))


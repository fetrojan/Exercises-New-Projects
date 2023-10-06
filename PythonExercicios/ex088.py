#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogo = []
tot = 0
quant = int(input('Digite quantos jogos você quer sortear: '))
while tot < quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    tot += 1
print('=-'* 10, f'Sorteando {quant} jogos', '=-'*10)
for i, l in enumerate(lista):
    print(f'Jogo {i+1} = {l}')


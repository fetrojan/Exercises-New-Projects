#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vit = part = 0
while True:
    computador = randint(1,10)
    jogador = int(input('Digite o número que vai jogar: '))
    soma = jogador + computador
    tipo = ' '
    part += 1
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()
    print(f'Computador jogou {computador}')
    print(f'{jogador} + {computador} deu um total de {soma}! ', end='')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU!')
            vit += 1
        else:
            print('VOCÊ PERDEU!!')
            break
    if tipo == 'I':
        if soma % 2 == 0:
            print('VOCÊ PERDEU!!!')
            break
        else:
            print('VOCÊ GANHOU!')
            vit += 1
    print('Mais uma vez...')
print(f'VocÊ jogou {part} partidas e ganhou {vit}')



#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

n = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
termo = n
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    c += 1
print('ACABOU')
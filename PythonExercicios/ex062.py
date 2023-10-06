#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

n = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))

termo = n
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos números a mais você quer ver: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

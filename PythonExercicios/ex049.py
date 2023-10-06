#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Escolha um número e obtenha sua tabuada:'))
for c in range (0,11):
    print('{} * {} = {}'.format(n, c, n*c))

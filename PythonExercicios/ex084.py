#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
cont = 0
pesados = list()
leves = list()

while True:
    dados.append(str(input('Nome da pessoa: ')))
    dados.append(int(input('Peso da pessoa: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1

    r = (str(input('Quer continuar? [S/N] ')))
    if r in 'nN':
        break

for p in pessoas:
    if p[1] >= 100:
        pesados.append(p)
    else:
        leves.append(p)
print(f'Foram cadastradas {cont} pessoas.')

print(f'As pessoas mais pesadas são: ')
for g in pesados:
    print(f'{g[0]} com {g[1]}kilos')
print(f'As pessoas mais leves são:')
for l in leves:
    print(f'{l[0]} com {l[1]}kilos')



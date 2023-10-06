#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

listanum = []
while True:
    listanum.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in "nN":
        break
listanum.sort(reverse=True)
print(f'Você digitou esta lista de números: {listanum}, com um total de {len(listanum)} números.')
if 5 in listanum:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não esta dentro desta lista!')

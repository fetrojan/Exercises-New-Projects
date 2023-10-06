# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
cont = 0
for c in range(1,8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 18:
        cont += 1
print('Das sete pessoas, {} alcançaram a maioridade e {} ainda não.'.format(cont, 7 - cont))





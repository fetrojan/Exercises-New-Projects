#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Digite a distância em kms de sua viagem: '))
if dist <= 200:
    custo = dist * 0.50
    print('Sua viagem por ser mais curta que 200km, vai lhe custar R$0,50 por km, um total de R${:.2f}'.format(custo))
else:
    custo = dist * 0.45
    print('Sua viagem por ser mais longa que 200km, vai lhe custar R$0,45 por km, um total de R${:.2f}'.format(custo))

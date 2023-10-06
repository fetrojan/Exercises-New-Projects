#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
dezoito = homens = mulvint = 0
print('=' * 10, 'CADASTRO DE PESSOAS', '-' * 10)
while True:
    sexo = ' '
    idade = int(input('Qual a idade da pessoa? '))
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulvint += 1
    cadastro = ' '
    while cadastro not in 'SN':
        cadastro = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()
    if cadastro == 'N':
        break
print('-' * 40)
print(f'''Você cadastrou:
Pessoas com mais de dezoito anos: {dezoito}
Total de homens cadastrados:{homens}
Mulheres com menos de vinte anos: {mulvint} ''')

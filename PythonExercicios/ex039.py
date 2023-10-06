#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Em que ano você nasceu soldado? '))
idade = 2022 - ano
if idade == 18:
    print('''Quem nasceu em {}, esta com {} anos,
chegou na hora certa de se alistar, boa sorte aspira!'''.format(ano, idade))
elif idade < 18:
    falta = 18 - idade
    print('''Quem nasceu em {}, esta com {} anos!
Ainda é muito cedo para se alistar soldado, volte daqui {} anos!'''.format(ano, idade, falta))
else:
    passou = idade - 18
    if passou > 1:
        print('''Quem nasceu em {}, esta com {} anos!
Por onde andavas soldado? Ja se passaram {} anos da hora de se alistar!!'''.format(ano, idade, passou))
    else:
        print('''Quem nasceu em {}, esta com {} anos!
Por onde andavas soldado? Ja se passou {} ano da hora de se alistar!!'''.format(ano, idade, passou))



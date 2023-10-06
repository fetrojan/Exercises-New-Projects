#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano = int(input('Informe o ano de nascimento do nadador par ver a qual categoria pertence: '))
idade = date.today().year - ano
if idade <= 9:
    print('Com {} anos de idade, o nadador esta na categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('Com {} anos de idade, o nadador esta na categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('Com {} anos de idade, o nadador esta na categoria JUNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('Com {} anos de idade, o nadador esta na categoria \33[33mSÊNIOR\33[m.'.format(idade))
else:
    print('Com {} anos de idade, o nadador esta na categoria \33[34mMASTER\33[m.'.format(idade))

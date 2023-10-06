# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
maioridade = 0
mulheres = 0
idoso = 0
for p in range(1,5):
    print('******** {}ª PESSOA ********'.format(p))
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(p))).lower()
    if idade > maioridade and sexo == 'm':
        maioridade = idade
        idoso = nome
    media += idade
    if sexo == 'f' and idade < 20:
            mulheres += 1
print('O nome do homem mais velho é {}, que possue {} anos.'.format(idoso, maioridade))
print('A média de idade do grupo é de {:.0f} anos.'.format(media/4))
print('O grupo possue {} mulheres com menos de 20 anos.'.format(mulheres))

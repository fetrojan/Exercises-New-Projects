#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas, o nome com todas as letras minusculas, quantas letras ao todo (sem espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

nome_sep = (nome.split())
nome_ju = "".join(nome_sep)
print('Seu nome completo possue {} letras!'.format(len(nome_ju)))
print('Seu primeiro nome é {}, e possue {} letras'.format(nome_sep[0], len(nome_sep[0])))
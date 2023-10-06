#Crie um program que receba o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
nome = input('Digite o seu nome completo: ').strip()
nome = nome.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))
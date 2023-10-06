#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['Nome']= str(input('Digite o nome do aluno: '))
aluno['Média']= float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média']>7.0:
    aluno['Situaçao']='APROVADO'
else:
    aluno['Situaçao']='REPROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

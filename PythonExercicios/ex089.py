#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()

while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    ficha.append([aluno, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*15)
    opc=int(input('Mostrar as notas de qual aluno? [999 p/ sair] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} foram {ficha[opc][1][0]} e {ficha[opc][1][1]}.')




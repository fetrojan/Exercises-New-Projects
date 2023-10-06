#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input("Primeira nota: "))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2)/2
if media >= 7.0:
    print("Sua média é {}. Parabéns, você foi \33[34mAPROVADO\33[m!".format(media))
elif media < 5.0:
    print('Sua média é {}. Você deveria ter estudado mais, \33[36mREPROVADO\33[m'.format(media))
else:
    print('Sua média ficou {}, mas você ainda tem chances, esta de \33[37mRECUPERAÇÃO\33[m'.format(media))

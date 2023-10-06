#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 15/100
nov_sal = salario + aumento
print('O funcionário que ganhava R${:.2f}, recebeu um aumento de 15% e agora receberá R${:.2f}'.format(salario, nov_sal))
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    aumento = (salario * 0.1)
    print('O seu salário de {}, teve um aumento de 10% (R${}), passando para R${}'.format(salario, aumento, salario + aumento))
else:
    aumento = (salario * 0.15)
    print('O seu salário de {}, teve um aumento de 15% (R${}), passando para R${}'.format(salario, aumento, salario + aumento))



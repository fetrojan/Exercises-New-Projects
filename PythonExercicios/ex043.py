#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Peso: '))
altura = float(input('Altura: '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print('IMC = {:.2f}, você esta abaixo do peso.'.format(IMC))
elif 18.5 <= IMC < 25:
    print('IMC = {:.2f}, você esta no PESO IDEAL!'.format(IMC))
elif 25 <= IMC < 30:
    print('IMC = {:.2f}, você esta no sobrepeso!'.format(IMC))
elif 30 <= IMC < 40:
    print('IMC = {:.2f}, vocÊ está obeso!'.format(IMC))
else:
    print('IMC = {:.2f}, você esta na obesidade mórbida!'.format(IMC))

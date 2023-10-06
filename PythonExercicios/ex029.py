#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre um mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por km acima do limite
v = float(input('Digite a velocidade do veículo em km/h: '))
if v > 80:
    multa = float((v - 80)*7)
    print('Você esta acima do limite de velocidade!! Sua infração lhe custou R${:.1f}!!!'.format(multa))
else:
    print('Tudo certo, continue sua viagem com segurança!')
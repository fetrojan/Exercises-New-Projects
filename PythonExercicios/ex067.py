#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('TABUADA')
print('-' * 30)
while True:
    n = int(input('Digite um número e veja a sua tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} * {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO...Volte sempre!')
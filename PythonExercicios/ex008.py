# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n = float(input('Digite o valor em metros para ser convertido: '))
cm = n*100
mm = n*1000
print('O valor de {} metros, equivale a {:.0f} centimetros ou a {:.0f} milimetros!'.format(n, cm, mm))
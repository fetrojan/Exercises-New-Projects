#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
n = int(input('Determine o primeiro número da sua PA: '))
r = int(input('Determine a razão da sua PA: '))
décimo = n + (10 - 1) * r
for c in range (n, décimo+r, r):
    print('{}'.format(c), end='-> ')
print('ACABOU')




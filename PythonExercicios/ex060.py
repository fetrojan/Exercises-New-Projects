#Faça um programa que leia um número qualquer e mostre o seu fatorial.

'''n = int(input('Digite um número e veja o seu fatorial: '))
c = n
f = 1
print('{}!= '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f), end='')'''

n = int(input('Digite um número e veja o seu fatorial: '))
print('{}! = '.format(n), end='')
f = 1
for c in range(n,0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print('{}'.format(f), end='')


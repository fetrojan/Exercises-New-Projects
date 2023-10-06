# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))

print(f'Os valores digitados foram: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro valor 3, apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')







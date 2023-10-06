#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

valores = []
max = min = 0
for c in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        max = min = valores[c]
    else:
        if valores[c] > max:
            max = valores[c]
        if valores[c] < min:
            min = valores[c]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == max:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}...',end='')
print()


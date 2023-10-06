#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('macaco', 'cachorro', 'leoa', 'galinha', 'elefante', 'tartaruga', 'tigre', 'lobo')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



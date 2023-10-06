#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Banana', 3.90,
            'Maça', 3.50,
            'Abacate', 6.00,
            'Melão', 5.90,
            'Tangerina', 1.50,
            'Laranja', 2.00)
print('-'*26)
print(f'{"LISTAGEM DE FRUTAS":^26}')
print('-'*26)
for pos in range (0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'{listagem[pos]:>5.2f}')


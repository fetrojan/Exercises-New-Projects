#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('A frase {}, invertida fica {}, portanto É UM PALINDROMO!'.format(junto, inverso))
else:
    print('A frase não é um PALINDROMO')'''


frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
inverso = junto[::-1]
if inverso == junto:
    print('A frase {}, invertida fica {}, portanto É UM PALINDROMO!'.format(junto, inverso))
else:
    print('A frase não é um PALINDROMO')
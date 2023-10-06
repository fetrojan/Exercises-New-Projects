#Crie um programa que leia uma frase e mostre: quantas vezes aparece a letra A, em que posição ela aparece pela primeira vez, em que posição ela aparece na ultima vez
frase = input('Digite uma frase: ').lower().strip()
print('A sua frase possue {} letras A nela!'.format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}!'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez na posição {}!'.format(frase.rfind('a')+1))
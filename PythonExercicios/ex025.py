#Crie um programa que leia um nome, e diga se existe SILVA no nome
nome = input('Digite seu nome completo: ').strip()
print("Seu nome tem Silva? {}".format('Silva' in nome.title()))

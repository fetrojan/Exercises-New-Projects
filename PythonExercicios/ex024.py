#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
city = input('Digite o nome da sua cidade: ').strip()
city = city.capitalize()
city = city.split()
print('Santo' in city[0])
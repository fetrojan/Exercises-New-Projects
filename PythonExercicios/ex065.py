#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
cont = soma = maior = menor = media = 0
while resp == 'S':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N}: ')).strip().upper()[0]
media = soma/cont
print('FIM, você digitou um total de {} valores, a média entre eles é {:.2f}. O maior valor digitado foi {} e o menor foi {}'.format(cont, media, maior, menor))



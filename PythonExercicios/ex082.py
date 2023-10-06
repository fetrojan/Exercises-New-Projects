#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listanum = []
pares = []
impares = []

while True:
    n = (int(input('Digite um valor: ')))
    listanum.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar?[S/N] '))
    if r in "nN":
        break
print(f'Você digitou esta lista de números: {listanum}\n'
      f'os números pares são {pares}\n'
      f'e os números impares são {impares}')
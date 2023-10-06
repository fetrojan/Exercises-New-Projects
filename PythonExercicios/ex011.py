#Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la
#Cada litro de tinta pinta 2m²
Altura = float(input('Digite a altura da parede em metros: '))
Largura = float(input('Digite a largura da parede em metros: '))
Area = Altura * Largura
print('Sua parede com {}m de altura e {}m de largura, possue uma área de {:.2f}m², \nportanto necessita de {:.2f}litros de tinta para pinta-la!'.format(Altura, Largura, Area, Area/2))
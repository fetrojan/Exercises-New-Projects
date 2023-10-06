phrase = input('Digite uma frase seu arrombado! ').strip()
print(phrase.lower())
separada = phrase.split()
print(len(separada))
invertida = separada[len(separada)-1] + separada[len(separada)-2] + separada[len(separada)-3]
print(invertida)
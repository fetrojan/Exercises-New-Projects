import random


class Jogador:

    def __init__(self, name):
        self.__name = name
        self.__vitorias = 0
        self.__jogadas = ('pedra', 'papel', 'tesoura')
        
    def fazer_jogada(self):
        return random.choice(self.__jogadas)
    
    def adicionar_vitoria(self):
        self.__vitorias += 1

    def apresentar_vitorias(self):
        return f'{self.__name} tem {self.__vitorias} vitórias!'
    
    def get_name(self):
        return self.__name
    


class Elevador:

    def __init__(self) -> None:
        self.__andar = 1

    def mover_elevador(self, andar):
        if andar < 1 or andar > 15: return self.__mensagem_de_erro()
        else: return self.__alterar_andar(andar)

    def __alterar_andar(self, andar):
        self.__andar = andar
        if andar == 1: return self.__mensagem_elevador_indo_terreo()
        else: return self.__mensagem_alteracao_andar()
    
    def __mensagem_de_erro(self):
        return 'Andar inválido, pressione um andar entre 1 e 15'
    
    def __mensagem_alteracao_andar(self):
        return f'Elevador indo para o {self.__andar}º andar!'
    
    def __mensagem_elevador_indo_terreo(self):
        return f'Elevador indo para o térreo!'
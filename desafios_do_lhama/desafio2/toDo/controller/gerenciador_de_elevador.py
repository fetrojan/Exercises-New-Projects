class Gerenciador_de_Elevador:

    def __init__(self, elevador1, elevador2) -> None:
        self.__elevadores = [elevador1, elevador2]

    def mover_elevador(self, andar, id):
        if (andar <1 or andar > 15): return self.__mensagem_erro_andar()
        else: return self.__checar_elevador_e_selecionar_andar(andar, id)

    def __checar_elevador_e_selecionar_andar(self, andar, id):
        for elevador in self.__elevadores:
            if elevador.check_id(id):
                return self.__mudar_andar(andar, elevador)
        return self.__mensagem_elevador_inexistente()
    
    def __mudar_andar(self, andar, elevador):
        elevador.set_andar(andar)
        if (andar == 1): return self.__mensagem_terreo(elevador)
        return self.__mensagem_alterar_andar(elevador)
    
    def __mensagem_erro_andar(self):
        return "Andar inexistente! Selecione entre o 1º e 15ºandar"
    
    def __mensagem_alterar_andar(self, elevador):
        return f'Elevador {elevador.get_id()} indo para o {elevador.get_andar()}ºandar'
    
    def __mensagem_terreo(self, elevador):
        return f'Elevador {elevador.get_id()} indo para o terreo'
    
    def __mensagem_elevador_inexistente(self):
        return 'Elevador não existe'
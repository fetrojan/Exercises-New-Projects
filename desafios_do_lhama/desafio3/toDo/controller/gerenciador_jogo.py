class GerenciadorJogo:

    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        
    def jogar_rodada(self):
        jogador1_jogada = self.__jogador1.fazer_jogada()
        jogador2_jogada = self.__jogador2.fazer_jogada()
    
        resultado = self.__verificar_jogada(jogador1_jogada, jogador2_jogada)

        if (resultado == 1): self.__jogador1.adicionar_vitoria()
        if (resultado == 2): self.__jogador2.adicionar_vitoria()

        return print (f'{self.__jogador1.get_name()} jogou {jogador1_jogada} e {self.__jogador2.get_name()} jogou {jogador2_jogada} \n O placar fica: \n {self.__apresentar_resultado()}')


    def __verificar_jogada(self, jogador1_jogada, jogador2_jogada):
        if jogador1_jogada == jogador2_jogada: return 0
        if (
            (jogador1_jogada == 'pedra' and jogador2_jogada == 'tesoura')
            or (jogador1_jogada == 'tesoura' and jogador2_jogada == 'papel')
            or (jogador1_jogada == 'papel' and jogador2_jogada == 'pedra')
        ): return 1
        else: return 2

    def __apresentar_resultado(self):
        return f'{self.__jogador1.apresentar_vitorias()} \n {self.__jogador2.apresentar_vitorias()}'
    


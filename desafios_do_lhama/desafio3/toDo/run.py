from controller import GerenciadorJogo
from model import Jogador

jogador1 = Jogador('Felipe')
jogador2 = Jogador('João')

gerenciador = GerenciadorJogo(jogador1, jogador2)

while (True):
    input()
    resultado = gerenciador.jogar_rodada()
    print(resultado)
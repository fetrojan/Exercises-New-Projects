from controller import Gerenciador_de_Elevador
from model import Elevador

elevador1 = Elevador(1)
elevador2 = Elevador(2)
gerenciador_elevador = Gerenciador_de_Elevador(elevador1, elevador2)


while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))

    response = gerenciador_elevador.mover_elevador(andar, elevadorId)

    print(response)

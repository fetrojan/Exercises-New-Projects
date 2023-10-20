from components import Elevador

elevador = Elevador()


while (True):
    andar = int(input('Defina um andar: '))
    response = elevador.mover_elevador(andar)
    print(response)

    

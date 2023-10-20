from planejador_de_viagens import PlanejadorDeViagens
from destinos.belo_horizonte import BeloHorizonte
from destinos.fortaleza import Fortaleza
from destinos.niteroi import Niteroi

planejador_de_viagens = PlanejadorDeViagens()

while (True):
    destino = None

    destino_da_viagem = input('Selecione o destino da viagem: ')
    if destino_da_viagem == '1': destino = BeloHorizonte()
    elif destino_da_viagem == '2': destino = Fortaleza()
    elif destino_da_viagem == '3': destino = Niteroi()

    atividade = planejador_de_viagens.viajar(destino)
    print(atividade)
    print()

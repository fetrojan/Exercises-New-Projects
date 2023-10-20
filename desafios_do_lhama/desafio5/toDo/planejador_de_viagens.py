from typing import Type
from destinos.interface.destinos import DestinoInterface

class PlanejadorDeViagens:

    def viajar(self, destino: Type[DestinoInterface]):
        return destino.atividade()
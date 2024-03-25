from Aeroporto import Aeroporto
from datetime import datetime
from Embraer import Embraer
from Airbus import Airbus
from Boeing import Boeing
from typing import Type
from Aviao import Aviao

class Voo:

    def __init__(self, aeroporto_de_saida: Type[Aeroporto], aeroporto_de_chegada: Type[Aeroporto], horario: Type[datetime], aviao: Type[Aviao]) -> None:
        self.aeroporto_de_saida = aeroporto_de_saida
        self.aeroporto_de_chegada = aeroporto_de_chegada
        self.horario = horario
        self.aviao = aviao

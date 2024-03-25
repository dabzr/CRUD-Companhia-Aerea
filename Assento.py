from Embraer import Embraer
from Airbus import Airbus
from Boeing import Boeing
from typing import Type
from Aviao import Aviao

class Assento:

    def __init__(self, assento_id: str, aviao: Type[Aviao]) -> None:
        self.assento_id = assento_id
        self.aviao = aviao
        self.ocupado = False

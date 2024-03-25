from typing import Type
from Aviao import Aviao

class Assento:

    def __init__(self, assento_id: str, aviao: Type[Aviao]) -> None:
        self.__assento_id = assento_id
        self.aviao = aviao
        self.ocupado =False

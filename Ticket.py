from Assento import Assento
from typing import Type
from Voo import Voo

class Ticket:
    
    def __init__(self, assento: Type[Assento], voo: Type[Voo]) -> None:
        self.assento = assento
        self.voo = voo


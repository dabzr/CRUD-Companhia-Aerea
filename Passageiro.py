from typing import Type
from Usuario import Usuario 

class Passageiro():
    def __init__(self, nome:str, usuario:Type[Usuario]):
        self.nome = nome
        self.usuario = usuario
        pass

    def acessar_tickets():
        pass

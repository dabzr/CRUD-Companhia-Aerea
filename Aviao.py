
class Aviao:

    def __init__(self, nome: str, quantidade_de_assentos: int) -> None:
        self.__nome = nome
        self.__quantidade_de_assentos = quantidade_de_assentos

    def getQuantidadeDeAssentos(self) -> int:
        return self.__quantidade_de_assentos


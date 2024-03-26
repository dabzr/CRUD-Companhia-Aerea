class Usuario:
    def __init__(self, user, senha):
        self.user = user
        self.senha = criptografar_senha(senha)

    def criptografar_senha():
        pass

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = criptografar_senha(value)




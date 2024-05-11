class Carta:

    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    @property
    def valor(self):
        return self._valor

    @property
    def naipe(self):
        return self._naipe

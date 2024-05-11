class Carta:
    VALORES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    NAIPES = ['ouros', 'espadas', 'copas', 'paus']

    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    @property
    def valor(self):
        return self._valor

    @property
    def naipe(self):
        return self._naipe

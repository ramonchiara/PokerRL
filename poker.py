class Carta:
    VALORES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    NAIPES = ['ouros', 'espadas', 'copas', 'paus']

    def __init__(self, valor, naipe):
        if valor not in Carta.VALORES or naipe not in Carta.NAIPES:
            raise ValueError(f'Carta({repr(valor)}, {repr(naipe)}) é inválida.')
        self._valor = valor
        self._naipe = naipe

    @property
    def valor(self):
        return self._valor

    @property
    def naipe(self):
        return self._naipe

    def __repr__(self):
        return f'Carta({repr(self._valor)}, {repr(self._naipe)})'

    def __eq__(self, other):
        return self._valor == other.valor and self._naipe == other.naipe


class Baralho:

    def __init__(self):
        self._cartas = []
        for naipe in Carta.NAIPES:
            for valor in Carta.VALORES:
                self._cartas.append(Carta(valor, naipe))

    @property
    def cartas(self):
        return self._cartas

    def distribuir(self, n):
        return [self.cartas.pop() for _ in range(n)]

    def __len__(self):
        return len(self._cartas)

    def __getitem__(self, item):
        return self._cartas[item]

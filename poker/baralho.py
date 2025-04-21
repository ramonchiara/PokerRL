import random

from poker.carta import Carta


class Baralho:

    def __init__(self):
        self._cartas = [Carta(valor, naipe) for naipe in Carta.NAIPES for valor in Carta.VALORES]

    @property
    def cartas(self):
        return self._cartas

    def embaralhar(self):
        random.shuffle(self._cartas)

    def distribuir(self, n_cartas):
        return [self._cartas.pop() for _ in range(n_cartas)]

    def __eq__(self, other):
        return self._cartas == other.cartas

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return iter(self._cartas)

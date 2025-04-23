from poker.mao import Mao


class Jogador:

    def __init__(self, nome, estrategia_troca):
        self._nome = nome
        self._estrategia_troca = estrategia_troca
        self._mao = None
        self._indices = None

    @property
    def nome(self):
        return self._nome

    @property
    def cartas(self):
        return str(self._mao)

    @property
    def mao(self):
        return self._mao

    @property
    def indices(self):
        return self._indices

    def receber(self, cartas):
        if not self._mao:
            self._mao = Mao(cartas)
        else:
            self._mao.trocar(self._indices, cartas)

    def apostar(self, rodada):
        pass

    def decidir_trocas(self):
        self._indices = self._estrategia_troca.obter_indices_de_troca(self._mao)
        cartas_descartadas = self._mao.cartas_from_indices(self._indices)
        return cartas_descartadas

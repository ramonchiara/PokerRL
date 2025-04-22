import random

from .estrategia_troca import EstrategiaTroca


class EstrategiaTrocaRandomica(EstrategiaTroca):
    def _decidir_trocas(self, mao):
        return random.randrange(2 ** len(mao.cartas))

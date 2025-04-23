import numpy as np

from poker.estrategias_troca.estrategia_troca import EstrategiaTroca
from poker.mao import Mao


class EstrategiaTrocaRL(EstrategiaTroca):
    MIN = 1
    MAX = 5000

    def __init__(self):
        super().__init__()
        self._tabela = np.ones((len(Mao.TIPOS), 2 ** Mao.TAMANHO))

    @property
    def tabela(self):
        return self._tabela

    def _decidir_trocas(self, mao):
        pesos_do_rank = self._tabela[mao.rank]
        probs = pesos_do_rank / pesos_do_rank.sum()
        return int(np.random.choice(len(pesos_do_rank), p=probs))

    def registrar_resultado(self, rank_mao, indices, recompensa):
        trocas = Mao.indices_to_trocas(indices)
        peso = self._tabela[rank_mao, trocas]
        if EstrategiaTrocaRL.MIN <= (peso + recompensa) <= EstrategiaTrocaRL.MAX:
            self._tabela[rank_mao, trocas] += recompensa

    def salvar(self, caminho):
        np.savetxt(caminho, self._tabela, delimiter=';', fmt='%d')

    def carregar(self, caminho):
        try:
            self._tabela = np.loadtxt(caminho, delimiter=';')
        except FileNotFoundError:
            pass

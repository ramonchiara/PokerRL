import numpy as np

from poker.mao import Mao
from poker.estrategias_troca.estrategia_troca import EstrategiaTroca


class EstrategiaTrocaRL(EstrategiaTroca):

    def __init__(self):
        super().__init__()
        self._tabela = np.ones((len(Mao.TIPOS), 2 ** Mao.TAMANHO))

    def _decidir_trocas(self, mao):
        rank_mao = mao.rank
        pesos = self._tabela[rank_mao]
        probs = pesos / pesos.sum()
        return int(np.random.choice(len(pesos), p=probs))

    def registrar_resultado(self, rank_mao, indices, recompensa):
        trocas = Mao.indices_to_trocas(indices)
        peso = self._tabela[rank_mao, trocas]
        if 1 <= (peso + recompensa) <= 1000:
            self._tabela[rank_mao, trocas] += recompensa

    def salvar(self, caminho):
        np.savetxt(caminho, self._tabela, delimiter=';', fmt='%d')

    def carregar(self, caminho):
        try:
            self._tabela = np.loadtxt(caminho, delimiter=';')
        except FileNotFoundError:
            pass

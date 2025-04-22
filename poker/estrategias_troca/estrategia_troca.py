from abc import ABC, abstractmethod


class EstrategiaTroca(ABC):

    def obter_indices_de_troca(self, mao):
        valor = self._decidir_trocas(mao)
        return bin(valor)[2:].zfill(len(mao.cartas))

    @abstractmethod
    def _decidir_trocas(self, mao):
        """ Deve retornar um número inteiro, cujo binário representa as cartas a serem trocadas. """

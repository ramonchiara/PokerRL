from poker.baralho import Baralho
from poker.mao import Mao


class Jogo:

    def __init__(self, jogadores):
        self._jogadores = jogadores
        self._baralho = Baralho()
        self._baralho.embaralhar()

    @property
    def jogadores(self):
        return self._jogadores

    def jogar(self):
        self._distribuir_cartas()
        self._rodada_de_apostas(1)
        self._trocar_cartas()
        self._rodada_de_apostas(2)
        self._mostrar_cartas()
        self._mostrar_ganhadores()

    def _distribuir_cartas(self):
        print('== Distribuindo cartas ==')
        for jogador in self.jogadores:
            cartas = self._baralho.distribuir(Mao.TAMANHO)
            jogador.receber(cartas)

    def _rodada_de_apostas(self, rodada):
        print(f'== {rodada}a rodada de apostas ==')
        for jogador in self.jogadores:
            jogador.apostar(rodada)
            print(f'* {jogador.nome} apostou.')

    def _trocar_cartas(self):
        print('== Troca de cartas ==')
        for jogador in self.jogadores:
            cartas_descartadas = jogador.decidir_trocas()
            n = len(cartas_descartadas)
            novas_cartas = self._baralho.distribuir(n)
            jogador.receber(novas_cartas)
            print(f'* {jogador.nome} trocou {n} cartas.')

    def _mostrar_cartas(self):
        print('== Mostrando as cartas ==')
        for jogador in self.jogadores:
            print(f'* {jogador.nome} tem {jogador.cartas}.')

    def _mostrar_ganhadores(self):
        print('== Ganhadores ==')
        ganhadores = self._determinar_ganhadores()
        print(ganhadores)

    def _determinar_ganhadores(self):
        return []

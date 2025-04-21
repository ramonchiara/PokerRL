from collections import Counter

from poker.carta import Carta


class Mao:
    TAMANHO = 5
    TIPOS = ['maior carta', 'um par', 'dois pares', 'trinca', 'straight', 'flush', 'full house', 'quadra', 'straight flush']

    def __init__(self, cartas):
        n = len(set(cartas))
        if n != Mao.TAMANHO:
            raise ValueError(f'Quantidade inválida de cartas: {n}.')
        self._cartas = cartas
        self._ordena_cartas()

    def _ordena_cartas(self):
        self._cartas = sorted(self._cartas, reverse=True)
        valores = [c.valor for c in self._cartas]
        is_wheel = valores == ['A', 5, 4, 3, 2]
        if is_wheel:
            self._ajusta_ordem_wheel()
        elif self.is_um_par():
            self._ajusta_ordem_um_par(valores)
        elif self.is_dois_pares():
            self._ajusta_ordem_dois_pares(valores)
        elif self.is_trinca():
            self._ajusta_ordem_trinca(valores)
        elif self.is_full_house():
            self._ajusta_ordem_full_house(valores)
        elif self.is_quadra():
            self._ajusta_ordem_quadra(valores)

    def _ajusta_ordem_wheel(self):
        self._cartas = self._cartas[1:] + [self._cartas[0]]

    def _ajusta_ordem_um_par(self, valores):
        if valores[1] == valores[2]:  # 3PP21
            self._cartas = self._cartas[1:3] + [self._cartas[0]] + self._cartas[3:5]
        elif valores[2] == valores[3]:  # 32PP1
            self._cartas = self._cartas[2:4] + self._cartas[0:2] + [self._cartas[4]]
        elif valores[3] == valores[4]:  # 321PP
            self._cartas = self._cartas[3:5] + self._cartas[0:3]

    def _ajusta_ordem_dois_pares(self, valores):
        if valores[0] == valores[1] and valores[3] == valores[4]:  # PPxQQ
            self._cartas = self._cartas[0:2] + self._cartas[3:5] + [self._cartas[2]]
        elif valores[1] == valores[2] and valores[3] == valores[4]:  # xPPQQ
            self._cartas = self._cartas[1:5] + [self._cartas[0]]

    def _ajusta_ordem_trinca(self, valores):
        if valores[1] == valores[2] and valores[2] == valores[3]:  # 2TTT1
            self._cartas = self._cartas[1:4] + [self._cartas[0]] + [self._cartas[4]]
        elif valores[2] == valores[3] and valores[3] == valores[4]:  # 21TTT
            self._cartas = self._cartas[2:5] + self._cartas[0:2]

    def _ajusta_ordem_full_house(self, valores):
        if valores[2] == valores[3] and valores[3] == valores[4]:  # PPTTT
            self._cartas = self._cartas[2:5] + self._cartas[0:2]

    def _ajusta_ordem_quadra(self, valores):
        if valores[1] == valores[2] and valores[2] == valores[3] and valores[3] == valores[4]:  # xQQQQ
            self._cartas = self._cartas[1:5] + [self._cartas[0]]

    @property
    def cartas(self):
        return self._cartas

    @property
    def tipo(self):
        for tipo in reversed(Mao.TIPOS):
            if getattr(self, 'is_' + tipo.replace(' ', '_'))():
                return tipo
        return None  # https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/inconsistent-return-statements.html

    @property
    def rank(self):
        return Mao.TIPOS.index(self.tipo)

    def _is_sequencia(self):
        ranks = [c.indice_valor for c in self._cartas]
        straight = [(self._cartas[0].indice_valor - i) % len(Carta.VALORES) for i in range(len(self._cartas))]
        return ranks == straight

    def _is_mesmo_naipe(self):
        return len(set(c.naipe for c in self._cartas)) == 1

    def is_straight(self):
        return self._is_sequencia() and not self._is_mesmo_naipe()

    def is_flush(self):
        return self._is_mesmo_naipe() and not self._is_sequencia()

    def is_straight_flush(self):
        return self._is_sequencia() and self._is_mesmo_naipe()

    def _get_repeticoes(self):
        valores = [c.valor for c in self._cartas]
        quantidades = Counter(valores)
        repetidas = Counter(quantidades.values())
        return tuple(repetidas[n] for n in range(1, Mao.TAMANHO))

    def is_quadra(self):
        return self._get_repeticoes() == (1, 0, 0, 1)

    def is_full_house(self):
        return self._get_repeticoes() == (0, 1, 1, 0)

    def is_trinca(self):
        return self._get_repeticoes() == (2, 0, 1, 0)

    def is_dois_pares(self):
        return self._get_repeticoes() == (1, 2, 0, 0)

    def is_um_par(self):
        return self._get_repeticoes() == (3, 1, 0, 0)

    def is_maior_carta(self):
        return not any([
            self.is_um_par(),
            self.is_dois_pares(),
            self.is_trinca(),
            self.is_straight(),
            self.is_flush(),
            self.is_full_house(),
            self.is_quadra(),
            self.is_straight_flush()
        ])

    def trocar(self, indices, novas_cartas):
        if len(indices) != Mao.TAMANHO:
            raise ValueError(f'Quantidade inválida de quais cartas a trocar: {len(indices)}.')
        if len(novas_cartas) != Mao.quantos_uns(indices):
            raise ValueError(f'Quantidade inválida de novas cartas: {len(novas_cartas)}.')
        self._cartas = self._cartas_from_indices(indices, '0')
        self._cartas += novas_cartas
        self._ordena_cartas()

    def cartas_from_indices(self, indices):
        return self._cartas_from_indices(indices, '1')

    def _cartas_from_indices(self, indices, flag):
        return [carta for carta, troca in zip(self._cartas, indices) if troca == flag]

    @staticmethod
    def quantos_uns(quais):
        return sum(int(b) for b in quais)

    @staticmethod
    def trocas_to_bin(trocas):
        return bin(trocas)[2:].zfill(Mao.TAMANHO)

    def __str__(self):
        return ''.join([str(c) for c in self._cartas])

    def __eq__(self, other):
        self._checa_sanidade_eq(other)
        return self.rank == other.rank

    def _checa_sanidade_eq(self, other):
        if len(set(self.cartas + other.cartas)) != Mao.TAMANHO * 2:
            raise ValueError('Mãos com cartas repetidas.')

    def __lt__(self, other):
        return self.rank < other.rank if self != other else self._compara_maior_carta(other)

    def _compara_maior_carta(self, other):
        for i in range(len(self._cartas)):
            if self.cartas[i].indice_valor != other.cartas[i].indice_valor:
                return self.cartas[i].indice_valor < other.cartas[i].indice_valor
        return False

import random


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

    @property
    def rank(self):
        return Carta.VALORES.index(self._valor)

    @property
    def naipe_rank(self):
        return Carta.NAIPES.index(self._naipe)

    @staticmethod
    def get_cartas(texto):
        """Gera uma lista de cartas a partir de um texto do tipo 2o3p10cAe"""
        resultado = []
        valor = ''
        for c in texto:
            if c.isdigit() or c in ['J', 'Q', 'K', 'A'] or not valor:
                valor += c
            else:
                busca_naipe = [naipe for naipe in Carta.NAIPES if naipe[0] == c]
                naipe = busca_naipe[0] if busca_naipe else c
                valor = int(valor) if valor.isdigit() else valor
                resultado.append(Carta(valor, naipe))
                valor = ''
        return resultado

    def __repr__(self):
        return f'Carta({repr(self._valor)}, {repr(self._naipe)})'

    def __eq__(self, other):
        return self._valor == other.valor and self._naipe == other.naipe

    def __lt__(self, other):
        rank1, naipe_rank1 = self.rank, self.naipe_rank
        rank2, naipe_rank2 = other.rank, other.naipe_rank
        return rank1 < rank2 if rank1 != rank2 else naipe_rank1 < naipe_rank2

    def __hash__(self):
        return hash((self._valor, self._naipe))


class Baralho:

    def __init__(self):
        self._cartas = []
        for naipe in Carta.NAIPES:
            for valor in Carta.VALORES:
                self._cartas.append(Carta(valor, naipe))

    @property
    def cartas(self):
        return self._cartas

    def embaralhar(self):
        random.shuffle(self._cartas)

    def distribuir(self, n):
        return [self._cartas.pop() for _ in range(n)]

    def __eq__(self, other):
        return self._cartas == other.cartas

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return iter(self._cartas)


class Mao:
    TAMANHO = 5

    def __init__(self, cartas):
        n = len(set(cartas))
        if n != Mao.TAMANHO:
            raise ValueError(f'Quantidade inválida de cartas: {n}.')
        self._cartas = sorted(cartas)
        self._cartas.reverse()
        self._ajusta_caso_wheel()

    def _ajusta_caso_wheel(self):
        valores = [c.valor for c in self._cartas]
        if valores == ['A', 5, 4, 3, 2]:
            self._cartas = self._cartas[1:] + [self._cartas[0]]

    @property
    def cartas(self):
        return self._cartas

    def is_straight(self):
        ranks = [c.rank for c in self._cartas]
        straight = [(self._cartas[0].rank - i) % len(Carta.VALORES) for i in range(Mao.TAMANHO)]
        return ranks == straight

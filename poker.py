import random
from collections import Counter


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
    def indice_valor(self):
        return Carta.VALORES.index(self._valor)

    @property
    def indice_naipe(self):
        return Carta.NAIPES.index(self._naipe)

    @staticmethod
    def get_cartas(texto):
        """Gera uma lista de cartas a partir de um texto do tipo 2o3p10cAe"""
        resultado = []
        valor = ''
        for c in texto:
            if not valor or c.isdigit() or c in ['J', 'Q', 'K', 'A']:
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

    def __str__(self):
        return f'{self._valor}{self._naipe[0]}'

    def __eq__(self, other):
        return self._valor == other.valor and self._naipe == other.naipe

    def __lt__(self, other):
        v1, n1 = self.indice_valor, self.indice_naipe
        v2, n2 = other.indice_valor, other.indice_naipe
        return v1 < v2 if v1 != v2 else n1 < n2

    def __hash__(self):
        return hash((self._valor, self._naipe))


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
        straight = [(self._cartas[0].indice_valor - i) % len(Carta.VALORES) for i in range(Mao.TAMANHO)]
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

    def trocar(self, quais, novas_cartas):
        if len(quais) != Mao.TAMANHO:
            raise ValueError(f'Quantidade inválida de quais cartas a trocar: {len(quais)}.')
        if len(novas_cartas) != Mao.quantos_uns(quais):
            raise ValueError(f'Quantidade inválida de novas cartas: {len(novas_cartas)}.')
        self._cartas = [carta for carta, troca in zip(self._cartas, quais) if troca == '0']
        self._cartas += novas_cartas
        self._ordena_cartas()

    @staticmethod
    def quantos_uns(quais):
        return sum(int(b) for b in quais)

    @staticmethod
    def trocas_to_bin(trocas):
        return bin(trocas)[2:].zfill(Mao.TAMANHO)

    def __str__(self):
        return ''.join([str(c) for c in self.cartas])

    def __eq__(self, other):
        self._checa_sanidade_eq(other)
        return self.rank == other.rank

    def _checa_sanidade_eq(self, other):
        if len(set(self.cartas + other.cartas)) != Mao.TAMANHO * 2:
            raise ValueError('Mãos com cartas repetidas.')

    def __lt__(self, other):
        return self.rank < other.rank if self != other else self._compara_maior_carta(other)

    def _compara_maior_carta(self, other):
        for i in range(Mao.TAMANHO):
            if self.cartas[i].indice_valor != other.cartas[i].indice_valor:
                return self.cartas[i].indice_valor < other.cartas[i].indice_valor
        return False


if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()

    mao1 = Mao(baralho.distribuir(Mao.TAMANHO))
    mao2 = Mao(baralho.distribuir(Mao.TAMANHO))

    trocas1 = random.randrange(2 ** Mao.TAMANHO)
    trocas2 = random.randrange(2 ** Mao.TAMANHO)

    quais1 = bin(trocas1)[2:].zfill(Mao.TAMANHO)
    quais2 = bin(trocas2)[2:].zfill(Mao.TAMANHO)

    quantas1 = sum(int(b) for b in quais1)
    quantas2 = sum(int(b) for b in quais2)

    novas_cartas1 = baralho.distribuir(quantas1)
    novas_cartas2 = baralho.distribuir(quantas2)

    print(f'Mão 1 = {mao1} ({mao1.tipo}) - vou trocar {quais1} por {"".join([str(c) for c in novas_cartas1])}')
    print(f'Mão 2 = {mao2} ({mao2.tipo}) - vou trocar {quais2} por {"".join([str(c) for c in novas_cartas2])}')

    mao1.trocar(quais1, novas_cartas1)
    mao2.trocar(quais2, novas_cartas2)
    print('--- TROCAS EFETUADAS ---')

    ganhou = 1 if mao2 < mao1 else 2 if mao1 < mao2 else 0  # pylint: disable=C0103
    print(f'Mão 1 = {mao1} ({mao1.tipo}) {"*** VENCEU POR POUCO ***" if mao1 == mao2 and ganhou == 1 else "*** VENCEDOR ***" if mao1 != mao2 and ganhou == 1 else ""}')
    print(f'Mão 2 = {mao2} ({mao2.tipo}) {"*** VENCEU POR POUCO ***" if mao1 == mao2 and ganhou == 2 else "*** VENCEDOR ***" if mao1 != mao2 and ganhou == 2 else ""}')
    if ganhou == 0:
        print('*** EMPATE ***')

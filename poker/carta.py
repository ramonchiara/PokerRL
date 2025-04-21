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

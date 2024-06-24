import unittest

from poker import Carta, Baralho, Mao


class CartaTest(unittest.TestCase):

    def test_quero_poder_criar_um_2_de_ouros(self):
        c = Carta(2, 'ouros')
        self.assertEqual(2, c.valor)
        self.assertEqual('ouros', c.naipe)

    def test_quero_saber_quais_valores_e_naipes_posso_usar(self):
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], Carta.VALORES)
        self.assertEqual(['ouros', 'espadas', 'copas', 'paus'], Carta.NAIPES)

    def test_quero_criar_uma_carta_de_cada_valor_e_naipe(self):
        for valor in Carta.VALORES:
            for naipe in Carta.NAIPES:
                with self.subTest(f'test_quero_poder_criar_um_{valor}_de_{naipe}'):
                    c = Carta(valor, naipe)
                    self.assertEqual(valor, c.valor)
                    self.assertEqual(naipe, c.naipe)

    def test_deve_gerar_excecao_ao_criar_carta_invalida(self):
        exemplos_de_valores_invalidos = [1, 11, '2', '10', 'j', 'q', 'r', 'a', 'V', 'D', 'R']
        exemplos_de_naipes_invalidos = ['Ouros', 'ESPADAS', 'diamonds', 'spades', 'hearts', 'clubs']

        for valor in exemplos_de_valores_invalidos:
            for naipe in Carta.NAIPES:
                with self.subTest(f'test_deve_gerar_excecao_ao_criar_um_{valor}_de_{naipe}'):
                    with self.assertRaises(ValueError) as ctx:
                        Carta(valor, naipe)
                    self.assertEqual(f'Carta({repr(valor)}, {repr(naipe)}) é inválida.', str(ctx.exception))

        for valor in Carta.VALORES:
            for naipe in exemplos_de_naipes_invalidos:
                with self.subTest(f'test_deve_gerar_excecao_ao_criar_um_{valor}_de_{naipe}'):
                    with self.assertRaises(ValueError) as ctx:
                        Carta(valor, naipe)
                    self.assertEqual(f'Carta({repr(valor)}, {repr(naipe)}) é inválida.', str(ctx.exception))

        for valor in exemplos_de_valores_invalidos:
            for naipe in exemplos_de_naipes_invalidos:
                with self.subTest(f'test_deve_gerar_excecao_ao_criar_um_{valor}_de_{naipe}'):
                    with self.assertRaises(ValueError) as ctx:
                        Carta(valor, naipe)
                    self.assertEqual(f'Carta({repr(valor)}, {repr(naipe)}) é inválida.', str(ctx.exception))

    def test_quero_poder_verificar_se_duas_cartas_sao_iguais(self):
        c1 = Carta(2, 'ouros')
        c2 = Carta(2, 'ouros')
        self.assertTrue(c1 == c2)

    def test_repr(self):
        c = Carta(2, 'ouros')
        self.assertEqual("Carta(2, 'ouros')", repr(c))

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto(self):
        testes = [
            ['2o', [Carta(2, 'ouros')]],
            ['3o', [Carta(3, 'ouros')]],
            ['4o', [Carta(4, 'ouros')]],
            ['10o', [Carta(10, 'ouros')]],
            ['Jo', [Carta('J', 'ouros')]],
            ['2e', [Carta(2, 'espadas')]],
            ['10e', [Carta(10, 'espadas')]],
            ['Je', [Carta('J', 'espadas')]],
            ['Qe', [Carta('Q', 'espadas')]],
            ['Kc', [Carta('K', 'copas')]],
            ['Ap', [Carta('A', 'paus')]],
            ['2o3p', [Carta(2, 'ouros'), Carta(3, 'paus')]]
        ]
        for teste in testes:
            texto = teste[0]
            expected = teste[1]
            with self.subTest(f'test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_{texto}'):
                cartas = Carta.get_cartas(texto)
                self.assertEqual(expected, cartas)

    def test_deve_gerar_excecao_ao_criar_carta_invalida_a_partir_de_um_texto(self):
        testes = [
            ['1o', "1, 'ouros'"],
            ['11o', "11, 'ouros'"],
            ['Ro', "'R', 'ouros'"],
            ['2d', "2, 'd'"],
            ['10s', "10, 's'"],
            ['Jh', "'J', 'h'"],
            ['AP', "'A', 'P'"]
        ]
        for teste in testes:
            texto = teste[0]
            expected = teste[1]
            with self.subTest(f'test_deve_gerar_excecao_ao_criar_carta_invalida_{texto}'):
                with self.assertRaises(ValueError) as ctx:
                    Carta.get_cartas(texto)
                self.assertEqual(f"Carta({expected}) é inválida.", str(ctx.exception))

    def test_quero_poder_comparar_cartas(self):
        c1 = Carta(2, 'paus')
        c2 = Carta(3, 'copas')
        c3 = Carta(4, 'espadas')
        c4 = Carta(5, 'ouros')
        self.assertTrue(c1 < c2)
        self.assertTrue(c2 < c3)
        self.assertTrue(c3 < c4)

    def test_apesar_de_nao_valer_para_poker_quero_ordenar_ouros_espadas_copas_e_paus_nessa_ordem(self):
        c1 = Carta(2, 'ouros')
        c2 = Carta(2, 'espadas')
        c3 = Carta(2, 'copas')
        c4 = Carta(2, 'paus')
        self.assertTrue(c1 < c2)
        self.assertTrue(c2 < c3)
        self.assertTrue(c3 < c4)

    def test_indice_valor(self):
        self.assertEqual(0, Carta(2, 'ouros').indice_valor)
        self.assertEqual(1, Carta(3, 'espadas').indice_valor)
        self.assertEqual(2, Carta(4, 'copas').indice_valor)
        self.assertEqual(3, Carta(5, 'paus').indice_valor)
        self.assertEqual(4, Carta(6, 'ouros').indice_valor)
        self.assertEqual(5, Carta(7, 'espadas').indice_valor)
        self.assertEqual(6, Carta(8, 'copas').indice_valor)
        self.assertEqual(7, Carta(9, 'paus').indice_valor)
        self.assertEqual(8, Carta(10, 'ouros').indice_valor)
        self.assertEqual(9, Carta('J', 'espadas').indice_valor)
        self.assertEqual(10, Carta('Q', 'copas').indice_valor)
        self.assertEqual(11, Carta('K', 'paus').indice_valor)
        self.assertEqual(12, Carta('A', 'ouros').indice_valor)

    def test_indice_naipe(self):
        self.assertEqual(0, Carta(2, 'ouros').indice_naipe)
        self.assertEqual(1, Carta(3, 'espadas').indice_naipe)
        self.assertEqual(2, Carta(4, 'copas').indice_naipe)
        self.assertEqual(3, Carta(5, 'paus').indice_naipe)
        self.assertEqual(0, Carta(6, 'ouros').indice_naipe)
        self.assertEqual(1, Carta(7, 'espadas').indice_naipe)
        self.assertEqual(2, Carta(8, 'copas').indice_naipe)
        self.assertEqual(3, Carta(9, 'paus').indice_naipe)
        self.assertEqual(0, Carta(10, 'ouros').indice_naipe)
        self.assertEqual(1, Carta('J', 'espadas').indice_naipe)
        self.assertEqual(2, Carta('Q', 'copas').indice_naipe)
        self.assertEqual(3, Carta('K', 'paus').indice_naipe)
        self.assertEqual(0, Carta('A', 'ouros').indice_naipe)


class BaralhoTest(unittest.TestCase):

    def test_quero_poder_criar_um_baralho_comum_de_52_cartas(self):
        b = Baralho()
        self.assertEqual(52, len(b))
        for valor in Carta.VALORES:
            for naipe in Carta.NAIPES:
                with self.subTest(f'test_{valor}_de_{naipe}_deve_estar_no_baralho'):
                    c = Carta(valor, naipe)
                    self.assertIn(c, b)

    def test_quero_poder_distribuir_n_cartas(self):
        baralho = Baralho()
        cartas = baralho.distribuir(5)
        self.assertEqual(5, len(cartas))
        self.assertEqual(47, len(baralho))
        cartas_iniciais_de_um_baralho_novo = Carta.get_cartas('ApKpQpJp10p')
        self.assertEqual(cartas_iniciais_de_um_baralho_novo, cartas)

    def test_quero_poder_verificar_se_dois_baralhos_sao_iguais(self):
        b1 = Baralho()
        b2 = Baralho()
        self.assertTrue(b1 == b2)

        b1.distribuir(1)
        self.assertFalse(b1 == b2)

        b2.distribuir(1)
        self.assertTrue(b1 == b2)

    def test_quero_poder_embaralhar(self):
        b = Baralho()
        b.embaralhar()

        baralho_novo = Baralho()
        self.assertFalse(b == baralho_novo)

        cartas = b.distribuir(5)
        cartas_iniciais_de_um_baralho_novo = baralho_novo.distribuir(5)
        self.assertNotEqual(cartas_iniciais_de_um_baralho_novo, cartas)


class MaoTest(unittest.TestCase):

    def test_quero_poder_criar_uma_mao_de_poker(self):
        baralho = Baralho()
        cartas = baralho.distribuir(5)
        mao = Mao(cartas)
        self.assertEqual(cartas, mao.cartas)

    def test_deve_gerar_excecao_se_mao_com_menos_de_5_cartas(self):
        with self.assertRaises(ValueError) as ctx:
            baralho = Baralho()
            cartas = baralho.distribuir(4)
            Mao(cartas)
        self.assertEqual('Quantidade inválida de cartas: 4.', str(ctx.exception))

    def test_deve_gerar_excecao_se_mao_com_mais_de_5_cartas(self):
        with self.assertRaises(ValueError) as ctx:
            baralho = Baralho()
            cartas = baralho.distribuir(6)
            Mao(cartas)
        self.assertEqual('Quantidade inválida de cartas: 6.', str(ctx.exception))

    def test_deve_gerar_excecao_se_mao_com_cartas_iguais(self):
        with self.assertRaises(ValueError) as ctx:
            cartas = Carta.get_cartas('2o3o4o5o2o')
            Mao(cartas)
        self.assertEqual('Quantidade inválida de cartas: 4.', str(ctx.exception))

    def test_cartas_da_mao_devem_estar_ordenadas_da_maior_para_a_menor(self):
        testes = [
            ['2o3o4o5o6o', '6o5o4o3o2o'],
            ['4c3e2o4o4p', '4p4c4o3e2o'],
            # casos 54321
            ['5o6e10eJcAe', 'AeJc10e6e5o'],  # maior carta
            ['2o3p4c5e6c', '6c5e4c3p2o'],  # straight
            ['Ae2o3p4c5e', '5e4c3p2oAe'],  # wheel
            ['2o7o9oJoKo', 'KoJo9o7o2o'],  # flush
            ['5p6p7p8p9p', '9p8p7p6p5p'],  # straight fush
            ['10eJeQeKeAe', 'AeKeQeJe10e']  # royal flush
        ]
        for teste in testes:
            texto = teste[0]
            expected = teste[1]
            with self.subTest(f'test_ordem_{texto}_deve_ser_{expected}'):
                mao = Mao(Carta.get_cartas(texto))
                self.assertEqual(Carta.get_cartas(expected), mao.cartas)

    def test_quero_saber_se_mao_is_tipo_e_se_nao_eh_de_outro_tipo(self):
        tipos = [
            'straight_flush',
            'quadra',
            'full_house',
            'flush',
            'straight',
            'trinca',
            'dois_pares',
            'um_par',
            'maior_carta'
        ]
        testes = [
            ['10eJeQeKeAe', 'straight_flush'],
            ['5p6p7p8p9p', 'straight_flush'],
            ['Ae2e3e4e5e', 'straight_flush'],
            ['5o5e5c5p9o', 'quadra'],
            ['7o7e7c8o8e', 'full_house'],
            ['2o7o9oJoKo', 'flush'],
            ['5p6p7p8p10p', 'flush'],
            ['2o3p4c5e6c', 'straight'],
            ['Ae2o3p4c5e', 'straight'],
            ['10eJeQeKeAc', 'straight'],
            ['7o7e7c8o9e', 'trinca'],
            ['7o7e8c8o9e', 'dois_pares'],
            ['5p6p7p8p8c', 'um_par'],
            ['5o6e10eJcAe', 'maior_carta']
        ]
        for teste in testes:
            texto = teste[0]
            expected = teste[1]
            for tipo in tipos:
                with self.subTest(f'test_{texto}_{"is" if tipo == expected else "is_not"}_{tipo}'):
                    mao = Mao(Carta.get_cartas(texto))
                    resultado = getattr(mao, 'is_' + tipo)()
                    self.assertEqual(tipo == expected, resultado)

    def test_quero_saber_os_tipos_de_mao(self):
        self.assertEqual(['maior carta', 'um par', 'dois pares', 'trinca', 'straight', 'flush', 'full house', 'quadra', 'straight flush'], Mao.TIPOS)

    def test_quero_saber_o_tipo_de_mao_e_respectivo_rank(self):
        testes = [
            ['5o6e10eJcAe', 'maior carta'],
            ['5p6p7p8p8c', 'um par'],
            ['7o7e8c8o9e', 'dois pares'],
            ['7o7e7c8o9e', 'trinca'],
            ['10eJeQeKeAc', 'straight'],
            ['5p6p7p8p10p', 'flush'],
            ['7o7e7c8o8e', 'full house'],
            ['5o5e5c5p9o', 'quadra'],
            ['5p6p7p8p9p', 'straight flush']
        ]
        for rank, teste in enumerate(testes):
            texto = teste[0]
            tipo = teste[1]
            with self.subTest(f'test_{texto}_eh_tipo_{tipo.replace(" ", "_")}_com_rank_{rank}'):
                mao = Mao(Carta.get_cartas(texto))
                self.assertEqual(tipo, mao.tipo)
                self.assertEqual(rank, mao.rank)

    def test_quero_poder_comparar_duas_maos_de_tipos_diferentes(self):
        maos_em_ordem = ['5o6e10eJcAe', '5p6p7p8p8c', '7o7e8e8o9e', '2o2e2c8c9c', '10eJeQeKeAc', '5p6p7p8p10p', '7o7e7c8o8e', '4o4e4c4p9o', '5p6p7p8p9p']
        for i in range(len(maos_em_ordem) - 1):
            texto1 = maos_em_ordem[i]
            texto2 = maos_em_ordem[i + 1]
            with self.subTest(f'test_{texto1}_menor_que_{texto2}'):
                m1 = Mao(Carta.get_cartas(texto1))
                m2 = Mao(Carta.get_cartas(texto2))
                self.assertTrue(m1 < m2)
                self.assertFalse(m2 < m1)

    def test_quero_poder_comparar_duas_maos_de_mesmo_tipo_maior_carta_m1_menor_m2(self):
        testes = [
            ['5o6e10eJcAe', '5e6c10cJpAc', False],  # m1 == m2 (empate)
            ['5o6e10eJcKe', '5e6c10cJpAc', True],  # m1 < m2 (1a maior carta)
            ['5o6e10eJcAe', '5e6c10cQpAc', True],  # m1 < m2 (2a maior carta)
            ['5o6e9eJcAe', '5e6c10cJpAc', True],  # m1 < m2 (3a maior carta)
            ['5o6e10eJcAe', '5e7c10cJpAc', True],  # m1 < m2 (4a maior carta)
            ['4o6e10eJcAe', '5e6c10cJpAc', True]  # m1 < m2 (5a maior carta - ou, menor carta)
        ]
        for teste in testes:
            texto1 = teste[0]
            texto2 = teste[1]
            is_menor = teste[2]
            with self.subTest(f'test_{texto1}_{"eh_menor_que" if is_menor else "nao_eh_menor_que"}_{texto2}'):
                m1 = Mao(Carta.get_cartas(texto1))
                m2 = Mao(Carta.get_cartas(texto2))
                self.assertTrue(m1 == m2)
                self.assertEqual(is_menor, m1 < m2)
                self.assertFalse(m2 < m1)

    def test_checa_a_sanidade_na_comparacao_de_maos_nao_pode_ter_cartas_repetidas(self):
        testes = [
            ['5o6e10eJcAe', '5o6e10eJcAe'],
            ['5o6e10eJcAe', '5e6c10cJpAe']
        ]
        for teste in testes:
            texto1 = teste[0]
            texto2 = teste[1]
            with self.subTest(f'test_sanidade_{texto1}_com_{texto2}'):
                m1 = Mao(Carta.get_cartas(texto1))
                m2 = Mao(Carta.get_cartas(texto2))

                with self.assertRaises(ValueError) as ctx:
                    self.assertTrue(m1 == m2)
                self.assertEqual('Mãos com cartas repetidas.', str(ctx.exception))

                with self.assertRaises(ValueError) as ctx:
                    self.assertFalse(m1 < m2)
                self.assertEqual('Mãos com cartas repetidas.', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()

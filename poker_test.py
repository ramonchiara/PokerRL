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

    def test_str(self):
        c = Carta(2, 'ouros')
        self.assertEqual("2o", str(c))

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
            ['10eJeQeKeAe', 'AeKeQeJe10e'],  # royal flush
            # casos PP321
            ['AoAc9e8p7o', 'AcAo9e8p7o'],  # um par PP321
            ['Ao9e9c8p7o', '9c9eAo8p7o'],  # um par 3PP21
            ['Ao9e8c8p7o', '8p8cAo9e7o'],  # um par 32PP1
            ['Ao9e8c7p7o', '7p7oAo9e8c'],  # um par 321PP
            # casos PPQQx
            ['AoAc9e9p7o', 'AcAo9p9e7o'],  # dois pares PPQQx
            ['AoAc9e7p7o', 'AcAo7p7o9e'],  # dois pares PPxQQ
            ['Ao9c9e7p7o', '9c9e7p7oAo'],  # dois pares xPPQQ
            # casos TTT21
            ['9p9c9e7o4p', '9p9c9e7o4p'],  # trinca TTT21
            ['9p7c7e7o4p', '7c7e7o9p4p'],  # trinca 2TTT1
            ['9p7c4e4o4p', '4p4e4o9p7c'],  # trinca 21TTT
            # casos TTTPP
            ['9o9e9c5p5o', '9c9e9o5p5o'],  # full house TTTPP
            ['9o9e5c5p5o', '5p5c5o9e9o'],  # full house PPTTT
            # casos QQQQx
            ['9o9e9c9p7o', '9p9c9e9o7o'],  # quadra QQQQx
            ['9o7o7e7c7p', '7p7c7e7o9o']  # quadra xQQQQ
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

    def test_quero_poder_comparar_duas_maos_de_mesmo_tipo_para_fins_de_desempate(self):
        testes = [
            ['maior carta', '5o6e10eJcAe', '5e6c10cJpAc', True],
            ['maior carta', '5o6e10eJcKe', '5e6c10cJpAc', False],  # maior carta vence
            ['maior carta', '5o6e10eJcAe', '5e6c10cQpAc', False],  # 2a maior carta vence
            ['maior carta', '5o6e9eJcAe', '5e6c10cJpAc', False],  # 3a maior carta vence
            ['maior carta', '5o6e10eJcAe', '5e7c10cJpAc', False],  # 4a maior carta vence
            ['maior carta', '4o6e10eJcAe', '5e6c10cJpAc', False],  # 5a maior carta vence
            ['um par', '3o5e7c9o9e', '3e5c7p9c9p', True],
            ['um par', '3o5e7c8o8e', '3e5c7p9c9p', False],  # maior par vence
            ['um par', '3o5e7c9o9e', '3e5c8p9c9p', False],  # maior carta vence
            ['um par', '3o5e7c9o9e', '3e6c7p9c9p', False],  # 2a maior carta vence
            ['um par', '3o5e7c9o9e', '4e5c7p9c9p', False],  # 3a maior carta vence
            ['dois pares', '3o7e7c9o9e', '3e7o7p9c9p', True],
            ['dois pares', '3o7e7c8o8e', '3e7o7p9c9p', False],  # maior par vence
            ['dois pares', '3o7e7c9o9e', '3e8o8p9c9p', False],  # 2o maior par vence
            ['dois pares', '3o7e7c9o9e', '4e7o7p9c9p', False],  # maior carta vence
            ['trinca', '3o7e8c8o8e', '3e7o9o9c9p', False],  # maior trinca vence
            ['straight', '3o4e5c6o7e', '3e4o5o6c7p', True],
            ['straight', '3o4e5c6o7e', '4o5o6c7c8p', False],  # maior carta vence
            ['flush', '5o6o10oJoAo', '5c6c10cJcAc', True],
            ['flush', '5o6o10oJoKo', '5c6c10cJcAc', False],  # maior carta vence
            ['flush', '5o6o10oJoAo', '5c6c10cQcAc', False],  # 2a maior carta vence
            ['flush', '5o6o9oJoAo', '5c6c10cJcAc', False],  # 3a maior carta vence
            ['flush', '5o6o10oJoAo', '5c7c10cJcAc', False],  # 4a maior carta vence
            ['flush', '4o6o10oJoAo', '5c6c10cJcAc', False],  # 5a maior carta vence
            ['full house', 'AoAe8c8o8e', '7e7o9o9c9p', False],  # maior trinca vence
            ['quadra', 'Ao8p8c8o8e', '7e9e9o9c9p', False],  # maior quadra vence
            ['straight flush', '3o4o5o6o7o', '3c4c5c6c7c', True],
            ['straight flush', '3o4o5o6o7o', '4c5c6c7c8c', False]  # maior carta vence
        ]
        for teste in testes:
            tipo = teste[0]
            texto1 = teste[1]
            texto2 = teste[2]
            empate = teste[3]
            with self.subTest(f'test_{tipo.replace(" ", "_")}_{texto1}_{"empata_com" if empate else "eh_menor_que"}_{texto2}'):
                m1 = Mao(Carta.get_cartas(texto1))
                m2 = Mao(Carta.get_cartas(texto2))
                self.assertEqual(tipo, m1.tipo)
                self.assertEqual(tipo, m2.tipo)
                mesmo_tipo_de_mao = m1 == m2
                self.assertTrue(mesmo_tipo_de_mao)
                self.assertEqual(not empate, m1 < m2)
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

    def test_str(self):
        texto = 'AeJc10e6e5o'
        mao = Mao(Carta.get_cartas(texto))
        self.assertEqual(texto, str(mao))

    def test_quero_poder_trocar_cartas_de_uma_mao(self):
        cartas_iniciais = '6o5o4o3o2o'
        testes = [
            ['00000', '', cartas_iniciais],
            ['00001', 'Kp', 'Kp6o5o4o3o'],
            ['00010', 'Kp', 'Kp6o5o4o2o'],
            ['00100', 'Kp', 'Kp6o5o3o2o'],
            ['01000', 'Kp', 'Kp6o4o3o2o'],
            ['10000', 'Kp', 'Kp5o4o3o2o'],
            ['00011', 'KpQp', 'KpQp6o5o4o'],
            ['00110', 'KpQp', 'KpQp6o5o2o'],
            ['01100', 'KpQp', 'KpQp6o3o2o'],
            ['11000', 'KpQp', 'KpQp4o3o2o'],
            ['00111', 'KpQpJp', 'KpQpJp6o5o'],
            ['01110', 'KpQpJp', 'KpQpJp6o2o'],
            ['11100', 'KpQpJp', 'KpQpJp3o2o'],
            ['01111', 'KpQpJp9p', 'KpQpJp9p6o'],
            ['11110', 'KpQpJp9p', 'KpQpJp9p2o'],
            ['11111', 'KpQpJp9p8p', 'KpQpJp9p8p'],
            ['00101', 'KpQp', 'KpQp6o5o3o'],
            ['01010', 'KpQp', 'KpQp6o4o2o'],
            ['10100', 'KpQp', 'KpQp5o3o2o'],
            ['10101', 'KpQpJp', 'KpQpJp5o3o'],
            ['11101', 'KpQpJp9p', 'KpQpJp9p3o'],
            ['11011', 'KpQpJp9p', 'KpQpJp9p4o'],
            ['10111', 'KpQpJp9p', 'KpQpJp9p5o']
        ]
        for teste in testes:
            quais = teste[0]
            novas_cartas = teste[1]
            expected = teste[2]
            with self.subTest(f'test_{cartas_iniciais}_ao_trocar_{quais}_por_{novas_cartas if novas_cartas else "nada"}_deve_mudar_para_{expected}'):
                mao = Mao(Carta.get_cartas(cartas_iniciais))
                mao.trocar(quais, Carta.get_cartas(novas_cartas))
                self.assertEqual(expected, str(mao))
                self.assertEqual(Mao.TAMANHO, len(mao.cartas))  # sanity_check: conjunto (set) final de cartas deve ter tamanho Mao.TAMANHO

    def test_checa_a_sanidade_na_troca_de_cartas(self):
        cartas_iniciais = '6o5o4o3o2o'
        mao = Mao(Carta.get_cartas(cartas_iniciais))

        # quais deve ter o tamanho de Mao.TAMANHO
        novas_cartas = ''
        for quais in ['0000', '000000']:
            with self.subTest(f'test_trocando_{quais}_em_uma_mao_de_{Mao.TAMANHO}_deve_gerar_excecao'):
                with self.assertRaises(ValueError) as ctx:
                    mao.trocar(quais, Carta.get_cartas(novas_cartas))
                self.assertEqual(f'Quantidade inválida de quais cartas a trocar: {len(quais)}.', str(ctx.exception))

        # quais será um sorteio de 0 a 2^Mao.TAMANHO-1, ou seja, 31 - ao transformar em binário, deve ter tamanho Mao.TAMANHO
        for trocas in range(2 ** Mao.TAMANHO):
            with self.subTest(f'test_ao_transformar_{trocas}_em_binario_deve_ter_tamanho_{Mao.TAMANHO}'):
                quais = Mao.trocas_to_bin(trocas)
                self.assertEqual(Mao.TAMANHO, len(quais))

        # novas_cartas deve ter o tamanho da quantidade de cartas a serem trocadas
        quais = '01010'  # precisa trocar 2
        for novas_cartas in ['Kp', 'KpQpJp']:
            with self.subTest(f'test_trocando_{quais}_por_{novas_cartas}_deve_gerar_excecao'):
                with self.assertRaises(ValueError) as ctx:
                    mao.trocar(quais, Carta.get_cartas(novas_cartas))
                self.assertEqual(f'Quantidade inválida de novas cartas: {len(Carta.get_cartas(novas_cartas))}.', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()

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

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_2o(self):
        cartas = Carta.get_cartas('2o')
        self.assertEqual([Carta(2, 'ouros')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_3o(self):
        cartas = Carta.get_cartas('3o')
        self.assertEqual([Carta(3, 'ouros')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_4o(self):
        cartas = Carta.get_cartas('4o')
        self.assertEqual([Carta(4, 'ouros')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_10o(self):
        cartas = Carta.get_cartas('10o')
        self.assertEqual([Carta(10, 'ouros')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_Jo(self):
        cartas = Carta.get_cartas('Jo')
        self.assertEqual([Carta('J', 'ouros')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_2e(self):
        cartas = Carta.get_cartas('2e')
        self.assertEqual([Carta(2, 'espadas')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_10e(self):
        cartas = Carta.get_cartas('10e')
        self.assertEqual([Carta(10, 'espadas')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_Je(self):
        cartas = Carta.get_cartas('Je')
        self.assertEqual([Carta('J', 'espadas')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_Qe(self):
        cartas = Carta.get_cartas('Qe')
        self.assertEqual([Carta('Q', 'espadas')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_Kc(self):
        cartas = Carta.get_cartas('Kc')
        self.assertEqual([Carta('K', 'copas')], cartas)

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_Ap(self):
        cartas = Carta.get_cartas('Ap')
        self.assertEqual([Carta('A', 'paus')], cartas)

    def test_deve_gerar_excecao_ao_criar_carta_invalida_1o(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('1o')
        self.assertEqual("Carta(1, 'ouros') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_11o(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('11o')
        self.assertEqual("Carta(11, 'ouros') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_Ro(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('Ro')
        self.assertEqual("Carta('R', 'ouros') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_2d(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('2d')
        self.assertEqual("Carta(2, 'd') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_10s(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('10s')
        self.assertEqual("Carta(10, 's') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_Jh(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('Jh')
        self.assertEqual("Carta('J', 'h') é inválida.", str(ctx.exception))

    def test_deve_gerar_excecao_ao_criar_carta_invalida_AP(self):
        with self.assertRaises(ValueError) as ctx:
            Carta.get_cartas('AP')
        self.assertEqual("Carta('A', 'P') é inválida.", str(ctx.exception))

    def test_quero_poder_criar_uma_lista_de_cartas_a_partir_de_um_texto_2o3p(self):
        cartas = Carta.get_cartas('2o3p')
        self.assertEqual([Carta(2, 'ouros'), Carta(3, 'paus')], cartas)

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

    def test_valor_rank(self):
        self.assertEqual(0, Carta(2, 'ouros').rank)
        self.assertEqual(1, Carta(3, 'espadas').rank)
        self.assertEqual(2, Carta(4, 'copas').rank)
        self.assertEqual(3, Carta(5, 'paus').rank)
        self.assertEqual(4, Carta(6, 'ouros').rank)
        self.assertEqual(5, Carta(7, 'espadas').rank)
        self.assertEqual(6, Carta(8, 'copas').rank)
        self.assertEqual(7, Carta(9, 'paus').rank)
        self.assertEqual(8, Carta(10, 'ouros').rank)
        self.assertEqual(9, Carta('J', 'espadas').rank)
        self.assertEqual(10, Carta('Q', 'copas').rank)
        self.assertEqual(11, Carta('K', 'paus').rank)
        self.assertEqual(12, Carta('A', 'ouros').rank)

    def test_naipe_rank(self):
        self.assertEqual(0, Carta(2, 'ouros').naipe_rank)
        self.assertEqual(1, Carta(3, 'espadas').naipe_rank)
        self.assertEqual(2, Carta(4, 'copas').naipe_rank)
        self.assertEqual(3, Carta(5, 'paus').naipe_rank)
        self.assertEqual(0, Carta(6, 'ouros').naipe_rank)
        self.assertEqual(1, Carta(7, 'espadas').naipe_rank)
        self.assertEqual(2, Carta(8, 'copas').naipe_rank)
        self.assertEqual(3, Carta(9, 'paus').naipe_rank)
        self.assertEqual(0, Carta(10, 'ouros').naipe_rank)
        self.assertEqual(1, Carta('J', 'espadas').naipe_rank)
        self.assertEqual(2, Carta('Q', 'copas').naipe_rank)
        self.assertEqual(3, Carta('K', 'paus').naipe_rank)
        self.assertEqual(0, Carta('A', 'ouros').naipe_rank)


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
        mao = Mao(Carta.get_cartas('2o3o4o5o6o'))
        self.assertEqual(Carta.get_cartas('6o5o4o3o2o'), mao.cartas)

        mao = Mao(Carta.get_cartas('4c3e2o4o4p'))
        self.assertEqual(Carta.get_cartas('4p4c4o3e2o'), mao.cartas)

    def test_cartas_da_mao_devem_estar_ordenadas_da_maior_para_a_menor_casos_54321(self):
        maior_carta = Mao(Carta.get_cartas('5o6e10eJcAe'))
        self.assertEqual(Carta.get_cartas('AeJc10e6e5o'), maior_carta.cartas)

        straight = Mao(Carta.get_cartas('2o3p4c5e6c'))
        self.assertEqual(Carta.get_cartas('6c5e4c3p2o'), straight.cartas)

        wheel = Mao(Carta.get_cartas('Ae2o3p4c5e'))
        self.assertEqual(Carta.get_cartas('5e4c3p2oAe'), wheel.cartas)

        flush = Mao(Carta.get_cartas('2o7o9oJoKo'))
        self.assertEqual(Carta.get_cartas('KoJo9o7o2o'), flush.cartas)

        straight_flush = Mao(Carta.get_cartas('5p6p7p8p9p'))
        self.assertEqual(Carta.get_cartas('9p8p7p6p5p'), straight_flush.cartas)

        royal_flush = Mao(Carta.get_cartas('10eJeQeKeAe'))
        self.assertEqual(Carta.get_cartas('AeKeQeJe10e'), royal_flush.cartas)

    def test_mao_is_straight(self):
        straight = Mao(Carta.get_cartas('2o3p4c5e6c'))
        self.assertTrue(straight.is_straight())

        wheel = Mao(Carta.get_cartas('Ae2o3p4c5e'))
        self.assertTrue(wheel.is_straight())

        straight_flush = Mao(Carta.get_cartas('5p6p7p8p9p'))
        self.assertFalse(straight_flush.is_straight())

        royal_flush = Mao(Carta.get_cartas('10eJeQeKeAe'))
        self.assertFalse(royal_flush.is_straight())

    def test_mao_is_flush(self):
        flush = Mao(Carta.get_cartas('5p6p7p8p10p'))
        self.assertTrue(flush.is_flush())

        um_par = Mao(Carta.get_cartas('5p6p7p8p8c'))
        self.assertFalse(um_par.is_flush())

        straight_flush = Mao(Carta.get_cartas('5p6p7p8p9p'))
        self.assertFalse(straight_flush.is_flush())

    def test_mao_is_straight_flush(self):
        straight = Mao(Carta.get_cartas('2o3p4c5e6c'))
        self.assertFalse(straight.is_straight_flush())

        wheel = Mao(Carta.get_cartas('Ae2o3p4c5e'))
        self.assertFalse(wheel.is_straight_flush())

        wheel_flush = Mao(Carta.get_cartas('Ae2e3e4e5e'))
        self.assertTrue(wheel_flush.is_straight_flush())

        straight_flush = Mao(Carta.get_cartas('5p6p7p8p9p'))
        self.assertTrue(straight_flush.is_straight_flush())

        royal_flush = Mao(Carta.get_cartas('10eJeQeKeAe'))
        self.assertTrue(royal_flush.is_straight_flush())

        flush = Mao(Carta.get_cartas('5p6p7p8p10p'))
        self.assertFalse(flush.is_straight_flush())

    def test_mao_is_quadra(self):
        um_par = Mao(Carta.get_cartas('5p6p7p8p8c'))
        self.assertFalse(um_par.is_quadra())

        dois_pares = Mao(Carta.get_cartas('7o7e8c8o9e'))
        self.assertFalse(dois_pares.is_quadra())

        trinca = Mao(Carta.get_cartas('7o7e7c8o9e'))
        self.assertFalse(trinca.is_quadra())

        full_house = Mao(Carta.get_cartas('7o7e7c8o8e'))
        self.assertFalse(full_house.is_quadra())

        quadra = Mao(Carta.get_cartas('5o5e5c5p9o'))
        self.assertTrue(quadra.is_quadra())


if __name__ == '__main__':
    unittest.main()

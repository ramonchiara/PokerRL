import unittest

from poker.carta import Carta


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


if __name__ == '__main__':
    unittest.main()

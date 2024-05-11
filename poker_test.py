import unittest

from poker import Carta


class CartaTest(unittest.TestCase):

    def test_quero_poder_criar_um_2_de_ouros(self):
        c = Carta(2, 'ouros')
        self.assertEqual(2, c.valor)
        self.assertEqual('ouros', c.naipe)

    def test_quero_saber_quais_valores_e_naipes_posso_usar(self):
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], Carta.VALORES)
        self.assertEqual(['ouros', 'espadas', 'copas', 'paus'], Carta.NAIPES)


if __name__ == '__main__':
    unittest.main()

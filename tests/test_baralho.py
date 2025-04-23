import unittest

from poker.baralho import Baralho
from poker.carta import Carta


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

    def test_quero_poder_distribuir_n_cartas_pre_determinadas(self):
        baralho = Baralho()
        baralho.embaralhar()
        cartas = baralho.distribuir(5, '9c9e9o5p5o')
        self.assertEqual(5, len(cartas))
        self.assertEqual(47, len(baralho))
        self.assertFalse(Carta(9, 'copas') in baralho)
        self.assertFalse(Carta(9, 'espadas') in baralho)
        self.assertFalse(Carta(9, 'ouros') in baralho)
        self.assertFalse(Carta(5, 'paus') in baralho)
        self.assertFalse(Carta(5, 'ouros') in baralho)


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


if __name__ == '__main__':
    unittest.main()

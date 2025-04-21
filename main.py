import random

from poker.baralho import Baralho
from poker.mao import Mao

if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()

    mao1 = Mao(baralho.distribuir(Mao.TAMANHO))
    mao2 = Mao(baralho.distribuir(Mao.TAMANHO))

    trocas1 = random.randrange(2 ** Mao.TAMANHO)
    trocas2 = random.randrange(2 ** Mao.TAMANHO)

    quais1 = Mao.trocas_to_bin(trocas1)
    quais2 = Mao.trocas_to_bin(trocas2)

    novas_cartas1 = baralho.distribuir(Mao.quantos_uns(quais1))
    novas_cartas2 = baralho.distribuir(Mao.quantos_uns(quais2))

    print(f'Mão 1 = {mao1} ({mao1.tipo}) - vou trocar {quais1} por {"".join([str(c) for c in novas_cartas1])}')
    print(f'Mão 2 = {mao2} ({mao2.tipo}) - vou trocar {quais2} por {"".join([str(c) for c in novas_cartas2])}')

    mao1.trocar(quais1, novas_cartas1)
    mao2.trocar(quais2, novas_cartas2)
    print('--- TROCAS EFETUADAS ---')

    ganhou = 1 if mao2 < mao1 else 2 if mao1 < mao2 else 0  # pylint: disable=C0103
    print(
        f'Mão 1 = {mao1} ({mao1.tipo}) {"*** VENCEU POR POUCO ***" if mao1 == mao2 and ganhou == 1 else "*** VENCEDOR ***" if mao1 != mao2 and ganhou == 1 else ""}')
    print(
        f'Mão 2 = {mao2} ({mao2.tipo}) {"*** VENCEU POR POUCO ***" if mao1 == mao2 and ganhou == 2 else "*** VENCEDOR ***" if mao1 != mao2 and ganhou == 2 else ""}')
    if ganhou == 0:
        print('*** EMPATE ***')

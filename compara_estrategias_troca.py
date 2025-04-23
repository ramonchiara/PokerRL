from poker.baralho import Baralho
from poker.estrategias_troca.estrategia_troca_randomica import EstrategiaTrocaRandomica
from poker.jogador import Jogador
from poker.mao import Mao


def testa_estrategia(quantidade_testes, estrategia):
    estatisticas = {
        'empate': 0.0,
        'melhorou': 0.0,
        'piorou': 0.0
    }

    for _ in range(quantidade_testes):
        # novo jogador
        jogador = Jogador('Teste', estrategia)

        # novo baralho
        baralho = Baralho()
        baralho.embaralhar()

        # distribuir cartas
        cartas = baralho.distribuir(Mao.TAMANHO)
        jogador.receber(cartas)

        # nossa mão atual
        mao_anterior = jogador.mao.rank

        # trocar cartas
        cartas_descartadas = jogador.decidir_trocas()
        n = len(cartas_descartadas)
        novas_cartas = baralho.distribuir(n)
        jogador.receber(novas_cartas)

        # nossa nova mão após trocas
        mao_posterior = jogador.mao.rank

        if mao_posterior > mao_anterior:
            estatisticas['melhorou'] += 1
        elif mao_posterior < mao_anterior:
            estatisticas['piorou'] += 1
        else:
            estatisticas['empate'] += 1

    for tipo, valor in estatisticas.items():
        porcentagem = valor / quantidade_testes * 100.0
        estatisticas[tipo] = porcentagem

    return estatisticas


def main():
    quantidade_testes = 10_000
    estrategia = EstrategiaTrocaRandomica()
    estatisticas = testa_estrategia(quantidade_testes, estrategia)
    for tipo, porcentagem in estatisticas.items():
        print(f'{tipo}: {porcentagem:.1f}%')


if __name__ == '__main__':
    main()

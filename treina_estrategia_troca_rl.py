import matplotlib.pyplot as plt
import numpy as np

from poker.baralho import Baralho
from poker.estrategias_troca.estrategia_troca_rl import EstrategiaTrocaRL
from poker.jogador import Jogador
from poker.mao import Mao


def treinamento(estrategia_troca_rl, cartas):
    # novo jogador
    jogador = Jogador('Treinamento', estrategia_troca_rl)

    # novo baralho
    baralho = Baralho()
    baralho.embaralhar()

    # distribuir cartas
    cartas = baralho.distribuir(Mao.TAMANHO, cartas)
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
        estrategia_troca_rl.registrar_resultado(mao_anterior, jogador.indices, 2)
    elif mao_posterior < mao_anterior:
        estrategia_troca_rl.registrar_resultado(mao_anterior, jogador.indices, -1)
    else:
        estrategia_troca_rl.registrar_resultado(mao_anterior, jogador.indices, 1)


def main():
    arquivo = 'tabela.csv'
    estrategia_troca_rl = EstrategiaTrocaRL()
    estrategia_troca_rl.carregar(arquivo)
    episodios_de_treinamento = 1_000_000
    tipos = [
        'AeJc10e6e5o',  # 'maior carta'
        'AcAo9e8p7o',  # 'um par'
        'AcAo9p9e7o',  # 'dois pares'
        '9p9c9e7o4p',  # 'trinca'
        '6c5e4c3p2o',  # 'straight'
        'KoJo9o7o2o',  # 'flush'
        '9c9e9o5p5o',  # 'full house'
        '9p9c9e9o7o',  # 'quadra'
        '9p8p7p6p5p'  # 'straight flush'
    ]
    for episodio in range(episodios_de_treinamento):
        print(f'Treinamento {episodio} de {episodios_de_treinamento} ({(episodio / episodios_de_treinamento * 100):.1f}%)...')
        if episodio % 1_000 == 0:
            gerar_heatmap(estrategia_troca_rl.tabela, episodio)
        for cartas in tipos:
            treinamento(estrategia_troca_rl, cartas)

    estrategia_troca_rl.salvar(arquivo)


def gerar_heatmap(tabela, episodio):
    plt.figure(figsize=(18, 6))
    heatmap = plt.imshow(tabela, cmap='YlGnBu', aspect='auto')

    plt.title(f'Tabela de Pesos - Estratégia de Troca (RL) - Episódio {episodio}', fontsize=16)
    plt.xlabel('Ações (trocas possíveis)', fontsize=12)
    plt.ylabel('Mãos', fontsize=12)

    cbar = plt.colorbar(heatmap)
    cbar.set_label('Peso', fontsize=12)

    plt.xticks(ticks=np.arange(tabela.shape[1]), labels=[format(i, '05b') for i in range(tabela.shape[1])], fontsize=8, rotation=45)
    plt.yticks(ticks=np.arange(tabela.shape[0]), labels=Mao.TIPOS, fontsize=10)

    plt.tight_layout()
    plt.savefig(f'heatmap-{episodio}')
    plt.close()


if __name__ == '__main__':
    main()

from poker.estrategias_troca.estrategia_troca_randomica import EstrategiaTrocaRandomica
from poker.jogador import Jogador
from poker.jogo import Jogo

if __name__ == '__main__':
    jogador1 = Jogador('Alice', EstrategiaTrocaRandomica())
    jogador2 = Jogador('Bob', EstrategiaTrocaRandomica())
    jogo = Jogo([jogador1, jogador2])
    jogo.jogar()

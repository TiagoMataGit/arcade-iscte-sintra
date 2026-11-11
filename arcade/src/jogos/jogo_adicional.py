"""
Módulo do Mini-Jogo Adicional da Equipa: Jogo do Galo / Tic-Tac-Toe.
Cumpre o requisito de jogo adicional e explora a utilização de Matrizes 3x3 (Critério 8.5).
"""
import random
from typing import List, Optional
from jogos.base_jogo import BaseJogo


class JogoGalo(BaseJogo):
    """
    Implementação orientada a objetos do Jogo do Galo (Tic-Tac-Toe) contra o Computador.
    Utiliza uma matriz 3x3 para representar o estado do tabuleiro.
    """

    def __init__(self):
        super().__init__(
            id_jogo="jogo_adicional",
            nome="Jogo do Galo (Tic-Tac-Toe)",
            descricao="Desafia o computador no clássico tabuleiro 3x3 com recurso a matrizes."
        )

    def get_instructions(self) -> str:
        return (
            "====================================================\n"
            "       INSTRUÇÕES: JOGO DO GALO (TIC-TAC-TOE)       \n"
            "====================================================\n"
            "1. Objetivo: Ser o primeiro a alinhar 3 símbolos (linha, coluna ou diagonal).\n"
            "2. O jogador joga com 'X' e o Computador joga com 'O'.\n"
            "3. O tabuleiro é uma matriz 3x3, numerada de 1 a 9:\n"
            "      1 | 2 | 3 \n"
            "     ---+---+---\n"
            "      4 | 5 | 6 \n"
            "     ---+---+---\n"
            "      7 | 8 | 9 \n"
            "4. Pontuação:\n"
            "   - Vitória: 100 pontos.\n"
            "   - Empate: 50 pontos.\n"
            "   - Derrota: 15 pontos.\n"
            "===================================================="
        )

    def _criar_tabuleiro(self) -> List[List[str]]:
        """Cria e devolve uma matriz vazia 3x3."""
        return [[" " for _ in range(3)] for _ in range(3)]

    def _imprimir_tabuleiro(self, tabuleiro: List[List[str]]) -> None:
        """Apresenta a matriz do tabuleiro na consola de forma visual."""
        print()
        for i, linha in enumerate(tabuleiro):
            print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
            if i < 2:
                print("---+---+---")
        print()

    def _posicao_para_indices(self, pos: int) -> tuple:
        """Converte número de 1 a 9 para coordenadas (linha, coluna) da matriz."""
        idx = pos - 1
        return idx // 3, idx % 3

    def _verificar_vencedor(self, tab: List[List[str]], simbolo: str) -> bool:
        """Verifica se o símbolo completou alguma linha, coluna ou diagonal na matriz."""
        # Verificar linhas
        for linha in tab:
            if all(cell == simbolo for cell in linha):
                return True

        # Verificar colunas
        for col in range(3):
            if all(tab[lin][col] == simbolo for lin in range(3)):
                return True

        # Verificar diagonais
        if tab[0][0] == tab[1][1] == tab[2][2] == simbolo:
            return True
        if tab[0][2] == tab[1][1] == tab[2][0] == simbolo:
            return True

        return False

    def _tabuleiro_cheio(self, tab: List[List[str]]) -> bool:
        """Verifica se todas as posições da matriz estão preenchidas."""
        return all(tab[r][c] != " " for r in range(3) for c in range(3))

    def _obter_posicoes_vazias(self, tab: List[List[str]]) -> List[int]:
        """Devolve lista de posições disponíveis (1 a 9)."""
        vazias = []
        for pos in range(1, 10):
            r, c = self._posicao_para_indices(pos)
            if tab[r][c] == " ":
                vazias.append(pos)
        return vazias

    def play(self, nome_jogador: str) -> int:
        tabuleiro = self._criar_tabuleiro()
        print(f"\n--- [JOGO DO GALO] Bem-vindo, {nome_jogador}! ---")
        print("Tu jogas com 'X' e o computador joga com 'O'.")

        while True:
            self._imprimir_tabuleiro(tabuleiro)

            # Turno do Jogador
            vazias = self._obter_posicoes_vazias(tabuleiro)
            entrada = input(f"Escolhe uma posição livre {vazias} (ou 'sair'): ").strip()

            if entrada.lower() == "sair":
                print("Abandonaste a partida de Jogo do Galo.")
                return 0

            try:
                pos = int(entrada)
            except ValueError:
                print("Por favor, introduz um número válido.")
                continue

            if pos not in vazias:
                print("Posição inválida ou já ocupada! Tenta outra.")
                continue

            lin, col = self._posicao_para_indices(pos)
            tabuleiro[lin][col] = "X"

            # Verificar se jogador ganhou
            if self._verificar_vencedor(tabuleiro, "X"):
                self._imprimir_tabuleiro(tabuleiro)
                print(f"Parabéns {nome_jogador}! Venceste o Jogo do Galo!")
                print("Pontuação conquistada: 100 pontos.\n")
                return 100

            # Verificar empate
            if self._tabuleiro_cheio(tabuleiro):
                self._imprimir_tabuleiro(tabuleiro)
                print("Empate! Nenhum jogador conseguiu a vitória.")
                print("Pontuação conquistada: 50 pontos.\n")
                return 50

            # Turno do Computador
            vazias = self._obter_posicoes_vazias(tabuleiro)
            escolha_pc = random.choice(vazias)
            lin_pc, col_pc = self._posicao_para_indices(escolha_pc)
            tabuleiro[lin_pc][col_pc] = "O"
            print(f">> O computador jogou na posição {escolha_pc}.")

            # Verificar se computador ganhou
            if self._verificar_vencedor(tabuleiro, "O"):
                self._imprimir_tabuleiro(tabuleiro)
                print("O computador venceu desta vez!")
                print("Pontuação de consolação: 15 pontos.\n")
                return 15

            # Verificar empate após jogada do PC
            if self._tabuleiro_cheio(tabuleiro):
                self._imprimir_tabuleiro(tabuleiro)
                print("Empate! O tabuleiro está cheio.")
                print("Pontuação conquistada: 50 pontos.\n")
                return 50


_jogo_instancia = JogoGalo()

def get_name() -> str:
    return _jogo_instancia.nome

def get_instructions() -> str:
    return _jogo_instancia.get_instructions()

def play(nome_jogador: str) -> int:
    return _jogo_instancia.play(nome_jogador)

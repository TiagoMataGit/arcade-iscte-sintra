"""
Módulo do Mini-Jogo: Pedra, Papel ou Tesoura (RF11).
"""
import random
from jogos.base_jogo import BaseJogo


class PedraPapelTesoura(BaseJogo):
    """
    Implementação orientada a objetos do jogo 'Pedra, Papel ou Tesoura'.
    """

    OPCOES = ["pedra", "papel", "tesoura"]
    VITORIAS_NECESSARIAS = 3

    def __init__(self):
        super().__init__(
            id_jogo="pedra_papel_tesoura",
            nome="Pedra, Papel ou Tesoura",
            descricao="Clássica disputa contra o computador. Primeiro a alcançar 3 vitórias vence!"
        )

    def get_instructions(self) -> str:
        return (
            "====================================================\n"
            "       INSTRUÇÕES: PEDRA, PAPEL OU TESOURA          \n"
            "====================================================\n"
            "1. Objetivo: Vencer o computador em sucessivas rondas.\n"
            "2. Regras Clássicas:\n"
            "   - Pedra vence Tesoura\n"
            "   - Tesoura vence Papel\n"
            "   - Papel vence Pedra\n"
            f"3. Fim de Partida: O primeiro a atingir {self.VITORIAS_NECESSARIAS} vitórias vence a partida.\n"
            "4. Pontuação:\n"
            "   - Vitória na partida: 100 pontos base - (20 * derrotas sofridas).\n"
            "   - Derrota na partida: 20 pontos de participação.\n"
            "===================================================="
        )

    def _determinar_vencedor_ronda(self, escolha_jogador: str, escolha_computador: str) -> str:
        """Devolve 'jogador', 'computador' ou 'empate'."""
        if escolha_jogador == escolha_computador:
            return "empate"
        regras = {
            "pedra": "tesoura",
            "tesoura": "papel",
            "papel": "pedra"
        }
        if regras[escolha_jogador] == escolha_computador:
            return "jogador"
        return "computador"

    def play(self, nome_jogador: str) -> int:
        vitorias_jogador = 0
        vitorias_pc = 0
        ronda = 1

        print(f"\n--- [PEDRA, PAPEL OU TESOURA] Bem-vindo, {nome_jogador}! ---")
        print(f"O primeiro a vencer {self.VITORIAS_NECESSARIAS} rondas ganha a partida!\n")

        while vitorias_jogador < self.VITORIAS_NECESSARIAS and vitorias_pc < self.VITORIAS_NECESSARIAS:
            print(f"--- Ronda {ronda} (Placar: {nome_jogador} {vitorias_jogador} x {vitorias_pc} Computador) ---")
            escolha = input("Escolhe [Pedra, Papel, Tesoura] ou 'sair' para desistir: ").strip().lower()

            if escolha == "sair":
                print("Desististe da partida.")
                return 0

            if escolha not in self.OPCOES:
                print("Opção inválida! Escolhe entre 'Pedra', 'Papel' ou 'Tesoura'.")
                continue

            escolha_computador = random.choice(self.OPCOES)
            print(f"Tu escolheste: {escolha.capitalize()} | O Computador escolheu: {escolha_computador.capitalize()}")

            resultado = self._determinar_vencedor_ronda(escolha, escolha_computador)
            if resultado == "jogador":
                vitorias_jogador += 1
                print(f"Parabéns! Venceste a ronda {ronda}!")
            elif resultado == "computador":
                vitorias_pc += 1
                print(f"O computador venceu a ronda {ronda}!")
            else:
                print("Empate nesta ronda!")

            ronda += 1
            print()

        if vitorias_jogador == self.VITORIAS_NECESSARIAS:
            pontos = max(40, 100 - (vitorias_pc * 20))
            print(f"Fim de jogo! {nome_jogador} venceu o computador por {vitorias_jogador} a {vitorias_pc}!")
            print(f"Pontuação conquistada: {pontos} pontos.\n")
            return pontos
        else:
            print(f"Fim de jogo! O computador venceu por {vitorias_pc} a {vitorias_jogador}.")
            print("Pontuação de consolação: 20 pontos.\n")
            return 20


_jogo_instancia = PedraPapelTesoura()

def get_name() -> str:
    return _jogo_instancia.nome

def get_instructions() -> str:
    return _jogo_instancia.get_instructions()

def play(nome_jogador: str) -> int:
    return _jogo_instancia.play(nome_jogador)

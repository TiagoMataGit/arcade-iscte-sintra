"""
Módulo do Mini-Jogo: Adivinha o Número (RF10).
"""
import random
from jogos.base_jogo import BaseJogo


class AdivinhaNumero(BaseJogo):
    """
    Implementação orientada a objetos do jogo 'Adivinha o Número'.
    """

    def __init__(self, limite_min: int = 1, limite_max: int = 100):
        super().__init__(
            id_jogo="adivinha_numero",
            nome="Adivinha o Número",
            descricao="Descobre o número secreto no menor número de tentativas possível."
        )
        self.limite_min = limite_min
        self.limite_max = limite_max

    def get_instructions(self) -> str:
        return (
            "====================================================\n"
            "            INSTRUÇÕES: ADIVINHA O NÚMERO           \n"
            "====================================================\n"
            f"1. Objetivo: Adivinhar o número secreto entre {self.limite_min} e {self.limite_max}.\n"
            "2. Regras: A cada tentativa válida, ser-te-á dito se o número\n"
            "   secreto é MAIOR ou MENOR do que o teu palpite.\n"
            "3. Condições de Vitória: Acertar no número secreto.\n"
            "4. Pontuação: Começas com 100 pontos base. Por cada tentativa\n"
            "   adicional perdes 10 pontos (pontuação mínima: 10 pontos).\n"
            "===================================================="
        )

    def calcular_pontuacao(self, tentativas: int) -> int:
        """Calcula a pontuação final (menos tentativas = mais pontos)."""
        pontuacao = 110 - (tentativas * 10)
        return max(10, pontuacao)

    def play(self, nome_jogador: str) -> int:
        numero_secreto = random.randint(self.limite_min, self.limite_max)
        tentativas = 0

        print(f"\n--- [ADIVINHA O NÚMERO] Bem-vindo, {nome_jogador}! ---")
        print(f"O computador escolheu um número entre {self.limite_min} e {self.limite_max}.")

        while True:
            entrada = input(f"Tentativa #{tentativas + 1} (digite 'sair' para desistir): ").strip()
            if entrada.lower() == "sair":
                print(f"Desististe! O número secreto era {numero_secreto}.")
                return 0

            try:
                palpite = int(entrada)
            except ValueError:
                print("Por favor, introduz um número inteiro válido.")
                continue

            if palpite < self.limite_min or palpite > self.limite_max:
                print(f"Valor fora do intervalo! Deve ser entre {self.limite_min} e {self.limite_max}.")
                continue

            tentativas += 1

            if palpite < numero_secreto:
                print(">> O número secreto é MAIOR! ▲")
            elif palpite > numero_secreto:
                print(">> O número secreto é MENOR! ▼")
            else:
                pontos = self.calcular_pontuacao(tentativas)
                print(f"\nParabéns {nome_jogador}! Acertaste no número {numero_secreto} em {tentativas} tentativa(s)!")
                print(f"Pontuação conquistada: {pontos} pontos.\n")
                return pontos


# Instância global para interface modular padrão (RF9)
_jogo_instancia = AdivinhaNumero()

def get_name() -> str:
    return _jogo_instancia.nome

def get_instructions() -> str:
    return _jogo_instancia.get_instructions()

def play(nome_jogador: str) -> int:
    return _jogo_instancia.play(nome_jogador)

"""
Módulo do Mini-Jogo: Jogo da Forca (RF12).
"""
import os
import random
from typing import List
from jogos.base_jogo import BaseJogo


class JogoDaForca(BaseJogo):
    """
    Implementação orientada a objetos do Jogo da Forca.
    """

    MAX_ERROS = 6

    def __init__(self, caminho_palavras: str = None):
        super().__init__(
            id_jogo="forca",
            nome="Jogo da Forca",
            descricao="Adivinha a palavra secreta letra a letra antes de esgotares os 6 erros permitidos."
        )
        if caminho_palavras is None:
            # Caminho padrão relativo a este ficheiro
            pasta_atual = os.path.dirname(os.path.abspath(__file__))
            self.caminho_palavras = os.path.abspath(os.path.join(pasta_atual, "..", "..", "data", "words.txt"))
        else:
            self.caminho_palavras = caminho_palavras

    def carregar_palavras(self) -> List[str]:
        """Carrega a lista de palavras do ficheiro words.txt com fallback."""
        palavras = []
        if os.path.exists(self.caminho_palavras):
            try:
                with open(self.caminho_palavras, mode="r", encoding="utf-8") as f:
                    palavras = [linha.strip().upper() for linha in f if linha.strip()]
            except Exception as e:
                print(f"[Aviso] Erro ao ler words.txt: {e}")

        # Fallback de emergência caso o ficheiro esteja vazio ou ausente
        if not palavras:
            palavras = ["PYTHON", "ALGORITMO", "ISCTE", "SINTRA", "PROGRAMACAO", "ESTRUTURA"]

        return palavras

    def get_instructions(self) -> str:
        return (
            "====================================================\n"
            "            INSTRUÇÕES: JOGO DA FORCA               \n"
            "====================================================\n"
            "1. Objetivo: Descobrir a palavra secreta antes de cometeres 6 erros.\n"
            "2. Regras:\n"
            "   - Em cada turno, introduz uma única letra.\n"
            "   - Se a letra estiver na palavra, é revelada na posição correta.\n"
            "   - Letras repetidas não descontam erros adicionais, mas são avisadas.\n"
            f"3. Limite de Erros: Tens no máximo {self.MAX_ERROS} erros.\n"
            "4. Pontuação:\n"
            "   - Vitória: 100 pontos - (10 * erros cometidos).\n"
            "   - Derrota: 10 pontos de consolação.\n"
            "===================================================="
        )

    def play(self, nome_jogador: str) -> int:
        palavras = self.carregar_palavras()
        palavra_secreta = random.choice(palavras).upper()
        letras_descobertas = set()
        letras_tentadas = set()
        erros = 0

        print(f"\n--- [JOGO DA FORCA] Bem-vindo, {nome_jogador}! ---")
        print(f"A palavra tem {len(palavra_secreta)} letras. Podes errar até {self.MAX_ERROS} vezes.")

        while erros < self.MAX_ERROS:
            # Apresentar palavra mascarada
            estado = " ".join([letra if letra in letras_descobertas else "_" for letra in palavra_secreta])
            print(f"\nPalavra: {estado}")
            print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}")
            print(f"Erros cometidos: {erros}/{self.MAX_ERROS}")

            entrada = input("Digita uma letra (ou 'sair' para desistir): ").strip().upper()

            if entrada.lower() == "sair":
                print(f"Desististe! A palavra era: {palavra_secreta}")
                return 0

            # Validações de input
            if len(entrada) != 1 or not entrada.isalpha():
                print("Entrada inválida! Por favor introduz apenas uma letra alfabética.")
                continue

            if entrada in letras_tentadas:
                print(f"Atenção: A letra '{entrada}' já foi tentada anteriormente!")
                continue

            letras_tentadas.add(entrada)

            if entrada in palavra_secreta:
                letras_descobertas.add(entrada)
                print(f">> Boa! A letra '{entrada}' existe na palavra!")
                # Verificar vitória
                if all(letra in letras_descobertas for letra in palavra_secreta):
                    pontos = max(20, 100 - (erros * 10))
                    print(f"\nVitória espetacular, {nome_jogador}! Descobriste a palavra: {palavra_secreta}")
                    print(f"Pontuação conquistada: {pontos} pontos.\n")
                    return pontos
            else:
                erros += 1
                print(f">> Que pena! A letra '{entrada}' NÃO existe na palavra.")

        # Derrota
        print(f"\nFim de jogo! Atingiste o limite de {self.MAX_ERROS} erros.")
        print(f"A palavra secreta era: {palavra_secreta}")
        print("Pontuação: 10 pontos.\n")
        return 10


_jogo_instancia = JogoDaForca()

def get_name() -> str:
    return _jogo_instancia.nome

def get_instructions() -> str:
    return _jogo_instancia.get_instructions()

def play(nome_jogador: str) -> int:
    return _jogo_instancia.play(nome_jogador)

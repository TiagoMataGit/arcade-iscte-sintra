"""
Módulo base para os mini-jogos do Arcade (RF9).
Define a interface comum que todos os jogos da plataforma devem respeitar.
"""
from abc import ABC, abstractmethod


class BaseJogo(ABC):
    """
    Classe base abstrata para todos os mini-jogos.
    Garante a modularização e consistência na comunicação com a plataforma Arcade.
    """

    def __init__(self, id_jogo: str, nome: str, descricao: str):
        self._id_jogo = id_jogo
        self._nome = nome
        self._descricao = descricao

    @property
    def id_jogo(self) -> str:
        return self._id_jogo

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def descricao(self) -> str:
        return self._descricao

    @abstractmethod
    def get_instructions(self) -> str:
        """
        Devolve as instruções completas do jogo (objetivo, regras, interação, vitória/derrota e pontuação).
        Requisito RF4.
        """
        pass

    @abstractmethod
    def play(self, nome_jogador: str) -> int:
        """
        Inicia a partida do jogo, controlando a interação e devolvendo a pontuação final obtida.
        Requisitos RF5 e RF6.
        """
        pass

    def __str__(self) -> str:
        return f"{self._nome} ({self._id_jogo}): {self._descricao}"

"""
Módulo da entidade Jogador (RF1).
ISCTE Sintra - Fundamentos de Programação 2026/2027

Classe representativa de um jogador no Arcade.
"""

from datetime import datetime


class Jogador:
    """Classe que representa um jogador no sistema Arcade."""

    def __init__(self, username, nome_apresentacao="", data_criacao=None, data_ultima_utilizacao=None):
        self._username = username
        self._nome_apresentacao = nome_apresentacao if nome_apresentacao else username
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._data_criacao = data_criacao if data_criacao else agora
        self._data_ultima_utilizacao = data_ultima_utilizacao if data_ultima_utilizacao else agora

    # Métodos de acesso (getters e setters)
    def get_username(self):
        return self._username

    def get_nome_apresentacao(self):
        return self._nome_apresentacao

    def set_nome_apresentacao(self, novo_nome):
        if novo_nome and novo_nome.strip():
            self._nome_apresentacao = novo_nome.strip()

    def get_data_criacao(self):
        return self._data_criacao

    def get_data_ultima_utilizacao(self):
        return self._data_ultima_utilizacao

    def atualizar_ultima_utilizacao(self):
        self._data_ultima_utilizacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"Username: {self._username}\n"
            f"Nome de Apresentação: {self._nome_apresentacao}\n"
            f"Data de Registo: {self._data_criacao}\n"
            f"Último Acesso: {self._data_ultima_utilizacao}"
        )

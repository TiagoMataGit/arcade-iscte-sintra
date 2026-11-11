"""
Módulo da entidade Jogador.
Cumpre o requisito RF1 e as boas práticas de Orientação a Objetos (__init__, __str__, getters e setters).
"""
from datetime import datetime


class Jogador:
    """
    Representa um jogador na plataforma Arcade.
    """

    def __init__(self, username: str, nome_apresentacao: str, data_criacao: str = None, data_ultima_utilizacao: str = None):
        """
        Inicializa uma nova instância de Jogador.
        """
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._username = username.strip()
        self._nome_apresentacao = nome_apresentacao.strip()
        self._data_criacao = data_criacao if data_criacao else agora
        self._data_ultima_utilizacao = data_ultima_utilizacao if data_ultima_utilizacao else agora

    # --- Getters e Setters ---

    @property
    def username(self) -> str:
        """Obtém o username único do jogador."""
        return self._username

    @username.setter
    def username(self, novo_username: str) -> None:
        """Define o username do jogador (validando se não é vazio)."""
        if not novo_username or not novo_username.strip():
            raise ValueError("O username não pode ser vazio.")
        self._username = novo_username.strip()

    @property
    def nome_apresentacao(self) -> str:
        """Obtém o nome de apresentação do jogador."""
        return self._nome_apresentacao

    @nome_apresentacao.setter
    def nome_apresentacao(self, novo_nome: str) -> None:
        """Define o nome de apresentação do jogador."""
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome de apresentação não pode ser vazio.")
        self._nome_apresentacao = novo_nome.strip()

    @property
    def data_criacao(self) -> str:
        """Obtém a data e hora de criação do perfil."""
        return self._data_criacao

    @property
    def data_ultima_utilizacao(self) -> str:
        """Obtém a data e hora da última utilização."""
        return self._data_ultima_utilizacao

    @data_ultima_utilizacao.setter
    def data_ultima_utilizacao(self, nova_data: str) -> None:
        """Atualiza a data da última utilização."""
        self._data_ultima_utilizacao = nova_data

    def atualizar_ultima_utilizacao(self) -> None:
        """Atualiza a data de última utilização para o momento atual."""
        self._data_ultima_utilizacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- Métodos de Conversão e Representação ---

    def to_csv_row(self) -> list:
        """Converte os dados do jogador para uma lista correspondente à linha do ficheiro CSV."""
        return [
            self._username,
            self._nome_apresentacao,
            self._data_criacao,
            self._data_ultima_utilizacao
        ]

    @classmethod
    def from_csv_row(cls, row: list) -> "Jogador":
        """Cria uma instância de Jogador a partir de uma linha do ficheiro CSV."""
        return cls(
            username=row[0],
            nome_apresentacao=row[1],
            data_criacao=row[2],
            data_ultima_utilizacao=row[3]
        )

    def __str__(self) -> str:
        """Representação amigável do perfil do jogador em texto."""
        return (
            f"Jogador: {self._nome_apresentacao} (@{self._username})\n"
            f"  - Criado em: {self._data_criacao}\n"
            f"  - Última utilização: {self._data_ultima_utilizacao}"
        )

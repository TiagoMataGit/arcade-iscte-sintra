"""
Módulo de Gestão de Jogadores.
Responsável pelo registo, seleção, validação e persistência em CSV dos jogadores (RF1, RF8).
"""
import os
import csv
from typing import Optional, List, Dict
from jogador import Jogador


class GestorJogadores:
    """
    Controla o ciclo de vida dos jogadores e o jogador atualmente ativo na sessão.
    """

    def __init__(self, caminho_csv: str):
        """
        Inicializa o gestor com o caminho para o ficheiro de jogadores.
        """
        self.caminho_csv = caminho_csv
        self.jogadores: Dict[str, Jogador] = {}
        self.jogador_ativo: Optional[Jogador] = None
        self._inicializar_ficheiro()
        self.carregar_jogadores()

    def _inicializar_ficheiro(self) -> None:
        """Garante que a diretoria e o ficheiro CSV existem com o cabeçalho correto."""
        pasta = os.path.dirname(self.caminho_csv)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)

        if not os.path.exists(self.caminho_csv):
            with open(self.caminho_csv, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["username", "nome_apresentacao", "data_criacao", "data_ultima_utilizacao"])

    def carregar_jogadores(self) -> None:
        """Lê os jogadores do ficheiro CSV para a memória."""
        self.jogadores.clear()
        if not os.path.exists(self.caminho_csv):
            return

        try:
            with open(self.caminho_csv, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)  # Pula o cabeçalho
                for linha in reader:
                    if len(linha) >= 4:
                        jogador = Jogador.from_csv_row(linha)
                        self.jogadores[jogador.username.lower()] = jogador
        except Exception as e:
            print(f"[Aviso] Erro ao carregar jogadores: {e}")

    def guardar_jogadores(self) -> None:
        """Grava todos os jogadores registados no ficheiro CSV."""
        try:
            with open(self.caminho_csv, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["username", "nome_apresentacao", "data_criacao", "data_ultima_utilizacao"])
                for jogador in self.jogadores.values():
                    writer.writerow(jogador.to_csv_row())
        except Exception as e:
            print(f"[Erro] Falha ao guardar dados dos jogadores: {e}")

    def username_existe(self, username: str) -> bool:
        """Verifica se um username já se encontra registado (case-insensitive)."""
        return username.strip().lower() in self.jogadores

    def criar_jogador(self, username: str, nome_apresentacao: str) -> Jogador:
        """
        Cria um novo jogador caso o username não exista e define-o como ativo.
        """
        clean_user = username.strip()
        if not clean_user:
            raise ValueError("O username não pode ser vazio.")
        if self.username_existe(clean_user):
            raise ValueError(f"O username '{clean_user}' já está em uso.")

        clean_nome = nome_apresentacao.strip() if nome_apresentacao.strip() else clean_user
        novo = Jogador(username=clean_user, nome_apresentacao=clean_nome)
        self.jogadores[clean_user.lower()] = novo
        self.jogador_ativo = novo
        self.guardar_jogadores()
        return novo

    def selecionar_jogador(self, username: str) -> Optional[Jogador]:
        """
        Seleciona um jogador existente e define-o como jogador ativo.
        """
        key = username.strip().lower()
        if key in self.jogadores:
            jogador = self.jogadores[key]
            jogador.atualizar_ultima_utilizacao()
            self.jogador_ativo = jogador
            self.guardar_jogadores()
            return jogador
        return None

    def desativar_jogador(self) -> None:
        """Remove o jogador ativo da sessão."""
        self.jogador_ativo = None

    def listar_jogadores(self) -> List[Jogador]:
        """Devolve a lista de todos os jogadores ordenados por nome."""
        return sorted(list(self.jogadores.values()), key=lambda j: j.nome_apresentacao.lower())

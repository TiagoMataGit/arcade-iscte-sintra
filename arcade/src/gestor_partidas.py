"""
Módulo de Gestão de Partidas e Histórico.
Cumpre os requisitos RF5, RF6, RF7 e RF8 (Registo, Histórico cronológico, Rankings e Estatísticas).
"""
import os
import csv
from datetime import datetime
from typing import List, Dict, Any


class Partida:
    """Representa o registo de uma partida terminada."""

    def __init__(self, data_hora: str, username: str, jogo_id: str, jogo_nome: str, pontuacao: int):
        self.data_hora = data_hora
        self.username = username
        self.jogo_id = jogo_id
        self.jogo_nome = jogo_nome
        self.pontuacao = int(pontuacao)

    def to_csv_row(self) -> list:
        return [self.data_hora, self.username, self.jogo_id, self.jogo_nome, str(self.pontuacao)]

    @classmethod
    def from_csv_row(cls, row: list) -> "Partida":
        return cls(
            data_hora=row[0],
            username=row[1],
            jogo_id=row[2],
            jogo_nome=row[3],
            pontuacao=int(row[4])
        )

    def __str__(self) -> str:
        return f"[{self.data_hora}] {self.jogo_nome} | Jogador: @{self.username} | Pontuação: {self.pontuacao} pts"


class GestorPartidas:
    """
    Controla o registo de partidas, histórico, rankings e estatísticas.
    """

    def __init__(self, caminho_csv: str):
        self.caminho_csv = caminho_csv
        self.partidas: List[Partida] = []
        self._inicializar_ficheiro()
        self.carregar_historico()

    def _inicializar_ficheiro(self) -> None:
        """Garante a existência da pasta e do ficheiro com cabeçalho."""
        pasta = os.path.dirname(self.caminho_csv)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)

        if not os.path.exists(self.caminho_csv):
            with open(self.caminho_csv, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["data_hora", "username", "jogo_id", "jogo_nome", "pontuacao"])

    def carregar_historico(self) -> None:
        """Carrega todo o histórico do ficheiro CSV para memória."""
        self.partidas.clear()
        if not os.path.exists(self.caminho_csv):
            return

        try:
            with open(self.caminho_csv, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # Pular cabeçalho
                for linha in reader:
                    if len(linha) >= 5:
                        self.partidas.append(Partida.from_csv_row(linha))
        except Exception as e:
            print(f"[Aviso] Erro ao carregar histórico: {e}")

    def registar_partida(self, username: str, jogo_id: str, jogo_nome: str, pontuacao: int) -> Partida:
        """
        Regista uma partida finalizada e guarda imediatamente no ficheiro persistente.
        """
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        partida = Partida(
            data_hora=agora,
            username=username,
            jogo_id=jogo_id,
            jogo_nome=jogo_nome,
            pontuacao=pontuacao
        )
        self.partidas.append(partida)

        try:
            with open(self.caminho_csv, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(partida.to_csv_row())
        except Exception as e:
            print(f"[Erro] Falha ao gravar partida no histórico: {e}")

        return partida

    def obter_historico(self, filtro_jogo_id: str = None, filtro_username: str = None) -> List[Partida]:
        """
        Devolve as partidas ordenadas cronologicamente (mais recentes primeiro).
        Permite filtros opcionais por jogo e/ou por username.
        """
        resultado = list(self.partidas)

        if filtro_jogo_id:
            resultado = [p for p in resultado if p.jogo_id.lower() == filtro_jogo_id.lower()]

        if filtro_username:
            resultado = [p for p in resultado if p.username.lower() == filtro_username.lower()]

        # Ordenar do mais recente para o mais antigo (cronologia inversa)
        resultado.reverse()
        return resultado

    def obter_ranking_jogo(self, jogo_id: str, top: int = 10) -> List[Dict[str, Any]]:
        """
        Devolve o ranking com as melhores pontuações para um jogo específico.
        """
        partidas_jogo = [p for p in self.partidas if p.jogo_id.lower() == jogo_id.lower()]
        # Ordenar pela pontuação decrescente
        partidas_jogo.sort(key=lambda p: p.pontuacao, reverse=True)

        ranking = []
        for p in partidas_jogo[:top]:
            ranking.append({
                "username": p.username,
                "pontuacao": p.pontuacao,
                "data_hora": p.data_hora
            })
        return ranking

    def obter_estatisticas_jogador(self, username: str) -> Dict[str, Any]:
        """
        Calcula estatísticas de desempenho para um dado jogador.
        """
        partidas_user = [p for p in self.partidas if p.username.lower() == username.lower()]
        total_partidas = len(partidas_user)
        if total_partidas == 0:
            return {
                "total_partidas": 0,
                "pontuacao_total": 0,
                "pontuacao_media": 0.0,
                "melhor_pontuacao": 0
            }

        pontuacao_total = sum(p.pontuacao for p in partidas_user)
        melhor = max(p.pontuacao for p in partidas_user)
        media = round(pontuacao_total / total_partidas, 1)

        return {
            "total_partidas": total_partidas,
            "pontuacao_total": pontuacao_total,
            "pontuacao_media": media,
            "melhor_pontuacao": melhor
        }

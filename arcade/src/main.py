"""
Aplicação Principal - Arcade: Plataforma Modular de Mini-Jogos
ISCTE Sintra - Fundamentos de Programação 2026/2027

Ponto de entrada (entry point) da aplicação.
Gere a autenticação/seleção de jogador, catálogo de jogos, menus interativos,
histórico de pontuações e navegação robusta (RF1 - RF9).
"""
import os
import sys
import json
import importlib
from typing import Dict, Any, List

# Garantir suporte UTF-8 na consola Windows/Linux/macOS
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Adicionar a pasta 'src' ao sys.path para importações absolutas/relativas limpas
DIRETORIA_SRC = os.path.dirname(os.path.abspath(__file__))
if DIRETORIA_SRC not in sys.path:
    sys.path.insert(0, DIRETORIA_SRC)

from gestor_jogadores import GestorJogadores
from gestor_partidas import GestorPartidas


class ArcadePlataforma:
    """
    Controlador central da plataforma Arcade.
    """

    def __init__(self):
        # Resolução de caminhos das pastas de dados
        self.diretoria_base = os.path.abspath(os.path.join(DIRETORIA_SRC, ".."))
        self.diretoria_dados = os.path.join(self.diretoria_base, "data")
        
        caminho_jogadores = os.path.join(self.diretoria_dados, "jogadores.csv")
        caminho_historico = os.path.join(self.diretoria_dados, "historico.csv")
        self.caminho_catalogo = os.path.join(self.diretoria_dados, "jogos.json")

        self.gestor_jogadores = GestorJogadores(caminho_jogadores)
        self.gestor_partidas = GestorPartidas(caminho_historico)
        self.catalogo_jogos: List[Dict[str, Any]] = []
        
        self.carregar_catalogo_jogos()

    def carregar_catalogo_jogos(self) -> None:
        """Carrega o catálogo de jogos a partir do ficheiro jogos.json (RF3, RF8)."""
        if os.path.exists(self.caminho_catalogo):
            try:
                with open(self.caminho_catalogo, mode="r", encoding="utf-8") as f:
                    self.catalogo_jogos = json.load(f)
            except Exception as e:
                print(f"[Aviso] Falha ao ler catálogo jogos.json: {e}")
                self.catalogo_jogos = []
        
        # Caso o catálogo esteja em falta, inicializa com os módulos predefinidos
        if not self.catalogo_jogos:
            self.catalogo_jogos = [
                {"id": "adivinha_numero", "nome": "Adivinha o Número", "descricao": "Descobre o número secreto.", "modulo": "jogos.adivinha_numero", "ativo": True},
                {"id": "pedra_papel_tesoura", "nome": "Pedra, Papel ou Tesoura", "descricao": "Disputa clássica contra o PC.", "modulo": "jogos.pedra_papel_tesoura", "ativo": True},
                {"id": "forca", "nome": "Jogo da Forca", "descricao": "Adivinha a palavra secreta.", "modulo": "jogos.forca", "ativo": True},
                {"id": "jogo_adicional", "nome": "Jogo do Galo (Tic-Tac-Toe)", "descricao": "Jogo da equipa com matrizes 3x3.", "modulo": "jogos.jogo_adicional", "ativo": True}
            ]

    # --- Fluxo de Entrada e Gestão de Sessão ---

    def menu_identificacao(self) -> bool:
        """
        Apresenta o ecrã inicial para identificar ou criar um novo jogador (RF1).
        Devolve True se um jogador foi selecionado, ou False para encerrar.
        """
        while True:
            print("\n" + "=" * 50)
            print("         BEM-VINDO À PLATAFORMA ARCADE            ")
            print("             ISCTE Sintra - 2026/2027             ")
            print("=" * 50)
            print("1. Entrar com jogador existente")
            print("2. Criar novo jogador")
            print("0. Sair da aplicação")
            print("-" * 50)

            opcao = input("Escolhe uma opção: ").strip()

            if opcao == "1":
                jogadores = self.gestor_jogadores.listar_jogadores()
                if not jogadores:
                    print("Ainda não existem jogadores registados! Cria um primeiro.")
                    continue

                print("\n--- Jogadores Registados ---")
                for i, j in enumerate(jogadores, 1):
                    print(f" {i}. @{j.username} ({j.nome_apresentacao})")
                print(" 0. Voltar")

                escolha = input("\nDigita o número ou o username do jogador: ").strip()
                if escolha == "0":
                    continue

                jogador_selecionado = None
                if escolha.isdigit() and 1 <= int(escolha) <= len(jogadores):
                    jogador_selecionado = self.gestor_jogadores.selecionar_jogador(jogadores[int(escolha) - 1].username)
                else:
                    jogador_selecionado = self.gestor_jogadores.selecionar_jogador(escolha)

                if jogador_selecionado:
                    print(f"\nOlá de volta, {jogador_selecionado.nome_apresentacao}!")
                    return True
                else:
                    print("Jogador não encontrado. Tenta novamente.")

            elif opcao == "2":
                print("\n--- Criar Novo Jogador ---")
                username = input("Introduz o username desejado: ").strip()
                if not username:
                    print("O username não pode estar em branco!")
                    continue

                if self.gestor_jogadores.username_existe(username):
                    print(f"Erro: O username '{username}' já se encontra registado!")
                    continue

                nome_apresentacao = input("Introduz o nome de apresentação (ex: Nome Completo): ").strip()
                if not nome_apresentacao:
                    nome_apresentacao = username

                novo = self.gestor_jogadores.criar_jogador(username, nome_apresentacao)
                print(f"\nJogador @{novo.username} ({novo.nome_apresentacao}) criado com sucesso!")
                return True

            elif opcao == "0":
                print("\nObrigado por usar o Arcade. Até breve!")
                return False
            else:
                print("Opção inválida! Por favor tenta novamente.")

    # --- Menu Principal e Submenus ---

    def executar(self) -> None:
        """Ciclo principal de execução da plataforma (RF2)."""
        while True:
            if not self.gestor_jogadores.jogador_ativo:
                sucesso = self.menu_identificacao()
                if not sucesso:
                    break

            jogador = self.gestor_jogadores.jogador_ativo

            print("\n" + "=" * 50)
            print(f" ARCADE :: MENU PRINCIPAL (Sessão: {jogador.nome_apresentacao})")
            print("=" * 50)
            print("1. Jogar mini-jogo")
            print("2. Histórico de partidas")
            print("3. Rankings")
            print("4. Estatísticas")
            print("5. Gerir perfil do jogador")
            print("6. Mudar de jogador")
            print("0. Sair da aplicação")
            print("-" * 50)

            opcao = input("Escolhe uma opção: ").strip()

            if opcao == "1":
                self.menu_jogar()
            elif opcao == "2":
                self.menu_historico()
            elif opcao == "3":
                self.menu_rankings()
            elif opcao == "4":
                self.menu_estatisticas()
            elif opcao == "5":
                self.menu_perfil()
            elif opcao == "6":
                self.gestor_jogadores.desativar_jogador()
                print("Sessão terminada. A redirecionar para seleção de jogador...")
            elif opcao == "0":
                print(f"\nAté logo, {jogador.nome_apresentacao}! A encerrar a plataforma Arcade...")
                break
            else:
                print("Opção inválida! Escolhe uma opção entre 0 e 6.")

    def menu_jogar(self) -> None:
        """Apresenta o catálogo de mini-jogos e executa o jogo escolhido (RF3, RF4, RF5)."""
        while True:
            jogos_disponiveis = [j for j in self.catalogo_jogos if j.get("ativo", True)]
            print("\n--- CATÁLOGO DE MINI-JOGOS DISPONÍVEIS ---")
            for i, j in enumerate(jogos_disponiveis, 1):
                print(f" {i}. {j['nome']} - {j['descricao']}")
            print(" 0. Voltar ao Menu Principal")
            print("-" * 50)

            escolha = input("Seleciona um jogo pelo número: ").strip()
            if escolha == "0":
                break

            if not escolha.isdigit() or not (1 <= int(escolha) <= len(jogos_disponiveis)):
                print("Seleção inválida! Tenta novamente.")
                continue

            info_jogo = jogos_disponiveis[int(escolha) - 1]
            self.gerir_execucao_jogo(info_jogo)

    def gerir_execucao_jogo(self, info_jogo: Dict[str, Any]) -> None:
        """Gere o ciclo de consulta de instruções e execução da partida (RF4, RF5)."""
        try:
            modulo = importlib.import_module(info_jogo["modulo"])
        except Exception as e:
            print(f"[Erro] Falha ao carregar o módulo do jogo '{info_jogo['nome']}': {e}")
            return

        while True:
            print(f"\n=== {info_jogo['nome'].upper()} ===")
            print("1. Iniciar Partida")
            print("2. Consultar Instruções e Regras")
            print("0. Voltar")

            opcao = input("Opção: ").strip()
            if opcao == "1":
                jogador_ativo = self.gestor_jogadores.jogador_ativo
                while True:
                    # Executa a partida através da interface modular comum (RF5, RF9)
                    pontuacao = modulo.play(jogador_ativo.nome_apresentacao)
                    
                    # Regista na plataforma (RF5, RF6)
                    self.gestor_partidas.registar_partida(
                        username=jogador_ativo.username,
                        jogo_id=info_jogo["id"],
                        jogo_nome=info_jogo["nome"],
                        pontuacao=pontuacao
                    )

                    print(f">> Partida registada com sucesso! Pontuação obtida: {pontuacao} pts")
                    
                    dn = input("Queres jogar novamente este jogo? (s/n): ").strip().lower()
                    if dn != "s":
                        break
            elif opcao == "2":
                # Consulta de instruções fornecida pelo próprio módulo (RF4)
                print("\n" + modulo.get_instructions())
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def menu_historico(self) -> None:
        """Apresenta o histórico de partidas com opção de filtragem (RF7)."""
        while True:
            print("\n--- HISTÓRICO DE PARTIDAS ---")
            print("1. Ver todas as partidas (cronológico recente)")
            print("2. Filtrar histórico por jogo")
            print("3. Ver apenas as minhas partidas")
            print("0. Voltar ao Menu Principal")

            opcao = input("Opção: ").strip()
            if opcao == "1":
                partidas = self.gestor_partidas.obter_historico()
                self._apresentar_lista_partidas(partidas)
            elif opcao == "2":
                print("\nJogos disponíveis:")
                for i, j in enumerate(self.catalogo_jogos, 1):
                    print(f" {i}. {j['nome']} (id: {j['id']})")
                
                escolha = input("Indica o número ou ID do jogo: ").strip()
                jogo_id = None
                if escolha.isdigit() and 1 <= int(escolha) <= len(self.catalogo_jogos):
                    jogo_id = self.catalogo_jogos[int(escolha) - 1]["id"]
                else:
                    jogo_id = escolha

                partidas = self.gestor_partidas.obter_historico(filtro_jogo_id=jogo_id)
                self._apresentar_lista_partidas(partidas, titulo=f"Filtrado por jogo '{jogo_id}'")
            elif opcao == "3":
                user = self.gestor_jogadores.jogador_ativo.username
                partidas = self.gestor_partidas.obter_historico(filtro_username=user)
                self._apresentar_lista_partidas(partidas, titulo=f"Partidas de @{user}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def _apresentar_lista_partidas(self, partidas: list, titulo: str = "Todas as Partidas") -> None:
        """Formata e imprime a listagem de partidas."""
        print(f"\n=================== {titulo.upper()} ===================")
        if not partidas:
            print("Nenhuma partida encontrada para os critérios selecionados.")
            print("=" * 60)
            return

        print(f"{'Data/Hora':<20} | {'Jogo':<25} | {'Jogador':<15} | {'Pontos':>6}")
        print("-" * 74)
        for p in partidas:
            print(f"{p.data_hora:<20} | {p.jogo_nome[:24]:<25} | @{p.username[:13]:<14} | {p.pontuacao:>6}")
        print("=" * 74)

    def menu_rankings(self) -> None:
        """Apresenta os rankings dos jogos."""
        print("\n--- RANKINGS DOS JOGOS ---")
        for j in self.catalogo_jogos:
            ranking = self.gestor_partidas.obter_ranking_jogo(j["id"], top=5)
            print(f"\n🏆 Top 5 - {j['nome']}:")
            if not ranking:
                print("   (Ainda sem partidas registadas)")
            else:
                for pos, r in enumerate(ranking, 1):
                    print(f"   {pos}º: @{r['username']} - {r['pontuacao']} pts ({r['data_hora']})")
        print("-" * 50)

    def menu_estatisticas(self) -> None:
        """Mostra as estatísticas do jogador com sessão ativa."""
        user = self.gestor_jogadores.jogador_ativo.username
        stats = self.gestor_partidas.obter_estatisticas_jogador(user)
        print("\n" + "=" * 50)
        print(f"ESTATÍSTICAS DO JOGADOR: @{user}")
        print("=" * 50)
        print(f"• Total de partidas jogadas: {stats['total_partidas']}")
        print(f"• Pontuação acumulada:      {stats['pontuacao_total']} pts")
        print(f"• Pontuação média por jogo: {stats['pontuacao_media']} pts")
        print(f"• Melhor pontuação:         {stats['melhor_pontuacao']} pts")
        print("=" * 50)

    def menu_perfil(self) -> None:
        """Permite visualizar e gerir o perfil do utilizador ativo (RF1)."""
        jogador = self.gestor_jogadores.jogador_ativo
        print("\n" + "=" * 50)
        print("PERFIL DO JOGADOR")
        print("=" * 50)
        print(jogador)
        print("-" * 50)
        print("1. Alterar nome de apresentação")
        print("0. Voltar")
        
        op = input("Opção: ").strip()
        if op == "1":
            novo_nome = input("Novo nome de apresentação: ").strip()
            if novo_nome:
                jogador.nome_apresentacao = novo_nome
                self.gestor_jogadores.guardar_jogadores()
                print("Nome de apresentação atualizado com sucesso!")
            else:
                print("Operação cancelada: nome inválido.")


def main():
    """Função de entrada do programa."""
    try:
        arcade = ArcadePlataforma()
        arcade.executar()
    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo utilizador. Até à próxima!")
    except Exception as e:
        print(f"\n[Erro Inesperado]: {e}")


if __name__ == "__main__":
    main()

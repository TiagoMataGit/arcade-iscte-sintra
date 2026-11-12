"""
Arcade - Plataforma Modular de Mini-Jogos
ISCTE Sintra - Fundamentos de Programação 2026/2027

Fase 1: Interface de Menus e Navegação da Aplicação (RF1 e RF2)
"""

import os
import sys
import csv

# Caminho relativo para a pasta de dados e importações
DIRETORIA_ATUAL = os.path.dirname(os.path.abspath(__file__))
if DIRETORIA_ATUAL not in sys.path:
    sys.path.insert(0, DIRETORIA_ATUAL)

# Importar a classe Jogador a partir do módulo jogador
from jogador import Jogador

CAMINHO_JOGADORES = os.path.join(DIRETORIA_ATUAL, "..", "data", "jogadores.csv")


# ==============================================================================
# GESTÃO E PERSISTÊNCIA DE JOGADORES (RF1, RF8)
# ==============================================================================

def carregar_jogadores():
    """
    Carrega a lista de jogadores a partir do ficheiro jogadores.csv.
    Se o ficheiro não existir, cria-o com o cabeçalho.
    """
    jogadores = []

    # Criar a pasta 'data' caso não exista
    pasta_data = os.path.dirname(CAMINHO_JOGADORES)
    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data, exist_ok=True)

    # Se o ficheiro não existir, cria-o com cabeçalho
    if not os.path.exists(CAMINHO_JOGADORES):
        with open(CAMINHO_JOGADORES, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "nome_apresentacao", "data_criacao", "data_ultima_utilizacao"])
        return jogadores

    # Ler jogadores do ficheiro CSV
    try:
        with open(CAMINHO_JOGADORES, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            cabecalho = next(reader, None)  # Ignorar cabeçalho
            for linha in reader:
                if len(linha) >= 4:
                    jogador = Jogador(
                        username=linha[0].strip(),
                        nome_apresentacao=linha[1].strip(),
                        data_criacao=linha[2].strip(),
                        data_ultima_utilizacao=linha[3].strip()
                    )
                    jogadores.append(jogador)
    except Exception as e:
        print(f"[Aviso] Não foi possível ler o ficheiro de jogadores: {e}")

    return jogadores


def guardar_jogadores(jogadores):
    """
    Guarda todos os jogadores da lista no ficheiro jogadores.csv.
    """
    try:
        with open(CAMINHO_JOGADORES, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "nome_apresentacao", "data_criacao", "data_ultima_utilizacao"])
            for j in jogadores:
                writer.writerow([
                    j.get_username(),
                    j.get_nome_apresentacao(),
                    j.get_data_criacao(),
                    j.get_data_ultima_utilizacao()
                ])
    except Exception as e:
        print(f"[Erro] Falha ao guardar dados dos jogadores: {e}")


# ==============================================================================
# MENU DE ENTRADA / IDENTIFICAÇÃO (RF1)
# ==============================================================================

def menu_identificacao(jogadores):
    """
    Apresenta o menu para selecionar um jogador existente ou criar um novo.
    Retorna o Jogador selecionado ou None se o utilizador optar por sair.
    """
    while True:
        print("\n" + "=" * 50)
        print("         ARCADE - PLATAFORMA DE MINI-JOGOS        ")
        print("            ISCTE Sintra - 2026/2027              ")
        print("=" * 50)
        print("1. Entrar com jogador existente")
        print("2. Criar novo jogador")
        print("0. Sair da aplicação")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if not jogadores:
                print("\n[!] Ainda não existem jogadores registados. Crie um jogador primeiro!")
                continue

            print("\n--- JOGADORES REGISTADOS ---")
            for i in range(len(jogadores)):
                j = jogadores[i]
                print(f"  {i + 1}. {j.get_nome_apresentacao()} (@{j.get_username()})")
            print("  0. Voltar")
            print("-" * 30)

            escolha = input("Selecione o número ou digite o username do jogador: ").strip()
            if escolha == "0":
                continue

            jogador_encontrado = None

            # Tentativa de seleção por número
            if escolha.isdigit():
                num = int(escolha)
                if 1 <= num <= len(jogadores):
                    jogador_encontrado = jogadores[num - 1]

            # Tentativa de seleção por username
            if not jogador_encontrado:
                for j in jogadores:
                    if j.get_username().lower() == escolha.lower():
                        jogador_encontrado = j
                        break

            if jogador_encontrado:
                jogador_encontrado.atualizar_ultima_utilizacao()
                guardar_jogadores(jogadores)
                print(f"\n[OK] Bem-vindo de volta, {jogador_encontrado.get_nome_apresentacao()}!")
                return jogador_encontrado
            else:
                print("\n[!] Jogador não encontrado. Tente novamente.")

        elif opcao == "2":
            print("\n--- CRIAR NOVO JOGADOR ---")
            username = input("Nome de utilizador (username): ").strip()

            if not username:
                print("[!] O username não pode estar vazio.")
                continue

            if "," in username:
                print("[!] O username não pode conter vírgulas.")
                continue

            # Verificar se já existe um jogador com este username
            existe = False
            for j in jogadores:
                if j.get_username().lower() == username.lower():
                    existe = True
                    break

            if existe:
                print(f"[!] Já existe um jogador com o username '{username}'. Escolha outro.")
                continue

            nome_apresentacao = input("Nome de apresentação (opcional - pressione ENTER para usar o username): ").strip()
            if not nome_apresentacao:
                nome_apresentacao = username

            novo_jogador = Jogador(username, nome_apresentacao)
            jogadores.append(novo_jogador)
            guardar_jogadores(jogadores)

            print(f"\n[OK] Jogador '{novo_jogador.get_nome_apresentacao()}' criado com sucesso!")
            return novo_jogador

        elif opcao == "0":
            return None

        else:
            print("\n[!] Opção inválida. Por favor escolha uma das opções apresentadas.")


# ==============================================================================
# SUBMENUS DO ARCADE (RF2, RF3, RF4, RF7)
# ==============================================================================

def menu_jogar():
    """
    Apresenta a lista de jogos disponíveis para seleção.
    """
    while True:
        print("\n" + "=" * 50)
        print("                  CATÁLOGO DE JOGOS               ")
        print("=" * 50)
        print("1. Adivinha o Número")
        print("2. Pedra, Papel ou Tesoura")
        print("3. Jogo da Forca")
        print("4. Jogo Adicional (Jogo do Galo)")
        print("0. Voltar ao Menu Principal")
        print("-" * 50)

        opcao = input("Selecione um jogo para jogar: ").strip()

        jogos_nomes = {
            "1": "Adivinha o Número",
            "2": "Pedra, Papel ou Tesoura",
            "3": "Jogo da Forca",
            "4": "Jogo Adicional (Jogo do Galo)"
        }

        if opcao in jogos_nomes:
            nome_jogo = jogos_nomes[opcao]
            print("\n" + "-" * 50)
            print(f"🎮  {nome_jogo.upper()}")
            print("-" * 50)
            print("Status: Funcionalidade do menu implementada com sucesso!")
            print("Nota: A lógica completa deste jogo será integrada na próxima fase.")
            print("-" * 50)
            input("Pressione ENTER para voltar ao catálogo de jogos...")

        elif opcao == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


def menu_historico():
    """
    Apresenta o submenu do histórico de partidas.
    """
    while True:
        print("\n" + "=" * 50)
        print("                HISTÓRICO DE PARTIDAS             ")
        print("=" * 50)
        print("1. Ver todas as partidas")
        print("2. Filtrar histórico por jogo")
        print("0. Voltar ao Menu Principal")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- TODAS AS PARTIDAS ---")
            print("Ainda não existem partidas registadas no histórico.")
            print("(As partidas serão gravadas automaticamente nas próximas fases)")
            input("\nPressione ENTER para voltar...")

        elif opcao == "2":
            print("\n--- FILTRAR POR JOGO ---")
            print("1. Adivinha o Número")
            print("2. Pedra, Papel ou Tesoura")
            print("3. Jogo da Forca")
            print("4. Jogo Adicional (Jogo do Galo)")
            print("0. Cancelar")
            sub_opcao = input("Selecione o jogo para filtrar: ").strip()
            if sub_opcao in ["1", "2", "3", "4"]:
                print("\nAinda não existem partidas registadas para o jogo selecionado.")
                input("\nPressione ENTER para voltar...")
            elif sub_opcao == "0":
                continue
            else:
                print("\n[!] Opção inválida.")

        elif opcao == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


def menu_rankings(jogadores):
    """
    Apresenta o submenu de rankings.
    """
    while True:
        print("\n" + "=" * 50)
        print("                      RANKINGS                    ")
        print("=" * 50)
        print("1. Todos os jogadores")
        print("2. Filtrar por jogo")
        print("0. Voltar ao Menu Principal")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- RANKING GERAL DE JOGADORES ---")
            if not jogadores:
                print("Sem jogadores registados.")
            else:
                for i in range(len(jogadores)):
                    j = jogadores[i]
                    print(f"  {i + 1}º Lugar: {j.get_nome_apresentacao()} (@{j.get_username()}) - 0 pontos")
            input("\nPressione ENTER para voltar...")

        elif opcao == "2":
            print("\n--- FILTRAR RANKING POR JOGO ---")
            print("1. Adivinha o Número")
            print("2. Pedra, Papel ou Tesoura")
            print("3. Jogo da Forca")
            print("4. Jogo Adicional (Jogo do Galo)")
            print("0. Cancelar")
            sub_opcao = input("Selecione o jogo: ").strip()
            if sub_opcao in ["1", "2", "3", "4"]:
                print("\nAinda não existem pontuações registadas para este jogo.")
                input("\nPressione ENTER para voltar...")
            elif sub_opcao == "0":
                continue
            else:
                print("\n[!] Opção inválida.")

        elif opcao == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


def menu_estatisticas(jogador_ativo):
    """
    Mostra as estatísticas gerais do jogador ativo.
    """
    print("\n" + "=" * 50)
    print("                    ESTATÍSTICAS                  ")
    print("=" * 50)
    print(f"Jogador: {jogador_ativo.get_nome_apresentacao()} (@{jogador_ativo.get_username()})")
    print("• Total de partidas jogadas: 0")
    print("• Pontuação total: 0 pontos")
    print("• Melhor pontuação: 0 pontos")
    print("-" * 50)
    print("(As estatísticas serão atualizadas à medida que realizar partidas)")
    input("\nPressione ENTER para voltar ao Menu Principal...")


def menu_gerir_perfil(jogador_ativo, jogadores):
    """
    Permite consultar e atualizar as informações do jogador ativo.
    """
    while True:
        print("\n" + "=" * 50)
        print("                    GERIR PERFIL                  ")
        print("=" * 50)
        print(jogador_ativo)
        print("-" * 50)
        print("1. Alterar nome de apresentação")
        print("0. Voltar ao Menu Principal")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            novo_nome = input("Introduza o novo nome de apresentação: ").strip()
            if novo_nome:
                jogador_ativo.set_nome_apresentacao(novo_nome)
                guardar_jogadores(jogadores)
                print("\n[OK] Nome de apresentação atualizado com sucesso!")
            else:
                print("\n[!] Nome inválido. Nenhuma alteração foi realizada.")

        elif opcao == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


# ==============================================================================
# MENU PRINCIPAL (RF2)
# ==============================================================================

def menu_principal(jogador_ativo, jogadores):
    """
    Menu principal da aplicação após o jogador ser autenticado.
    Retorna True se for para mudar de jogador, ou False se for para sair da aplicação.
    """
    while True:
        print("\n" + "=" * 50)
        print("                   MENU PRINCIPAL                 ")
        print(f"   Jogador ativo: {jogador_ativo.get_nome_apresentacao()} (@{jogador_ativo.get_username()})")
        print("=" * 50)
        print("1. Jogar")
        print("2. Consultar histórico de partidas")
        print("3. Consultar rankings")
        print("4. Consultar estatísticas")
        print("5. Gerir perfil do jogador")
        print("6. Mudar de jogador")
        print("0. Sair da aplicação")
        print("-" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_jogar()
        elif opcao == "2":
            menu_historico()
        elif opcao == "3":
            menu_rankings(jogadores)
        elif opcao == "4":
            menu_estatisticas(jogador_ativo)
        elif opcao == "5":
            menu_gerir_perfil(jogador_ativo, jogadores)
        elif opcao == "6":
            print(f"\nA terminar sessão de {jogador_ativo.get_nome_apresentacao()}...")
            return True  # Mudar de jogador
        elif opcao == "0":
            return False  # Sair da aplicação
        else:
            print("\n[!] Opção inválida. Por favor, introduza um número válido.")


# ==============================================================================
# PONTO DE ENTRADA (MAIN)
# ==============================================================================

def main():
    """Função principal que coordena o arranque da aplicação Arcade."""
    jogadores = carregar_jogadores()

    while True:
        # 1. Identificação / Criação do Jogador
        jogador_ativo = menu_identificacao(jogadores)

        # Se o jogador escolher sair no menu inicial
        if jogador_ativo is None:
            break

        # 2. Navegação no Menu Principal
        quer_mudar_jogador = menu_principal(jogador_ativo, jogadores)

        # Se o utilizador não quer apenas mudar de jogador, encerra a aplicação
        if not quer_mudar_jogador:
            break

    print("\n" + "=" * 50)
    print("    Obrigado por utilizar o Arcade. Até à próxima!   ")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAplicação terminada. Até à próxima!")

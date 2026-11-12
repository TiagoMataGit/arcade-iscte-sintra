"""
Arcade - Plataforma Modular de Mini-Jogos
ISCTE Sintra - Fundamentos de Programação 2026/2027

Progresso da 1ª Fase: Estrutura inicial de menus e navegação na consola.
"""


def menu_jogar():
    """Menu para seleção de jogos."""
    while True:
        print("\n--- JOGAR ---")
        print("1. Adivinha o Número")
        print("2. Pedra, Papel ou Tesoura")
        print("3. Jogo da Forca")
        print("4. Jogo adicional")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolhe um jogo: ")

        if opcao == "1":
            print("\n[Adivinha o Número - a implementar na próxima fase]")
        elif opcao == "2":
            print("\n[Pedra, Papel ou Tesoura - a implementar na próxima fase]")
        elif opcao == "3":
            print("\n[Jogo da Forca - a implementar na próxima fase]")
        elif opcao == "4":
            print("\n[Jogo adicional - a implementar na próxima fase]")
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tenta novamente.")


def menu_historico():
    """Menu do histórico de partidas."""
    while True:
        print("\n--- HISTÓRICO ---")
        print("1. Todas as partidas")
        print("2. Filtrar por jogo")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            print("\n[Ainda não existem partidas registadas]")
        elif opcao == "2":
            print("\n--- Filtrar por Jogo ---")
            print("1. Adivinha o Número")
            print("2. Pedra, Papel ou Tesoura")
            print("3. Jogo da Forca")
            print("4. Jogo adicional")
            input("Escolhe o jogo para filtrar: ")
            print("[Ainda não existem partidas para este jogo]")
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tenta novamente.")


def menu_rankings():
    """Menu de rankings."""
    while True:
        print("\n--- RANKINGS ---")
        print("1. Todos os jogadores")
        print("2. Filtrar por jogo")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            print("\n[Rankings gerais - a implementar]")
        elif opcao == "2":
            print("\n--- Filtrar Ranking por Jogo ---")
            print("1. Adivinha o Número")
            print("2. Pedra, Papel ou Tesoura")
            print("3. Jogo da Forca")
            print("4. Jogo adicional")
            input("Escolhe o jogo: ")
            print("[Rankings por jogo - a implementar]")
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tenta novamente.")


def menu_perfil(jogador):
    """Menu simples para consulta do perfil."""
    print("\n--- GERIR PERFIL ---")
    print(f"Jogador atual: {jogador}")
    print("[Edição de perfil a implementar nas próximas fases]")
    input("Pressiona ENTER para voltar...")


def menu_principal(jogador):
    """
    Menu principal da aplicação.
    Retorna True se o utilizador quiser mudar de jogador, ou False para sair.
    """
    while True:
        print(f"\n==============================")
        print(f"  MENU PRINCIPAL ({jogador})")
        print(f"==============================")
        print("1. Jogar")
        print("2. Histórico")
        print("3. Rankings")
        print("4. Gerir perfil")
        print("5. Mudar de jogador")
        print("0. Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            menu_jogar()
        elif opcao == "2":
            menu_historico()
        elif opcao == "3":
            menu_rankings()
        elif opcao == "4":
            menu_perfil(jogador)
        elif opcao == "5":
            return True  # Mudar de jogador
        elif opcao == "0":
            return False  # Sair do programa
        else:
            print("Opção inválida! Tenta novamente.")


def main():
    """Ciclo inicial do Arcade."""
    print("========================================")
    print("           BEM-VINDO AO ARCADE          ")
    print("========================================")

    while True:
        print("\n--- ENTRAR / CRIAR JOGADOR ---")
        print("1. Entrar / Criar jogador")
        print("0. Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            nome = input("Introduz o teu nome de jogador: ").strip()
            if nome == "":
                print("Nome inválido! Tenta novamente.")
                continue

            # Entrar no menu principal
            mudar_jogador = menu_principal(nome)
            if not mudar_jogador:
                break
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tenta novamente.")

    print("\nA sair do Arcade... Até à próxima!")


if __name__ == "__main__":
    main()

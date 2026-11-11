# Arcade: Plataforma Modular de Mini-Jogos 🎮

> **ISCTE Sintra - Instituto Universitário de Lisboa**  
> **Unidade Curricular:** Fundamentos de Programação  
> **Ano Letivo:** 2026/2027 – 1º Semestre  
> **Docente Prática:** Prof.ª Catarina Reis (`catarina.reis@iscte-iul.pt`)

---

## 👥 Identificação da Equipa

| Papel | Nome | Número de Aluno | Utilizador GitHub |
|---|---|---|---|
| Aluno 1 | `Tiago Mata` | `139709` | `@TiagoMataGit` |
| Aluno 2 | `[Nome Colega 2]` | `[Preencher]` | `@[utilizador2]` |
| Aluno 3 | `[Nome Colega 3]` | `[Preencher]` | `@[utilizador3]` |

> **Nota para a Entrega:**  
> De acordo com o enunciado oficial, o repositório GitHub final deve ser nomeado segundo a convenção:  
> `licenciatura_NumeroAluno1_NumeroAluno2_NumeroAluno3`  
> *(Exemplo: `tdia_11111_22222_33333` ou `dsa_10101_20202_30303`)* e partilhado com **`catarina.reis@iscte-iul.pt`**.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.10+** instalado (o projeto utiliza **exclusivamente a biblioteca padrão do Python**, em conformidade com os requisitos não-funcionais).
- **VS Code** (ou outro editor à escolha).

### Passos de Execução
1. Abre esta pasta no **VS Code**:
   ```bash
   code .
   ```
2. No terminal integrado do VS Code (`Ctrl + ~`), executa a aplicação:
   ```bash
   python arcade/src/main.py
   ```

---

## 📁 Estrutura de Ficheiros do Projeto

A organização de pastas e módulos respeita a especificação do enunciado:

```text
fp-projeto/
├── .gitignore                      # Ignora ficheiros temporários, pycache e venv
├── README.md                       # Documentação principal da equipa e do projeto
└── arcade/
    ├── data/                       # Armazenamento e persistência de dados
    │   ├── words.txt               # Lista de palavras para o Jogo da Forca
    │   ├── jogadores.csv           # Base de dados persistente de jogadores
    │   ├── jogos.json              # Catálogo configurável de mini-jogos
    │   └── historico.csv           # Registo de histórico de partidas e pontuações
    └── src/                        # Código-fonte Python
        ├── __init__.py
        ├── main.py                 # Menu principal, navegação robusta e controlador
        ├── jogador.py              # Classe Jogador (POO, getters/setters, __str__)
        ├── gestor_jogadores.py     # Gestão, criação, seleção e persistência de jogadores
        ├── gestor_partidas.py      # Gestão de histórico, rankings e estatísticas
        └── jogos/                  # Módulos independentes dos mini-jogos (RF9)
            ├── __init__.py
            ├── base_jogo.py        # Classe abstrata base e contrato comum dos jogos
            ├── adivinha_numero.py  # Mini-jogo: Adivinha o Número (RF10)
            ├── pedra_papel_tesoura.py # Mini-jogo: Pedra, Papel ou Tesoura (RF11)
            ├── forca.py            # Mini-jogo: Jogo da Forca (RF12)
            └── jogo_adicional.py   # Mini-jogo da equipa: Jogo do Galo com Matrizes 3x3 (Critério 8.5)
```

---

## 🎯 Requisitos Implementados

| Requisito | Descrição | Ficheiro Responsável |
|---|---|---|
| **RF1** | Gestão de Jogadores (registo único, seleção, dados básicos, persistência) | `src/jogador.py` e `src/gestor_jogadores.py` |
| **RF2** | Menu Principal e Navegação contínua com tratamento de inputs inválidos | `src/main.py` |
| **RF3** | Catálogo modular de mini-jogos | `data/jogos.json` e `src/main.py` |
| **RF4** | Consulta de instruções específicas de cada jogo | `src/jogos/*.py` |
| **RF5** | Execução de partidas e comunicação de resultados à plataforma | `src/main.py` |
| **RF6** | Sistema de pontuação diferenciado por jogo | `src/jogos/*.py` |
| **RF7** | Histórico cronológico (mais recente primeiro), rankings e filtros | `src/gestor_partidas.py` |
| **RF8** | Persistência automática em ficheiros (CSV / JSON / TXT) com inicialização segura | `data/` |
| **RF9** | Módulos Python independentes com interface comum (`get_name`, `get_instructions`, `play`) | `src/jogos/base_jogo.py` |
| **RF10** | Adivinha o Número (número secreto, intervalos, dicas maior/menor) | `src/jogos/adivinha_numero.py` |
| **RF11** | Pedra, Papel ou Tesoura (rondas contra PC, regras clássicas, placar) | `src/jogos/pedra_papel_tesoura.py` |
| **RF12** | Jogo da Forca (palavras de ficheiro, limite de 6 erros, revelação) | `src/jogos/forca.py` |
| **Jogo Adicional** | Jogo do Galo / Tic-Tac-Toe com matrizes 3x3 contra o PC | `src/jogos/jogo_adicional.py` |

---

## 🤝 Fluxo de Trabalho Git para 3 Pessoas

Para garantir uma colaboração eficiente e sem conflitos de código entre os 3 membros do grupo:

### 1. Criar uma Branch por Funcionalidade
Nunca trabalhem diretamente na branch `main` ao mesmo tempo. Cada colega cria a sua branch:
```bash
# Colega 1 (ex: melhorias na Forca):
git checkout -b feature/forca

# Colega 2 (ex: estatísticas avançadas):
git checkout -b feature/estatisticas

# Colega 3 (ex: regras do jogo adicional):
git checkout -b feature/jogo-galo
```

### 2. Guardar Alterações com Commits Claros
```bash
git add .
git commit -m "feat(forca): adiciona desenho ascii da forca"
```

### 3. Sincronizar Sempre Antes de Enviar
Antes de enviar código ou iniciar uma sessão de trabalho:
```bash
git checkout main
git pull origin main
git checkout feature/sua-branch
git merge main
```

### 4. Enviar para o GitHub e Criar Pull Request (PR)
```bash
git push -u origin feature/sua-branch
```
No GitHub, abram um **Pull Request (PR)** para juntar à branch `main`, revisto pelos outros colegas de grupo.

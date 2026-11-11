# Arcade: Plataforma Modular de Mini-Jogos 🎮

> **ISCTE Sintra - Instituto Universitário de Lisboa**  
> **Unidade Curricular:** Fundamentos de Programação  
> **Ano Letivo:** 2026/2027 – 1º Semestre  
> **Docente Prática:** Prof.ª Catarina Reis (`catarina.reis@iscte-iul.pt`)

---

## 👥 Identificação da Equipa

| Papel | Nome | Número de Aluno | Utilizador GitHub |
|---|---|---|---|
| Aluno 1 | `[Nome Aluno 1]` | `[Número]` | `@TiagoMataGit` |
| Aluno 2 | `[Nome Colega 2]` | `[Número]` | `@[utilizador2]` |
| Aluno 3 | `[Nome Colega 3]` | `[Número]` | `@[utilizador3]` |

> **Nota para a Entrega:**  
> De acordo com o enunciado oficial (Secção 5), o repositório GitHub deve ser nomeado segundo a seguinte convenção:  
> `licenciatura_NumeroAluno1_NumeroAluno2_NumeroAluno3`  
> *(Exemplo: `tdia_11111_22222_33333` ou `dsa_10101_20202_30303`)* e partilhado com **`catarina.reis@iscte-iul.pt`**.

---

## 🚀 Como Abrir e Executar no VS Code

### Pré-requisitos
- **Python 3.10+** (utilizar **apenas a biblioteca padrão do Python**).
- **VS Code** (com a extensão de Python instalada).

### Executar a aplicação
1. Abre esta pasta no **VS Code**:
   ```bash
   code .
   ```
2. No terminal integrado (`Ctrl + ~`), executa:
   ```bash
   python arcade/src/main.py
   ```

---

## 📁 Estrutura de Ficheiros do Projeto

A organização de pastas e módulos respeita a especificação do enunciado (Secção 4):

```text
fp-projeto/
├── .gitignore                      # Ignora ficheiros temporários, cache e venv
├── README.md                       # Documentação da equipa e checklist do projeto
└── arcade/
    ├── data/                       # Armazenamento e persistência de dados (RF8)
    │   ├── words.txt               # Palavras para o Jogo da Forca
    │   ├── jogadores.csv           # Base de dados persistente de jogadores
    │   └── jogos.json              # Catálogo configurável de mini-jogos
    └── src/                        # Código-fonte Python
        ├── __init__.py
        ├── main.py                 # Ponto de entrada, menu e navegação (RF2)
        ├── jogador.py              # Classe Jogador (POO, getters/setters, __str__)
        └── jogos/                  # Módulos independentes dos mini-jogos (RF9)
            ├── __init__.py
            ├── adivinha_numero.py  # Mini-jogo obrigatório (RF10)
            ├── pedra_papel_tesoura.py # Mini-jogo obrigatório (RF11)
            ├── forca.py            # Mini-jogo obrigatório com words.txt (RF12)
            └── jogo_adicional.py   # Mini-jogo adicional escolhido pela equipa
```

*Novas classes e módulos podem ser adicionados pela equipa conforme a necessidade.*

---

## ✅ Checklist de Requisitos do Enunciado

Usem esta checklist para irem marcando o progresso da equipa:

### Requisitos Funcionais
- [ ] **RF1 - Gestão de Jogadores:**
  - [ ] Criar novo jogador com username único
  - [ ] Selecionar jogador existente
  - [ ] Consultar dados básicos (username, nome, datas de criação e última utilização)
  - [ ] Mudar de jogador sem fechar a aplicação
  - [ ] Persistência dos jogadores em CSV (`data/jogadores.csv`)
- [ ] **RF2 - Menu Principal e Navegação:**
  - [ ] Opções: Jogar, Histórico, Estatísticas, Rankings, Gerir Perfil, Mudar Jogador, Sair
  - [ ] Regressar ao menu anterior sem reiniciar
  - [ ] Validação de inputs (não crashar com entradas inválidas)
- [ ] **RF3 - Catálogo de Jogos:**
  - [ ] Obter ID, nome, descrição, instruções e módulo responsável
  - [ ] Leitura a partir de `data/jogos.json`
- [ ] **RF4 - Consulta das Instruções:**
  - [ ] Consultar instruções antes de iniciar partida (fornecidas pelo módulo do jogo)
- [ ] **RF5 - Execução de uma Partida:**
  - [ ] Identificar jogador ativo e executar módulo do jogo selecionado
  - [ ] Comunicar pontuação de volta à plataforma e registar partida
  - [ ] Opção de jogar novamente ou voltar ao menu
- [ ] **RF6 - Sistema de Pontuação:**
  - [ ] Pontuação numérica associada ao desempenho em cada jogo
- [ ] **RF7 - Histórico:**
  - [ ] Listar partidas por ordem cronológica (mais recentes primeiro)
  - [ ] Filtrar histórico por jogo
- [ ] **RF8 - Persistência de Dados:**
  - [ ] Guardar em ficheiros CSV, TXT ou JSON
  - [ ] Inicialização correta mesmo quando os ficheiros ainda não existem
- [ ] **RF9 - Integração Modular dos Jogos:**
  - [ ] Interface comum em cada jogo: `get_name()`, `get_instructions()`, `play()`
- [ ] **RF10 - Adivinha o Número:**
  - [ ] Gerar número aleatório, dicas (maior/menor), contagem de tentativas e pontuação
- [ ] **RF11 - Pedra, Papel ou Tesoura:**
  - [ ] Rondas contra o computador, validação de jogadas, condição de vitória/derrota e pontuação
- [ ] **RF12 - Jogo da Forca:**
  - [ ] Palavras lidas de `data/words.txt`, palavra mascarada, limite de erros e pontuação
- [ ] **Jogo Adicional:**
  - [ ] Desenvolver 4º jogo à escolha da equipa (ex: com matrizes 3x3)

### Requisitos Não Funcionais & Avaliação
- [ ] Execução exclusivamente em consola (sem interfaces gráficas externas)
- [ ] Apenas biblioteca padrão do Python (sem `pip install` de pacotes externos)
- [ ] Utilização obrigatória de Classes e Métodos (`__init__`, `__str__`, getters e setters)
- [ ] Tratamento de erros com `try / except` para não terminar abruptamente
- [ ] Utilização de listas e/ou matrizes para gestão de dados
- [ ] Código limpo, modular, organizado e com comentários

---

## 🤝 Fluxo de Trabalho Git para a Equipa (3 Pessoas)

Para trabalharem os 3 em simultâneo sem sobrescreverem o trabalho uns dos outros:

### 1. Criar uma Branch para cada Funcionalidade
Nunca façam commits diretamente na branch `main`. Cada membro cria a sua própria branch:
```bash
# Exemplo Aluno 1:
git checkout -b feature/jogador

# Exemplo Aluno 2:
git checkout -b feature/forca

# Exemplo Aluno 3:
git checkout -b feature/pedra-papel-tesoura
```

### 2. Fazer Commit do Trabalho Local
```bash
git add .
git commit -m "feat(forca): cria esqueleto da leitura do ficheiro de palavras"
```

### 3. Sincronizar com a `main` antes de Enviar
Antes de submeter código:
```bash
git checkout main
git pull origin main
git checkout feature/tua-branch
git merge main
```

### 4. Enviar a Branch para o GitHub
```bash
git push -u origin feature/tua-branch
```
No GitHub, abram um **Pull Request (PR)** para juntar à `main`, revisto pelos outros colegas.

# 📋 Sistema de Cadastro em Python

> Sistema de cadastro via interface de linha de comando (CLI), com interface aprimorada usando a biblioteca **Rich**. Permite cadastrar, listar e buscar usuários com persistência em arquivo de texto.

---

## 📌 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Módulos](#módulos)
- [Boas Práticas Aplicadas](#boas-práticas-aplicadas)
- [Melhorias Futuras](#melhorias-futuras)
- [Autor](#autor)

---

## 💡 Sobre o Projeto

Este projeto é um **sistema de cadastro de usuários** desenvolvido em Python com foco em organização de código, experiência do usuário e boas práticas de programação. O sistema roda inteiramente no terminal, com uma interface visualmente agradável proporcionada pela biblioteca **Rich**, que adiciona cores, tabelas formatadas e elementos visuais ao CLI.

Os dados dos usuários são armazenados em um arquivo de texto (`Sistema.txt`), garantindo **persistência entre sessões** — ou seja, as informações cadastradas não se perdem ao fechar o programa.

---

## ✅ Funcionalidades

- **Listar usuários** — exibe todos os usuários cadastrados de forma organizada
- **Cadastrar usuário** — adiciona um novo usuário com validação de dados e geração automática de ID único (UUID)
- **Buscar usuário** — permite localizar um usuário específico dentro da base de dados
- **Persistência em arquivo** — os dados são salvos e lidos de um arquivo `.txt`
- **Validação de dados** — entradas do usuário são verificadas antes de serem salvas
- **Interface colorida e formatada** — uso da biblioteca Rich para melhor experiência visual no terminal

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3.x | Linguagem principal do projeto |
| [Rich](https://github.com/Textualize/rich) | Biblioteca para interface CLI rica e colorida |
| UUID | Módulo nativo do Python para geração de IDs únicos |
| `time` (sleep) | Módulo nativo para controle de tempo na interface |
| Arquivo `.txt` | Mecanismo de persistência de dados |

---

## 📁 Estrutura do Projeto

```
Sistema-de-cadastro-em-python/
│
├── sistema.py          # Arquivo principal — ponto de entrada da aplicação
├── Sistema.txt         # Arquivo de persistência dos dados cadastrados
│
└── lib/                # Módulos auxiliares (estrutura modular)
    ├── arquivo.py      # Funções de leitura/escrita no arquivo de dados
    ├── busca.py        # Lógica de busca de usuários
    ├── cadastrar.py    # Lógica de cadastro de novos usuários
    └── interface.py    # Funções de interface com o usuário (menus, exibição)
```

---

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)

---

## 🚀 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/gasaadh/Sistema-de-cadastro-em-python.git
```

2. **Acesse a pasta do projeto:**

```bash
cd Sistema-de-cadastro-em-python
```

3. **Instale a dependência necessária:**

```bash
pip install rich
```

---

## ▶️ Como Usar

Execute o arquivo principal pelo terminal:

```bash
python sistema.py
```

Ao iniciar, o sistema exibirá um menu interativo com as seguintes opções:

```
╔══════════════════════════════╗
║    SISTEMA DE CADASTRO       ║
╠══════════════════════════════╣
║  1. Listar usuários          ║
║  2. Cadastrar usuário        ║
║  3. Buscar usuário           ║
║  4. Sair                     ║
╚══════════════════════════════╝
```

Basta digitar o número da opção desejada e pressionar **Enter**.

> **Nota:** O arquivo `Sistema.txt` é criado automaticamente na primeira execução caso não exista.

---

## 🧩 Módulos

### `sistema.py`
Ponto de entrada da aplicação. Inicializa o arquivo de dados (se necessário) e controla o loop principal do menu.

### `lib/arquivo.py`
Responsável por toda a interação com o arquivo de persistência. Contém funções como:
- `arquivo_existe(nome)` — verifica se o arquivo de dados já existe
- `criar_arquivo(nome)` — cria o arquivo caso não exista
- `ler_arquivo(nome)` — lê e retorna os dados armazenados

### `lib/cadastrar.py`
Contém a lógica de cadastro de novos usuários, incluindo a coleta de dados, validação e geração de UUID único para cada registro.

### `lib/busca.py`
Implementa a funcionalidade de busca, permitindo ao usuário localizar registros pelo nome ou outro campo.

### `lib/interface.py`
Centraliza as funções de exibição: menu principal, listagem formatada de usuários e outros elementos visuais construídos com Rich.

---

## 📐 Boas Práticas Aplicadas

- **Estrutura modular** — código organizado em módulos separados por responsabilidade
- **Geração de UUID** — identificação única e segura para cada usuário cadastrado
- **Validação de entrada** — dados verificados antes de serem persistidos
- **Interface de usuário aprimorada** — uso do Rich para feedback visual claro
- **Criação automática de arquivo** — o sistema se auto-configura na primeira execução
- **Separação de responsabilidades** — cada módulo tem uma função bem definida

---

## 🔮 Melhorias Futuras

- [ ] Adicionar funcionalidade de **editar** um cadastro existente
- [ ] Adicionar funcionalidade de **deletar** um registro
- [ ] Migrar a persistência de `.txt` para **JSON** ou banco de dados SQLite
- [ ] Implementar busca por múltiplos campos (nome, ID, etc.)
- [ ] Adicionar testes unitários com `pytest`
- [ ] Criar um executável standalone com `PyInstaller`

---

## 👤 Autor

**Gabriel Saad**

- GitHub: [@gasaadh](https://github.com/gasaadh)
- Estudante de Sistemas de Informação — FIAP

---

> Projeto desenvolvido como parte do aprendizado em Python, com foco em organização de código e boas práticas de desenvolvimento.

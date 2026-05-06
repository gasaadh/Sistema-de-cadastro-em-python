from rich.console import Console
from rich.table import Table
from datetime import datetime
from rich import print

def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("[red]Houve um erro na criação do arquivo[/]")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def ler_arquivo(arquivo):
    pessoas = []

    try:
        with open(arquivo, 'rt') as a:
            for linha in a:
                dados = linha.strip().split(';')

                if len(dados) < 5:
                    continue

                pessoa = {
                    "id": dados[0],
                    "nome": dados[1],
                    "data_nascimento": dados[2],
                    "email": dados[3],
                    "cpf": dados[4]
                }

                pessoas.append(pessoa)

    except:
        print("[red]Erro ao ler o arquivo[/]")

    return pessoas


console = Console()


def calcular_idade(data):
    nascimento = datetime.strptime(data, "%d/%m/%Y")
    hoje = datetime.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade


def listar_pessoas(pessoas):
    tabela = Table(title="Pessoas Cadastradas")

    tabela.add_column("Nome")
    tabela.add_column("Idade")

    for pessoa in pessoas:
        idade = calcular_idade(pessoa["data_nascimento"])

        tabela.add_row(
            pessoa["nome"],
            str(idade)
        )

    console.print(tabela)
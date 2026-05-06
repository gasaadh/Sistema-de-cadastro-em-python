from rich.prompt import Prompt
from datetime import datetime
import uuid
from rich import print
import re

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except:
        return False

def validar_nome(nome):
    return nome.strip() != "" and not any(char.isdigit() for char in nome)


def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def validar_cpf(cpf):
    padrao = r'^\d{11}$'
    return re.match(padrao, cpf) is not None


def cadastrar_pessoa(arquivo):
    print("[bold cyan]--- Cadastro de Pessoa ---[/bold cyan]")

    # Nome
    while True:
        nome = Prompt.ask("Nome")
        if validar_nome(nome):
            break
        else:
            print("[red]Nome inválido![/red]")

    # Data
    while True:
        data = Prompt.ask("Data de nascimento (dd/mm/aaaa)")
        if validar_data(data):
            break
        else:
            print("[red]Data inválida![/red]")

    # Email
    while True:
        email = Prompt.ask("Email")
        if validar_email(email):
            break
        else:
            print("[red]Email inválido![/red]")

    # CPF
    while True:
        cpf = Prompt.ask("CPF (somente números)")
        if validar_cpf(cpf):
            break
        else:
            print("[red]CPF inválido![/red]")

    pessoa = {
        "id": str(uuid.uuid4()),
        "nome": nome,
        "data_nascimento": data,
        "email": email,
        "cpf": cpf
    }

    salvar_pessoa(arquivo, pessoa)

    print("[green]✔ Pessoa cadastrada com sucesso![/green]")

def salvar_pessoa(arquivo, pessoa):
    with open(arquivo, 'a') as f:
        f.write(f"{pessoa['id']};{pessoa['nome']};{pessoa['data_nascimento']};{pessoa['email']};{pessoa['cpf']}\n")

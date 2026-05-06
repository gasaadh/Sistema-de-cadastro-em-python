from rich.console import Console
from rich.panel import Panel

from .leiaInt import *

console = Console()

def mostrar_menu():
    menu_texto = """
[bold cyan]1.[/] Listar usuários
[bold cyan]2.[/] Cadastrar usuário
[bold cyan]3.[/] Buscar usuário
[bold red]4.[/] Sair
"""


    painel = Panel(
        menu_texto,
        title="[bold magenta]💾 SISTEMA DE CADASTRO[/bold magenta]",
        subtitle="[bold yellow]Escolha uma opção[/bold yellow]",
        border_style="bright_blue",
        padding=(1, 4),
        width=40
    )

    console.print(painel)

    opc = leia_int("Sua Opção: ")
    console.print(opc)
    return opc


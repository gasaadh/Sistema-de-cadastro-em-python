from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console

console = Console()


def buscar_usuario(pessoas):
    nome_busca = Prompt.ask("Digite o nome para buscar")

    resultados = []

    # busca parcial
    for pessoa in pessoas:
        if nome_busca.lower() in pessoa["nome"].lower():
            resultados.append(pessoa)

    #  nenhum encontrado
    if not resultados:
        console.print("[red]Usuário não encontrado[/red]")
        return

    # mostra resultados
    console.print("\n[bold cyan]Resultados encontrados:[/bold cyan]\n")

    for pessoa in resultados:
        console.print(f"[green]{pessoa['nome']}[/green] - ID: [yellow]{pessoa['id']}[/yellow]")

    #  escolher pelo ID
    id_escolhido = Prompt.ask("\nDigite o ID do usuário que deseja ver")

    for pessoa in resultados:
        if pessoa["id"] == id_escolhido:

            texto = f"""
[bold]ID:[/] {pessoa['id']}
[bold]Nome:[/] {pessoa['nome']}
[bold]Nascimento:[/] {pessoa['data_nascimento']}
[bold]Email:[/] {pessoa['email']}
[bold]CPF:[/] {pessoa['cpf']}
"""

            console.print(Panel(texto, title="👤 Detalhes do Usuário"))
            return

    # ID não encontrado
    console.print("[red]ID inválido[/red]")
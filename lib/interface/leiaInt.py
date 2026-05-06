from rich import print

def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Tipo de dado informado está incorreto.[/]')
            continue

        except KeyboardInterrupt:
            print(f'\n[red]O usuário preferiu não informar um número.[/]')
            return 0

        else:
            return num


def leia_float(msg):
    while True:
        try:
            num = float(input(msg))

        except (ValueError, TypeError):
            print('[red]Tipo de dado informado está incorreto.[/]')
            continue
        except KeyboardInterrupt:
            print(f'\n[red]O usuário preferiu não informar um número.[/]')
            return 0

        else:
            return num
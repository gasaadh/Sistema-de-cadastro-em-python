from lib.busca import buscar_usuario
from lib.interface import *
from time import sleep
from lib.arquivo import *
from lib.cadastrar import *

arq = "Sistema.txt"

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = mostrar_menu()
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        pessoas = ler_arquivo(arq)
        listar_pessoas(pessoas)
    elif resposta == 2:
        cadastrar_pessoa(arq)
    elif resposta == 3:
        pessoas = ler_arquivo(arq)
        buscar_usuario(pessoas)
    elif resposta == 4:
        print("Saindo do sistema")
        break
    else:
        print("[red]ERRO: digite uma opção válida [/]")
        sleep(1)

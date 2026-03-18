from rich.console import Console 
import os

cs = Console()


def exibir_caixa(titulo, largura=60):
    topo = "╔" + "═" * (largura - 2) + "╗"
    fundo = "╚" + "═" * (largura - 2) + "╝"
    linha_vazia = "║" + " " * (largura - 2) + "║"
    
    cs.print(f"[bold blue]{topo}")
    cs.print(f"[bold blue]{linha_vazia}")
    
    titulo_formatado = titulo.center(largura - 2)
    cs.print(f"[bold blue]║{titulo_formatado}║")
    
    cs.print(f"[bold blue]{linha_vazia}")
    cs.print(f"[bold blue]{fundo}")

def limpar_terminal():
    os.system("cls")

def menu():
    exibir_caixa("Menu Principal")

    cs.print("[bold blue]1. [/]Painel")
    cs.print("[bold blue]2. [/]Lançamentos")
    cs.print("[bold blue]3. [/]Relatórios")

def escolher_opcao():
    try:
        opcao_escolhida = cs.int(input("\n[blue]Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                cs.print("[bold red]Opção inválida!")
    except:
        menu()
        escolher_opcao()

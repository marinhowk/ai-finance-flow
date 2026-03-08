# --- PIP INSTALL RICH [BIBLIOTECA PARA APLICAR ESTILIZAÇÃO NO TERMINAL]
from rich.console import Console 
import os

cs = Console()


def exibir_caixa(titulo, largura=60):
    topo = "╔" + "═" * (largura - 2) + "╗"
    fundo = "╚" + "═" * (largura - 2) + "╝"
    linha_vazia = "║" + " " * (largura - 2) + "║"
    
    cs.print(f"[bold green]{topo}")
    cs.print(f"[bold green]{linha_vazia}")
    
    titulo_formatado = titulo.center(largura - 2)
    cs.print(f"[bold green]║{titulo_formatado}║")
    
    cs.print(f"[bold green]{linha_vazia}")
    cs.print(f"[bold green]{fundo}")

def limpar_terminal():
    os.system("cls")

def menu():
    limpar_terminal()
    exibir_caixa("Menu Principal")
    
    cs.print("[bold green]1. [/]Realizar login")
    cs.print("[bold green]2. [/]Relizar cadastro")
    cs.print("[bold green]3. [/]Esqueci minha senha")
    
def login():
    limpar_terminal()
    exibir_caixa("Realize o seu login")

    email = input("Email: ")
    senha = input("Senha: ")

    return email, senha

def cadastro():
    limpar_terminal()
    exibir_caixa("Realize o seu cadastro")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirmar_senha = input("Confirme a sua senha: ")

    if not nome or not email or not senha or not confirmar_senha:
        print("É necessário que todos os campos sejam preenchidos!")
        limpar_terminal()
        return cadastro()

    if senha != confirmar_senha:
        print("As senhas digitadas são diferentes!")
        limpar_terminal()
        return cadastro()
    
    return nome, email, senha

def redefinir_senha():
    limpar_terminal()
    exibir_caixa("Redefinir senha")

    email = input("Digite o seu e-mail de cadastro: ")
    limpar_terminal()

    return email

def cadastrar_nova_senha():
    senha = input("Informe a nova senha: ")
    confirmar_senha = input("Confirme a nova senha: ")

    if not senha or not confirmar_senha:
        print("É necessário que todos os campos senham preenchidos")
        return
    
    if senha != confirmar_senha:
        print("As senhas não coincidem!")
        return
    
    return senha

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                login()
            case 2:
                cadastro()
            case 3:
                redefinir_senha()
            case _:
                print("Opção inválida.")
    except:
        limpar_terminal()
        menu()
        escolher_opcao()

    
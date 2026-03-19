# --- PIP INSTALL RICH [BIBLIOTECA PARA APLICAR ESTILIZAÇÃO NO TERMINAL]
from models.user_model import Usuarios
from config.database import BancoDeDados
from controllers.user_controller import UsuariosController
from repository.user_repository import UsuariosRepository
from rich.console import Console
import os
import sys

db = BancoDeDados()
ur = UsuariosRepository(db)
uc = UsuariosController()
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
    limpar_terminal()
    exibir_caixa("Menu Principal")
    
    cs.print("[bold blue]1. [/]Realizar login")
    cs.print("[bold blue]2. [/]Relizar cadastro")
    cs.print("[bold blue]3. [/]Esqueci minha senha")
    cs.print("[bold blue]4. [/]Sair")
    
def login():
    limpar_terminal()
    exibir_caixa("Realize o seu login")

    email = input("Email: ")
    senha = input("Senha: ")

    validar = uc.reliazar_login(email, senha)

    if validar["status"] == "erro":
        print(validar["mensagem"])
    else:
        print("BemVindo")

def cadastro():
    limpar_terminal()
    exibir_caixa("Realize o seu cadastro")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirmar_senha = input("Confirme a sua senha: ")
    usuario = Usuarios(nome, email, senha)

    validar_dados = uc.validar_dados(nome, email, senha, confirmar_senha)

    if validar_dados["status"] == "erro":
        print(validar_dados["mensagem"])
        input("Pressionae ENTER para continuar.")
        return cadastro()
    
    else:
        uc.enviar_email(email)
    
        tentativas = 3

        while tentativas > 0:
            codigo = cs.input("\n[bold blue]Insira o código de verificação enviado em seu e-mail: ")

            validar_codigo = uc.validar_codigo(codigo)

            if validar_codigo["status"] == "ok":
                ur.salvar_cadastro(usuario)
                cs.input("Cadastro realizado, precione ENTER para realizar seu login na plataforma.")
                return login()
            
            else:
                tentativas -= 1
                cs.print(f"[bold red]Código inválido.[/] Tentativas restantes? {tentativas}")

        cs.print("[bold red]Número de tentativas atingido. Código expirado.")

def confirmacao_email():
    limpar_terminal()
    exibir_caixa("Confirmação de E-mail")

    print("Insira o código de verificação que foi enviado em seu e-mail")
    codigo = cs.input("[bold blue]\nCódigo: ")

    return codigo

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
            case 4:
                sys.exit()
            case _:
                print("Opção inválida.")
    except:
        sys.exit()
        #limpar_terminal()
        #menu()
        #escolher_opcao()

    
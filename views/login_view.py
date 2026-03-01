# --- PIP INSTALL RICH [BIBLIOTECA PARA APLICAR ESTILIZAÇÃO NO TERMINAL]
from rich.console import Console 
import os

cs = Console()

def exibir_subtitulo(texto):
    print("=" * 50)
    cs.print(f"[bold green]{texto}")
    print("=" * 50)
  
def limpar_terminal():
    os.system("cls")

def menu():
    cs.print("[bold green]1. Realizar login")
    cs.print("[bold green]2. Relizar cadastro")
    cs.print("[bold green]3. Esqueci minha senha")
    
def login():
    exibir_subtitulo("Realize o seu login")

    email = input("Email: ")
    senha = input("Senha: ")

def cadastro():
    pass
